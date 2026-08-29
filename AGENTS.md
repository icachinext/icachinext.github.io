# AGENTS.md

本文件适用于仓库根目录及所有子目录，供在本项目中工作的自动化编码代理使用。

## 项目概览

- 本项目是 ICACHI（世界华人华侨人机交互协会）的中英文官方网站。
- 技术栈为 VitePress 1、Vue 3、TypeScript/JavaScript、Markdown、JSON 和 CSS。
- 网站由 GitHub Pages 托管；推送到 `main` 或 `master` 后，GitHub Actions 会使用 Node.js 20 构建并部署。
- 中文站位于 `/`，英文站位于 `/en/`。
- 项目没有后端、数据库或运行时 API；内容均在构建时从仓库文件加载。

## 目录职责

- `docs/`：VitePress 页面和新闻 Markdown。
  - `docs/en/`：英文页面；中文页面有对应英文版本时，应一并检查是否需要同步。
  - `docs/news/`：中文新闻，文件名使用 `YYYY-MM-DD-slug.md`。
  - `docs/en/news/`：英文新闻。
  - `docs/public/`：原样发布的静态资源；代码中的 URL 从站点根路径开始，例如 `/images/icachi.svg`。
  - `docs/.vitepress/config.mts`：站点、导航、locale 和搜索配置。
  - `docs/.vitepress/theme/`：主题入口、自定义布局、全局样式和设计变量。
- `components/`：在主题入口注册或由其他组件引用的 Vue 组件。
- `data/`：结构化站点内容。
  - `site.json` / `site.en.json`：中英文首页、按钮和页脚文案。
  - `board.json`：现任理事会。
  - `past-boards/board-YYYY.json`：往届理事会。
  - `conferences.json`：会议列表。
  - `resources.json`：中英文资源列表。
- `.github/workflows/deploy.yml`：GitHub Pages 构建和部署流程。
- `CONTRIBUTING.md`：面向内容贡献者的新闻和往届理事会录入规范；涉及这些内容时以其格式要求为准。

## 环境与常用命令

使用 Node.js 20，并以 `package-lock.json` 为依赖版本依据。

```bash
npm ci
npm run docs:dev
npm run docs:build
npm run docs:preview
```

- 本地开发服务器默认由 VitePress 提供。
- 提交前至少运行 `npm run docs:build`。
- 仓库目前没有独立的 lint、format 或 test 脚本；不要声称运行过不存在的检查。
- 不要提交 `node_modules/`、`docs/.vitepress/cache/` 或 `docs/.vitepress/dist/`。

## 实现约定

### Vue 与 VitePress

- 现有组件使用 Vue Composition API 和 `<script setup>`；新增组件沿用该方式。
- 从 VitePress 读取语言时使用 `useData()`；共享的中英文站点数据优先通过 `components/useSiteData.ts` 获取。
- 需要在 Markdown 中直接使用的全局组件，必须在 `docs/.vitepress/theme/index.ts` 注册。
- 访问 `window`、`document`、DOM 尺寸或浏览器事件时，考虑 VitePress 的服务端渲染：放在 `onMounted()` 中或使用 `typeof window !== 'undefined'` 防护。
- 保持无障碍属性完整：图片提供有意义的 `alt`，交互控件使用正确的元素和 ARIA 状态，外部新窗口链接使用 `rel="noopener"`。
- 不要引入新的框架或依赖来完成已有 Vue、CSS 或浏览器 API 能简单解决的工作。

### 样式

- 优先复用 `docs/.vitepress/theme/tokens.css` 和现有的 `--vp-*`、`--ic-*` CSS 变量。
- 组件私有样式放在 `<style scoped>`；跨页面规则和 VitePress 覆盖放在主题样式中。
- 修改布局时同时检查桌面端和移动端；现有主要移动端断点为 `768px`。
- 避免无必要地改变全局 VitePress 选择器或现有视觉语言。

### 内容与数据

- JSON 必须保持有效；字段名称和现有对象形状一致，不要为缺失信息编造值。
- `docs/public/` 内资源在页面中以根路径引用，例如文件 `docs/public/images/board/name.jpg` 对应 `/images/board/name.jpg`。
- 修改用户可见的共享文案、链接或导航时，检查中文和英文版本是否都需要更新。
- 新闻 frontmatter 以 `docs/news/_template.md` 为准。至少提供 `title`、`date` 和 `description`；日期使用 `YYYY-MM-DD`。
- 新闻列表由 `docs/news.data.ts` 在构建时加载并按日期倒序排列。中文新闻放在 `docs/news/`，英文新闻放在 `docs/en/news/`，避免依赖 `lang` 字段替代正确目录。
- 往届理事会文件使用 `data/past-boards/board-YYYY.json` 命名。角色值必须与组件中的 `ROLE_ORDER` 保持一致，否则成员不会显示。
- 新增、重命名或删除图片时，检查所有 Markdown、JSON、Vue 和 CSS 引用；注意文件名大小写在 GitHub Pages 上敏感。

## 工作流程与验证

1. 修改前查看 `git status --short --branch`，保留并避开用户已有改动。
2. 只修改任务所需文件；不要顺手重排无关 JSON、Markdown 或 CSS。
3. 对 JSON 和内容路径做针对性检查。
4. 运行 `npm run docs:build`，修复所有构建错误和失效的本地资源引用。
5. 涉及布局、动画、响应式或主题样式时，再用本地预览检查中文、英文、桌面和移动视图。
6. 完成后查看 `git diff --check` 和 `git status --short`，准确汇报实际验证结果。

## Git 规则

- `main` 是部署分支。遵循 `CONTRIBUTING.md`：通过 Pull Request 合并，不直接推送到 `main`。
- 自动化环境可能以 detached HEAD 打开仓库；需要提交时，先从当前提交创建 `codex/<简短任务名>` 分支。
- 不覆盖、还原或提交与当前任务无关的用户改动。
- 不修改 Git 历史，不强推，不执行破坏性清理，除非用户明确要求并确认范围。
- 提交信息使用简洁的祈使式描述，并确保一个提交只包含一个清晰目的。
