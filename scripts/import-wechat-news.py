#!/usr/bin/env python3
"""Convert ICACHI WeChat articles listed in a URL file into VitePress news markdown.

Images are downloaded to docs/public/news/ and referenced at
https://media.icachi.org/news/. Upload them with scripts/upload-news-media.sh
before deleting the local copies.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
NEWS_DIR = ROOT / "docs" / "news"
MEDIA_DIR = ROOT / "docs" / "public" / "news"
MEDIA_BASE = "https://media.icachi.org/news"
CACHE_DIR = Path("/tmp/icachi-wx-cache")
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)
TZ = ZoneInfo("Asia/Shanghai")
SKIP_IDS = {
    "EnPQ34wVUD6S5ZjCjsY5eg",
    "rcjL0uiGGMf6poRS59TqrA",
}
THREADS = {y: f"chinese-chi-{y}" for y in range(2013, 2025)}
THREADS[2025] = "ichec-2025"
THREADS[2026] = "ichec-2026"

SLUG_WORDS = [
    ("工作坊", "workshop"),
    ("workshop", "workshop"),
    ("征稿", "cfp"),
    ("征文", "cfp"),
    ("call for papers", "cfp"),
    ("赞助", "sponsor"),
    ("获奖", "award"),
    ("最佳论文", "best-paper"),
    ("best paper", "best-paper"),
    ("颁奖", "award"),
    ("注册", "registration"),
    ("早鸟", "early-bird"),
    ("志愿者", "volunteer"),
    ("回顾", "recap"),
    ("圆满", "recap"),
    ("议程", "program"),
    ("日程", "program"),
    ("程序委员会", "committee"),
    ("短文", "short-paper"),
    ("长文", "full-paper"),
    ("海报", "poster"),
    ("艺术", "art"),
    ("招聘", "hiring"),
    ("理事会", "board"),
    ("换届", "election"),
    ("选举", "election"),
    ("会员", "membership"),
    ("晚宴", "banquet"),
    ("主旨", "keynote"),
    ("keynote", "keynote"),
    ("论坛", "forum"),
    ("圆桌", "panel"),
    ("通知", "notice"),
    ("公告", "notice"),
    ("启事", "notice"),
    ("招募", "call"),
    ("论文", "paper"),
    ("延期", "extension"),
    ("录用", "acceptance"),
    ("住宿", "accommodation"),
    ("直播", "livestream"),
    ("开幕", "opening"),
    ("闭幕", "closing"),
    ("专访", "interview"),
    ("奖学金", "scholarship"),
    ("研讨会", "seminar"),
    ("讲座", "lecture"),
    ("教程", "tutorial"),
    ("博士", "doctoral"),
    ("学生", "student"),
    ("合作", "collaboration"),
    ("成立", "founding"),
    ("年会", "annual"),
    ("照片", "photos"),
    ("参会", "attendance"),
    ("报名", "registration"),
    ("会议", "conference"),
]

DECOR_TEXT = re.compile(
    r"^(?:"
    r"在小说阅读器读本章|"
    r"继续滑动看下一个|"
    r"向上滑动看下一个|"
    r"阅读原文|"
    r"点赞|在看|分享|收藏|"
    r"关注我们|点击关注|点击蓝字关注|"
    r"长按识别二维码.*|长按二维码.*|"
    r"微信扫一扫.*|"
    r"预览时标签不可点|"
    r"不喜欢|知道了|"
    r"华人华侨人机交互|"
    r"ICACHI"
    r")$"
)
DATE_STAMP = re.compile(
    r"^(?:ICACHI\s*)?\d{4}年\d{1,2}月\d{1,2}日(?:\s+\d{1,2}:\d{2})?$"
)
DATE_IN_LINE = re.compile(
    r"20\d{2}\s*年.*\d{1,2}\s*月|\d{1,2}:\d{2}|\bAOE\b"
)
CONF_RE = re.compile(
    r"(ICHEC|Chinese\s*CHI|ChineseCHI|华人\s*CHI|中国人机交互大会)",
    re.I,
)
YEAR_RE = re.compile(r"20\d{2}")
URL_RE = re.compile(r"https?://[^\s<>）)，。；、]+")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.\w+")
SENTENCE_END = re.compile(r"[。！？]")


def fetch_bytes(url: str, referer: str | None = None) -> bytes:
    headers = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"fetch failed {url}: {last_error}")


def load_html(url: str, article_id: str) -> str:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = CACHE_DIR / f"{article_id}.html"
    if cache.exists() and cache.stat().st_size > 1000:
        return cache.read_text(encoding="utf-8", errors="replace")
    data = fetch_bytes(url)
    text = data.decode("utf-8", errors="replace")
    if "secitptpage" in text or "cap_sid" in text or 'id="js_content"' not in text:
        raise RuntimeError("captcha or empty page")
    cache.write_bytes(data)
    time.sleep(0.25)
    return text


def js_unescape(value: str) -> str:
    return (
        value.replace("\\/", "/")
        .replace("\\x26", "&")
        .replace("\\x0a", " ")
        .replace("\\x0d", " ")
        .replace("\\'", "'")
        .replace('\\"', '"')
        .replace("\\n", " ")
    )


def field(raw: str, name: str) -> str | None:
    patterns = [
        rf"var {name} = '(.*?)'\.html\(false\)",
        rf'var {name} = htmlDecode\("(.*?)"\)',
        rf'var {name} = "(.*?)"',
        rf"var {name} = '(.*?)'",
    ]
    for pattern in patterns:
        match = re.search(pattern, raw)
        if match:
            return html.unescape(js_unescape(match.group(1))).strip()
    return None


def og_field(raw: str, prop: str) -> str | None:
    match = re.search(rf'property="{prop}" content="([^"]*)"', raw)
    if not match:
        return None
    return html.unescape(match.group(1)).strip()


def extract_content(raw: str) -> str | None:
    match = re.search(r'<div[^>]*id="js_content"[^>]*>', raw)
    if not match:
        return None
    start = match.end()
    depth = 1
    for token in re.finditer(r"<div\b|</div>", raw[start:], re.I):
        if token.group(0).lower().startswith("</"):
            depth -= 1
            if depth == 0:
                return html.unescape(raw[start : start + token.start()])
        else:
            depth += 1
    return None


def style_font(style: str) -> int | None:
    match = re.search(r"font-size:\s*(\d+(?:\.\d+)?)px", style or "", re.I)
    return int(float(match.group(1))) if match else None


def style_highlight(style: str) -> bool:
    match = re.search(r"background(?:-color)?:\s*([^;]+)", style or "", re.I)
    if not match:
        return False
    value = match.group(1).strip().lower()
    return value not in {"transparent", "none", "rgba(0, 0, 0, 0)", "initial", "inherit"}


def style_hidden(style: str) -> bool:
    return bool(re.search(r"display\s*:\s*none", style or "", re.I))


class ArticleParser(HTMLParser):
    VOID = {"img", "br", "hr", "source", "meta", "link", "input", "wbr"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple] = []
        self.stack: list[dict] = []
        self.para: dict | None = None
        self.list_kind: list[str] = []

    def _hidden(self) -> bool:
        return any(item["hidden"] for item in self.stack)

    def _font(self) -> int | None:
        for item in reversed(self.stack):
            if item["font"]:
                return item["font"]
        return None

    def _highlight(self) -> bool:
        return any(item["highlight"] for item in self.stack)

    def _bold(self) -> bool:
        return any(item["bold"] for item in self.stack)

    def _italic(self) -> bool:
        return any(item["italic"] for item in self.stack)

    def _href(self) -> str | None:
        for item in reversed(self.stack):
            if item["href"]:
                return item["href"]
        return None

    def handle_starttag(self, tag, attrs):
        self._start(tag, attrs, void=tag in self.VOID)

    def handle_startendtag(self, tag, attrs):
        self._start(tag, attrs, void=True)

    def _start(self, tag: str, attrs, void: bool) -> None:
        ad = {key: value or "" for key, value in attrs}
        style = ad.get("style", "")
        hidden = style_hidden(style) or tag in {"script", "style", "mp-style-type"}
        if self._hidden():
            hidden = True
        frame = {
            "tag": tag,
            "hidden": hidden,
            "font": style_font(style),
            "highlight": style_highlight(style),
            "bold": tag in {"strong", "b"},
            "italic": tag in {"em", "i"},
            "href": ad.get("href") if tag == "a" else None,
        }
        if not void:
            self.stack.append(frame)
        if hidden or self._hidden():
            return
        if tag == "img":
            self._flush_para(force=True)
            src = ad.get("data-src") or ad.get("src") or ""
            ratio = ad.get("data-ratio") or ""
            width = ad.get("data-w") or ""
            self.blocks.append(("img", src, ratio, width))
            return
        if tag == "br":
            self._add_text("\n")
            return
        if tag in {"ul", "ol"}:
            self._flush_para(force=True)
            self.list_kind.append("ol" if tag == "ol" else "ul")
            return
        if tag in {"p", "li", "h1", "h2", "h3", "h4"}:
            self._flush_para(force=True)
            inside_li = tag == "li" or any(item["tag"] == "li" for item in self.stack)
            kind = self.list_kind[-1] if inside_li and self.list_kind else None
            self.para = {
                "tag": "li" if inside_li else tag,
                "runs": [],
                "list": kind or ("ul" if inside_li else None),
            }

    def handle_endtag(self, tag):
        if tag in {"p", "li", "h1", "h2", "h3", "h4"}:
            self._flush_para(force=True)
        if tag in {"ul", "ol"} and self.list_kind:
            self.list_kind.pop()
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        if self._hidden():
            return
        self._add_text(data)

    def _add_text(self, data: str) -> None:
        if data is None:
            return
        if self.para is None:
            if not data.strip():
                return
            self.para = {"tag": "p", "runs": [], "list": None}
        run = {
            "text": data,
            "bold": self._bold(),
            "italic": self._italic(),
            "href": self._href(),
            "highlight": self._highlight(),
            "font": self._font(),
        }
        runs = self.para["runs"]
        if runs and {k: runs[-1][k] for k in ("bold", "italic", "href", "highlight", "font")} == {
            k: run[k] for k in ("bold", "italic", "href", "highlight", "font")
        }:
            runs[-1]["text"] += data
        else:
            runs.append(run)

    def _flush_para(self, force: bool = False) -> None:
        if not self.para:
            return
        text = "".join(run["text"] for run in self.para["runs"])
        if not text.strip() and not force:
            return
        if text.strip():
            self.blocks.append(("text", self.para))
        self.para = None

    def close(self):
        super().close()
        self._flush_para(force=True)


def clean_text(text: str) -> str:
    text = text.replace("\xa0", " ").replace("\u200b", "").replace("\ufeff", "")
    text = text.replace("在小说阅读器读本章", "")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def plain_text(para: dict) -> str:
    return clean_text("".join(run["text"] for run in para["runs"]))


def is_decorative_text(text: str) -> bool:
    compact = re.sub(r"\s+", "", text)
    if not compact:
        return True
    if compact in {"●", "○", "·", "•", "｜", "|", "—", "–", "-", "★", "☆"}:
        return True
    if DECOR_TEXT.match(compact) or DECOR_TEXT.match(text.strip()):
        return True
    if DATE_STAMP.match(text.strip()):
        return True
    if "扫一扫" in compact and "关注" in compact:
        return True
    if len(compact) <= 40 and ("愿与你共同成长" in compact or compact.startswith("华人华侨人机交互")):
        return True
    if "是首个由华人华侨创立" in compact or "是第一个由华人华侨创立" in compact:
        return True
    if compact.startswith("世界华人华侨人机交互协会") and "icachi.org" in compact.lower() and len(compact) < 220:
        return True
    if re.fullmatch(r"点击上方.*关注.*", compact):
        return True
    return False


def is_heading(para: dict, text: str) -> bool:
    if para["tag"] == "li" or para["list"]:
        return False
    if not text or len(text) > 70:
        return False
    if SENTENCE_END.search(text):
        return False
    if re.search(r"[.!?]\s*$", text) and len(text.split()) >= 6:
        return False
    if "http://" in text or "https://" in text or "@" in text:
        return False
    if DATE_IN_LINE.search(text):
        return False
    if re.search(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\b", text, re.I):
        return False
    if re.fullmatch(r"\d{1,2}", text):
        return False
    if re.search(r"[：:]\s*\S.{6,}", text):
        return False
    if ("｜" in text or "|" in text) and not re.search(r"会议|简介|征稿|Workshop|Overview|Guideline", text, re.I):
        return False
    if text.count(",") >= 1 and len(text) > 28:
        return False
    if re.search(r"[（(].+[）)]", text) and not re.search(r"会议|简介|征稿|Workshop", text):
        return False
    runs = [run for run in para["runs"] if clean_text(run["text"])]
    if not runs:
        return False
    all_bold = all(run["bold"] for run in runs)
    all_highlight = all(run["highlight"] for run in runs)
    font = max((run["font"] or 0) for run in runs)
    if font >= 24 and len(text) <= 40:
        return True
    if all_bold and len(text) <= 56 and text.count("，") == 0 and text.count(",") == 0:
        return True
    if all_highlight and len(text) <= 24 and "（" not in text and "(" not in text:
        return True
    if re.match(r"^(会议简介|会议概况|征稿选题|征稿事宜|关于)", text):
        return True
    return False


def render_runs(runs: list[dict], force_plain: bool = False) -> str:
    pieces: list[str] = []
    for run in runs:
        text = clean_text(run["text"]) if False else run["text"]
        text = text.replace("\xa0", " ").replace("\u200b", "").replace("在小说阅读器读本章", "")
        text = re.sub(r"[ \t]{2,}", " ", text)
        if not text.strip() and "\n" not in text:
            continue
        inner = text.strip() if text.strip() == text or not pieces else text
        # Keep internal spacing but trim each run's edges when it is the whole token.
        inner = inner.strip()
        if not inner:
            continue
        if not force_plain and run["bold"] and run["italic"]:
            inner = f"***{inner}***"
        elif not force_plain and run["bold"]:
            inner = f"**{inner}**"
        elif not force_plain and run["italic"]:
            inner = f"*{inner}*"
        if run["href"]:
            href = run["href"].strip()
            if href and not href.startswith("javascript"):
                inner = f"[{inner}]({href})"
        pieces.append(inner)
    merged = " ".join(pieces)
    merged = re.sub(r"\s+([，。！？、；：])", r"\1", merged)
    merged = re.sub(r"[ \t]{2,}", " ", merged).strip()
    merged = linkify(merged)
    merged = re.sub(r"(?:\s|\*)*(?:关注我们|点赞|在看|阅读原文)(?:\s|\*)*$", "", merged).strip()
    return merged


def linkify(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        url = match.group(0).rstrip(".,;")
        start = match.start()
        if start >= 2 and text[start - 2 : start] == "](":
            return match.group(0)
        if start >= 1 and text[start - 1] in "([":
            return match.group(0)
        return f"[{url}]({url})"

    return URL_RE.sub(repl, text)


def looks_like_qr(ratio: str, width: str) -> bool:
    try:
        parsed_ratio = float(ratio) if ratio else None
    except ValueError:
        parsed_ratio = None
    try:
        parsed_width = int(float(width)) if width else None
    except ValueError:
        parsed_width = None
    if parsed_width is not None and parsed_width <= 48:
        return True
    if parsed_ratio is not None and parsed_width is not None and 0.9 <= parsed_ratio <= 1.1 and parsed_width <= 320:
        return True
    return False


def is_decorative_image(src: str, ratio: str, width: str) -> bool:
    if not src or src.startswith("data:"):
        return True
    if "qrcode" in src.lower() or "/qr_" in src.lower():
        return True
    try:
        if ratio and float(ratio) < 0.15:
            return True
    except ValueError:
        pass
    try:
        if width and int(float(width)) < 80:
            return True
    except ValueError:
        pass
    return False


def find_conference_year(text: str) -> int | None:
    for match in CONF_RE.finditer(text):
        window_start = max(0, match.start() - 16)
        window_end = min(len(text), match.end() + 16)
        window = text[window_start:window_end]
        years = YEAR_RE.findall(window)
        if years:
            # Prefer the year written closest to the conference name.
            nearest = min(years, key=lambda year: abs(window.find(year) - (match.start() - window_start)))
            return int(nearest)
    return None


def thread_for(title: str, body: str) -> str | None:
    year = find_conference_year(title)
    if year is None:
        year = find_conference_year(body[:1200])
    if year is None:
        return None
    return THREADS.get(year)


def tags_for(title: str) -> list[str]:
    if re.search(r"征稿|征文|投稿启事|Call for Papers|\bCFP\b", title, re.I):
        return ["征稿"]
    if re.search(r"获奖|颁奖|最佳论文|Best Paper|Award", title, re.I):
        return ["获奖"]
    if re.search(r"工作坊|论坛|圆桌|沙龙|Workshop|圆满|回顾", title, re.I):
        return ["活动"]
    if re.search(r"通知|公告|启事|招募|注册|报名|征集", title):
        return ["通知"]
    return []


def slug_for(title: str, article_id: str, used: set[str], date: str) -> str:
    parts: list[str] = []
    year = find_conference_year(title)
    if year:
        kind = "ichec" if year >= 2025 else "chinesechi"
        # Confirm the nearby name so a bare year is not misread.
        if re.search(r"ICHEC", title, re.I) and year >= 2025:
            parts.append(f"ichec{year}")
        elif re.search(r"Chinese\s*CHI|ChineseCHI|华人\s*CHI", title, re.I):
            parts.append(f"chinesechi{year}")
        elif re.search(r"ICHEC", title, re.I):
            parts.append(f"ichec{year}")
        else:
            parts.append(f"{kind}{year}")
    lowered = title.lower()
    seen: set[str] = set()
    generic = {"notice", "conference", "call"}
    specific: list[str] = []
    generic_hits: list[str] = []
    for needle, token in SLUG_WORDS:
        if needle.lower() in lowered and token not in seen:
            seen.add(token)
            if token in generic:
                generic_hits.append(token)
            else:
                specific.append(token)
    parts.extend(specific[:3] or generic_hits[:1])
    if not parts:
        parts.append("article-" + re.sub(r"[^a-z0-9]", "", article_id.lower())[:8])
    base = "-".join(parts)
    base = re.sub(r"-{2,}", "-", base).strip("-")
    candidate = base
    # used keys include the date so the same slug on another day is fine
    key = f"{date}-{candidate}"
    index = 2
    while key in used:
        candidate = f"{base}-{index}"
        key = f"{date}-{candidate}"
        index += 1
    used.add(key)
    return candidate


def clip_description(paragraphs: list[str]) -> str:
    for paragraph in paragraphs:
        if paragraph.startswith("｜") or paragraph.startswith("|"):
            continue
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda match: match.group(1), paragraph)
        text = re.sub(r"[#*`>\[\]]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        if "｜" in text or len(text) < 24:
            continue
        sentence = re.split(r"(?<=[。！？!?])", text, maxsplit=1)[0].strip()
        if len(sentence) < 12:
            sentence = text
        if len(sentence) > 50:
            sentence = sentence[:50]
            if re.search(r"[A-Za-z0-9]$", sentence) and " " in sentence:
                sentence = sentence.rsplit(" ", 1)[0]
            sentence = sentence.rstrip("，,、；; ") + "…"
        return sentence
    return ""


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def ext_from(url: str, data: bytes) -> str:
    match = re.search(r"wx_fmt=([a-z0-9]+)", url, re.I)
    if match:
        fmt = match.group(1).lower()
        return {"jpeg": "jpg", "jpg": "jpg", "png": "png", "gif": "gif", "webp": "webp", "svg": "svg"}.get(fmt, fmt)
    if data.startswith(b"\xff\xd8"):
        return "jpg"
    if data.startswith(b"\x89PNG"):
        return "png"
    if data.startswith(b"GIF"):
        return "gif"
    if data.startswith(b"RIFF") and b"WEBP" in data[:16]:
        return "webp"
    return "jpg"


def save_image(url: str, stem: str, referer: str, saved: dict[str, str]) -> str | None:
    if url in saved:
        return saved[url]
    existing = [path for path in MEDIA_DIR.glob(stem + ".*") if path.is_file()]
    if len(existing) == 1:
        saved[url] = existing[0].name
        return existing[0].name
    try:
        data = fetch_bytes(url, referer=referer)
    except Exception as exc:  # noqa: BLE001
        print(f"  image failed {url[:80]} {exc}", file=sys.stderr)
        return None
    if len(data) < 800:
        return None
    ext = ext_from(url, data)
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{stem}.{ext}"
    (MEDIA_DIR / filename).write_bytes(data)
    saved[url] = filename
    return filename


def blocks_to_markdown(blocks: list[tuple], title: str) -> tuple[list[str], list[str]]:
    lines: list[str] = []
    images: list[str] = []
    list_open = False

    def close_list() -> None:
        nonlocal list_open
        list_open = False

    for block in blocks:
        if block[0] == "img":
            _, src, ratio, width = block
            if is_decorative_image(src, ratio, width):
                continue
            close_list()
            images.append(src)
            marker = "qr" if looks_like_qr(ratio, width) else "photo"
            lines.append(f"![配图]({src})" if marker == "photo" else f"<!--qr-->![配图]({src})")
            continue
        para = block[1]
        text = plain_text(para)
        if is_decorative_text(text):
            continue
        if text == title:
            continue
        if is_heading(para, text):
            previous = next((line for line in reversed(lines) if line.strip()), "")
            if previous.startswith("### ") and previous.rstrip().endswith(("：", ":")):
                close_list()
                rendered = render_runs(para["runs"])
                rendered = clean_text(rendered)
                if rendered:
                    lines.append(rendered)
                continue
            close_list()
            lines.append(f"### {text}")
            continue
        rendered = render_runs(para["runs"])
        rendered = clean_text(rendered)
        if not rendered or is_decorative_text(rendered):
            continue
        if para["tag"] == "li" or para["list"]:
            marker = "1." if para["list"] == "ol" else "-"
            lines.append(f"{marker} {rendered}")
            list_open = True
            continue
        close_list()
        lines.append(rendered)

    # Drop a trailing QR-style image when the last text mentions following the account.
    cleaned: list[str] = []
    for line in lines:
        compact = re.sub(r"\s+", "", line)
        if any(token in compact for token in ("扫码关注", "识别二维码", "关注公众号", "阅读原文", "点赞", "在看")):
            continue
        cleaned.append(line)
    while cleaned and cleaned[-1].startswith("<!--qr-->"):
        cleaned.pop()
    cleaned = [line.replace("<!--qr-->", "") for line in cleaned]
    return cleaned, images


def article_id_from(url: str) -> str:
    match = re.search(r"/s/([^/?#]+)", url)
    if not match:
        raise ValueError(url)
    return match.group(1)


def convert(url: str, used_slugs: set[str], download: bool) -> dict:
    article_id = article_id_from(url)
    raw = load_html(url, article_id)
    if "环境异常" in raw or "该内容已被发布者删除" in raw or "此内容因违规无法查看" in raw:
        raise RuntimeError("unavailable")
    title = og_field(raw, "og:title") or field(raw, "msg_title")
    if not title:
        raise RuntimeError("missing title")
    title = re.sub(r"\s+", " ", title).strip()
    ct = field(raw, "ct")
    if not ct or not ct.isdigit():
        match = re.search(r'var ct = "(\d+)"', raw)
        ct = match.group(1) if match else None
    if not ct:
        raise RuntimeError("missing date")
    published = datetime.fromtimestamp(int(ct), TZ)
    date = published.strftime("%Y-%m-%d")
    content = extract_content(raw)
    if not content:
        raise RuntimeError("missing content")
    parser = ArticleParser()
    parser.feed(content)
    parser.close()
    lines, images = blocks_to_markdown(parser.blocks, title)
    body_text = "\n".join(lines)
    description = clip_description([
        line for line in lines
        if not line.startswith("### ") and "![" not in line
    ])
    if not description or is_decorative_text(description):
        description = title if len(title) <= 50 else title[:50].rstrip("，,、；; ") + "…"
    slug = slug_for(title, article_id, used_slugs, date)
    thread = thread_for(title, body_text)
    tags = tags_for(title)
    cover_url = field(raw, "msg_cdn_url") or og_field(raw, "og:image")
    saved: dict[str, str] = {}
    cover_name = None
    image_jobs: list[tuple[str, str]] = []
    if cover_url:
        image_jobs.append((cover_url, f"{date}-{slug}-cover"))
    body_sources: list[str] = []
    for line in lines:
        match = re.match(r"!\[配图\]\((.*)\)$", line)
        if match:
            body_sources.append(match.group(1))
    for index, src in enumerate(body_sources, start=1):
        image_jobs.append((src, f"{date}-{slug}-{index:02d}"))
    if download and image_jobs:
        with ThreadPoolExecutor(max_workers=6) as pool:
            futures = {
                pool.submit(save_image, src, stem, url, saved): (src, stem)
                for src, stem in image_jobs
            }
            for future in futures:
                future.result()
        if cover_url:
            cover_name = saved.get(cover_url)
        rewritten: list[str] = []
        body_index = 0
        for line in lines:
            match = re.match(r"!\[配图\]\((.*)\)$", line)
            if not match:
                rewritten.append(line)
                continue
            src = match.group(1)
            filename = saved.get(src)
            if not filename:
                body_index += 1
                continue
            body_index += 1
            rewritten.append(f"![配图]({MEDIA_BASE}/{filename})")
        lines = rewritten
    elif images:
        lines = [line if not line.startswith("![配图](") else line for line in lines]

    front = ["---", f"title: {yaml_quote(title)}", f"date: {date}", f"description: {yaml_quote(description)}"]
    if cover_name:
        front.append(f"cover: {MEDIA_BASE}/{cover_name}")
    if thread:
        front.append(f"thread: {thread}")
    if tags:
        front.append("tags:")
        for tag in tags:
            front.append(f"  - {tag}")
    front.append(f"source: {yaml_quote(url)}")
    front.append("lang: zh")
    front.append("---")
    chunks: list[str] = []
    for line in lines:
        if chunks and chunks[-1].startswith(("- ", "1. ")) and line.startswith(("- ", "1. ")):
            chunks[-1] = chunks[-1] + "\n" + line
        else:
            chunks.append(line)
    body = "<NewsCover />\n\n" + "\n\n".join(chunks).strip() + "\n"
    body = re.sub(r"\n{3,}", "\n\n", body)
    filename = f"{date}-{slug}.md"
    return {
        "id": article_id,
        "file": filename,
        "title": title,
        "date": date,
        "thread": thread,
        "tags": tags,
        "images": len(list(MEDIA_DIR.glob(f"{date}-{slug}-*"))) if download else len(images),
        "markdown": "\n".join(front) + "\n\n" + body,
    }


def read_urls(path: Path) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        article_id = article_id_from(line)
        if article_id in seen or article_id in SKIP_IDS:
            continue
        seen.add(article_id)
        urls.append(line.split()[0])
    return urls


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url_file", type=Path)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--no-download", action="store_true")
    parser.add_argument("--stdout", action="store_true", help="print markdown instead of writing files")
    args = parser.parse_args()
    urls = read_urls(args.url_file)
    if args.limit:
        urls = urls[: args.limit]
    used: set[str] = set()
    for existing in NEWS_DIR.glob("*.md"):
        match = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", existing.name)
        if match and not existing.name.startswith("_"):
            used.add(f"{match.group(1)}-{match.group(2)}")
    ok = 0
    failures: list[dict] = []
    for index, url in enumerate(urls, start=1):
        article_id = article_id_from(url)
        print(f"[{index}/{len(urls)}] {article_id}", flush=True)
        try:
            result = convert(url, used, download=not args.no_download)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL {exc}", file=sys.stderr)
            failures.append({"url": url, "error": str(exc)})
            continue
        if args.stdout:
            print(result["markdown"])
            print("\n----- FILE", result["file"], "-----\n")
        else:
            (NEWS_DIR / result["file"]).write_text(result["markdown"], encoding="utf-8")
        ok += 1
        print(f"  {result['file']} images={result['images']} thread={result['thread']} tags={result['tags']}")
    report = CACHE_DIR / "failures.json"
    report.write_text(json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"done ok={ok} fail={len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
