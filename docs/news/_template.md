---
title: "文章标题"
date: YYYY-MM-DD
description: "一句话摘要，显示在新闻列表预览中（建议 50 字以内）。"
cover: /images/news/文件名.jpg
thread: ichec-2026
tags:
  - 征稿
source: "https://mp.weixin.qq.com/s/..."
lang: zh
---

<NewsCover />
正文从这里开始。删除上方 source 行如果没有原文链接。

## 字段说明

| 字段 | 是否必填 | 说明 |
|------|----------|------|
| `title` | ✅ | 文章标题，显示在列表和页面 `<h1>` |
| `date` | ✅ | 发布日期 `YYYY-MM-DD`，用于排序 |
| `description` | ✅ | 列表摘要，不填则自动截取正文首段 |
| `cover` | 可选 | 封面图，放在 `docs/public/images/news/` 下 |
| `thread` | 可选 | 所属会议时间线的稳定标识，必须与 `data/conferences.json` 中的 `thread` 一致 |
| `tags` | 可选 | 标签数组，用于列表筛选 |
| `source` | 可选 | 原文链接（公众号 URL 等），存档用 |
| `lang` | 可选 | `zh`（默认）或 `en` |

## Thread 与 tags

- `thread` 表示文章所属的年度会议，例如 `ichec-2026`。
- `tags` 只表示内容类别，例如：
- `征稿` / `获奖` / `通知` / `活动`

## 文件命名规范

`YYYY-MM-DD-slug.md`，例如：`2026-05-20-ichec2026-cfp-full.md`

中文文件名也可接受，但 slug 形式对 URL 更友好。
