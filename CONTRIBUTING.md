# 网站内容协作指南

本指南面向协作者，说明如何补充两类内容：

1. [往届理事会成员](#任务一往届理事会成员)
2. [新闻文章](#任务二新闻文章)

---

## 准备工作

确认你已被添加为本仓库的 **Collaborator**（联系管理员）。所有修改通过 **Pull Request** 提交，不要直接推送到 `main` 分支。

---

## 任务一：往届理事会成员

### 文件位置

```
data/past-boards/
├── board-2024.json   ✅ 已有
├── board-2022.json   ← 待补充
├── board-2020.json   ✅ 已有
├── board-2018.json   ← 待补充
├── board-2016.json   ← 待补充
├── board-2014.json   ← 待补充
└── board-2012.json   ← 待补充（创始届）
```

每届一个文件，以任期开始年份命名。

### JSON 格式

```json
[
  {
    "name": "付志勇 Zhiyong Fu",
    "role": "President",
    "org": "清华大学"
  },
  {
    "name": "麻晓娟 Xiaojuan Ma",
    "role": "Executive Vice President",
    "org": "香港科技大学",
    "avatar": "/images/board/maxiaojuan.png"
  }
]
```

### 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `name` | ✅ | 中文姓名 + 英文姓名，空格分隔 |
| `role` | ✅ | 职位（英文），见下方列表 |
| `org` | ✅ | 所在机构 |
| `avatar` | 可选 | 头像路径，**暂无可省略**，后续单独补充 |

### 常用职位（role）

```
President
Executive Vice President
Vice President
Secretary General
Treasurer
Director
Supervisor
```

参考 `data/past-boards/board-2024.json` 中已有的写法保持一致。

### 第一步：只填文字信息（头像后续补）

**先不用管头像**，把姓名、职位、机构填齐即可：

```json
[
  {
    "name": "张三 San Zhang",
    "role": "Director",
    "org": "某大学"
  }
]
```

### 第二步：补充头像（有图片时再做）

- 图片放在 `docs/public/images/board/` 目录
- 文件名用拼音小写，如 `zhangsan.jpg`
- 格式：JPG / PNG，建议正方形，至少 200×200px
- 在 JSON 中补充：`"avatar": "/images/board/zhangsan.jpg"`

### 如何在 GitHub 上提交

**新建文件（推荐新手）**

1. 进入仓库的 `data/past-boards/` 目录
2. 点击右上角 **Add file → Create new file**
3. 文件名填写，例如：`board-2018.json`
4. 粘贴 JSON 内容（可以复制 `board-2020.json` 的结构再修改）
5. 页面下方点击 **Propose new file**，填写说明后提交 PR

**格式检查**：提交前可将 JSON 内容粘贴到 [jsonlint.com](https://jsonlint.com) 验证格式是否正确。

---

## 任务二：新闻文章

### 文件位置

```
docs/news/
├── _template.md                           ← 模板（复制它来开始）
├── 2025-12-08-ichec2025-recap.md
├── 2026-05-20-ichec2026-cfp-full.md
└── ...
```

### 文件命名规范

格式：`YYYY-MM-DD-slug.md`

- `YYYY-MM-DD`：文章发布日期（微信公众号发布日期）
- `slug`：英文短标题，单词用 `-` 连接，尽量简洁

> 示例：`2024-08-15-ichec2024-award.md`

中文文件名也可接受，但英文 slug 对 URL 更友好。

### 文章开头格式（frontmatter）

每篇文章开头必须包含以下信息块：

```markdown
---
title: "文章标题"
date: 2024-08-15
description: "一句话摘要，50字以内，显示在新闻列表预览中"
cover: /images/news/文件名.jpg
tags:
  - ICHEC 2024
source: "https://mp.weixin.qq.com/s/..."
lang: zh
---

<NewsCover />
正文从这里开始...
```

| 字段 | 必填 | 说明 |
|------|------|------|
| `title` | ✅ | 文章标题 |
| `date` | ✅ | 发布日期 `YYYY-MM-DD` |
| `description` | ✅ | 列表摘要，不超过 50 字 |
| `cover` | 建议 | 封面图路径，公众号文章一般都有封面，尽量补充 |
| `tags` | 建议 | 分类标签，见下方列表 |
| `source` | 可选 | 原公众号链接，存档用，没有可删掉这行 |
| `lang` | 可选 | `zh`（默认）或 `en` |

**注意**：`title` 和 `description` 如包含冒号 `:` 或引号，改用单引号包裹整个值：
```yaml
description: '2024年ICHEC：年会在北京圆满落幕'
```

### 常用 tags

```
ICHEC 2026 / ICHEC 2025 / ICHEC 2024 …（年度会议）
征稿 / 获奖 / 通知 / 活动
```

### 封面图

封面图**尽量提供**——公众号文章都有封面，如有原图请一并上传。

- 图片放在 `docs/public/images/news/` 目录
- 文件名与文章 slug 对应，如 `ichec2024-award.jpg`
- 建议宽度至少 800px，比例 3:2

---

### 方式一：Obsidian Web Clipper（适合微信公众号文章）

用这个方式可以直接把公众号文章裁剪为 Markdown，效率最高。

#### 安装

1. 安装 [Obsidian](https://obsidian.md)（免费桌面笔记软件）
2. 在 Chrome / Edge 安装 [Obsidian Web Clipper](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf) 扩展

#### 配置模板

打开 Web Clipper 扩展 → **Settings → Templates → 新建模板**，粘贴以下内容：

```
---
title: "{{title}}"
date: {{date:YYYY-MM-DD}}
description: ""
cover: 
tags:
  - 
source: "{{url}}"
lang: zh
---

<NewsCover />
{{content}}
```

将模板命名为 `ICACHI News`，保存。

#### 使用步骤

1. 在电脑浏览器打开微信公众号文章
2. 点击浏览器工具栏中的 Web Clipper 图标
3. 模板选择 `ICACHI News`，确认标题和日期无误
4. 点击 **Add to Obsidian**，保存到 Obsidian 的某个文件夹
5. 在 Obsidian 中：
   - 补充 `description`（摘要）
   - 补充 `tags`
   - 检查正文，删除公众号末尾的"阅读原文""关注我们"等无关内容
6. 将文件重命名为 `YYYY-MM-DD-slug.md`
7. 将 `.md` 文件上传到 GitHub 的 `docs/news/` 目录（见下方"如何在 GitHub 上提交"）

---

### 方式二：直接在 GitHub 上编写

1. 进入仓库 `docs/news/` 目录
2. 点击 **Add file → Create new file**
3. 文件名填写，例如：`2024-08-15-ichec2024-award.md`
4. 复制 `_template.md` 的内容作为起点，填写正文
5. 页面下方点击 **Propose new file**，填写说明后提交 PR

---

### 如何在 GitHub 上提交 Markdown 文件和图片

**上传单个 .md 文件**

1. 进入 `docs/news/` 目录
2. 点击 **Add file → Upload files**
3. 拖入 `.md` 文件
4. 填写提交说明（如"Add ICHEC 2024 recap article"），提交 PR

**上传封面图**

1. 进入 `docs/public/images/news/` 目录
2. 点击 **Add file → Upload files**
3. 上传图片文件
4. 确保文章 frontmatter 中的 `cover` 路径与文件名一致

---

## 常见问题

**Q：JSON 格式提交后页面显示异常？**  
将 JSON 内容粘贴到 [jsonlint.com](https://jsonlint.com) 检查，最常见的问题是最后一个成员后面多了逗号 `,`。

**Q：frontmatter 里有特殊字符导致解析出错？**  
把有问题的那行改为单引号：`description: '含有:冒号的文字'`

**Q：不确定某人的英文姓名怎么写？**  
参考该成员发表的论文署名，或谷歌搜索其机构主页。

**Q：提交 PR 后需要等多久？**  
联系管理员审核合并，合并后网站会自动部署（约 2 分钟生效）。
