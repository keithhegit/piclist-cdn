# 本地优先 AI 视频创作画布 BeefTV - GitHub

> **元信息**
> - 仓库：[glanderness/BeefTV](https://github.com/glanderness/BeefTV)（官网 https://beeftv.app/ ；X @beefnoode）
> - 仓库自述（About）："Local-first, lightweight, AI-native video workspace."
> - 抓取时间：2026-10-08 12:30（UTC+8）；main 分支 HEAD `ef65732`（2026-10-07 23:47 UTC+8，`fix(settings): 统一 Seedance 展示并发布 v1.7.12 (#93)`）
> - 校对说明：一手源，直接 clone 仓库读取 README.md / QUICKSTART.md / NOTICE / LICENSE / SECURITY.md / THIRD_PARTY_NOTICES.md / CHANGELOG.md / docker-compose*.yml，元数据来自 GitHub API。README 正文本身以中文为主，英文部分（标语、表头、"Why BeefTV"、"Open by design"）在下方逐条中译；NOTICE 为英文，附全译。
> - 名称提醒：虽然叫 "TV"，**它不是 IPTV / 影视聚合 / 盗链播放器**，而是 AI 生成视频的创作工作台（画布 + 模型渠道）。

## 仓库元数据

| 项目 | 值 |
|---|---|
| 所有者 | glanderness（个人账号）；LICENSE 署名 @beefnoode and BeefTV contributors、basketikun、ddcat |
| 创建 | 2026-09-24 13:20（UTC+8），至今约 2 周 |
| 最近 push | 2026-10-08 12:26（UTC+8） |
| Stars / Forks / Watchers | 897 / 183 / 12（2026-10-08 抓取） |
| Open issues + PRs | 23（多数是 PR：MCP/CLI、Agent、本地 TTS、ComfyUI、ChatGPT 订阅 OAuth 等） |
| 主要语言 | TypeScript（前端）+ Go（后端） |
| 许可证 | MIT（附 NOTICE；FFmpeg.wasm core 组件为 GPL-2.0-or-later） |
| 最新版本 | v1.7.12，2026-10-08 00:07（UTC+8）发布；提供 macOS arm64/amd64、Windows amd64 zip |
| 发版节奏 | 极快：10-07 一天发了 v1.7.9→v1.7.12 四个版本 |
| 提交 | main 共 170 次提交（9-24 起），活跃作者 enderzcx 65、Sunny 40、Lucas 4、Beefnoodle 4 |
| 上游 | 派生自 [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) v0.5.0（commit 568f0f1），上游已改为 MIT |
| 技术栈 | React 19 + Vite + Ant Design 6 + Excalidraw + Leafer-UI + three.js + FFmpeg.wasm + MediaPipe；Go 1.25 + Gin + GORM + SQLite（服务端模式可用 PostgreSQL + Redis）；桌面壳 Wails v2 |
| 模型协议插件 | `plugin-packages/` 下约 85 个适配：OpenAI（Chat/Responses/Images/Videos/Audio）、Gemini/Veo/Imagen、Anthropic、xAI Grok、火山方舟 Seedance/Seedream/即梦、可灵、Vidu、海螺、通义万相、混元、智谱、Runway、Luma、Pika、Flux、Stability、Replicate、fal、ComfyUI、Ollama、vLLM、OpenRouter、NewAPI 等 |

---

## 一、README.md 原文

<p align="center">
  <img src="assets/readme/beeftv-wordmark.svg" width="640" alt="BeefTV — High-performance, lightweight, AI-native video workspace">
</p>

<p align="center"><strong>High-performance · Lightweight · AI Native</strong></p>

<p align="center">
  面向 AI 时代的视频创作工作台。<br>
  在一个自由画布中连接创意、模型与素材。
</p>

<p align="center">
  <a href="https://github.com/glanderness/BeefTV/stargazers"><img src="https://img.shields.io/github/stars/glanderness/BeefTV?style=flat-square&amp;logo=github&amp;label=Stars&amp;labelColor=303030&amp;color=E86C36" alt="BeefTV GitHub Stars"></a>
  <a href="https://github.com/glanderness/BeefTV/releases/latest"><img src="https://img.shields.io/github/v/release/glanderness/BeefTV?style=flat-square&amp;label=Release&amp;labelColor=303030&amp;color=525252" alt="BeefTV 最新版本"></a>
  <a href="QUICKSTART.md#下载与首次打开"><img src="https://img.shields.io/badge/Desktop-macOS%20%7C%20Windows-525252?style=flat-square&amp;labelColor=303030" alt="桌面版支持 macOS 和 Windows"></a>
  <a href="QUICKSTART.md"><img src="https://img.shields.io/badge/Workspace-Local--first-525252?style=flat-square&amp;labelColor=303030" alt="本地优先工作区"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-525252?style=flat-square&amp;labelColor=303030" alt="MIT 许可证"></a>
</p>

<p align="center">
  <a href="https://beeftv.app/"><img src="assets/readme/button-website.svg" width="180" alt="访问 BeefTV 官网"></a>
  <a href="https://github.com/glanderness/BeefTV/releases/latest"><img src="assets/readme/button-download.svg" width="175" alt="下载 BeefTV 桌面版"></a>
  <a href="https://beeftv.app/assets/beeftv-wecom-qr.png"><img src="assets/readme/button-community.svg" width="185" alt="扫码加入 BeefTV 社群"></a>
  <a href="https://x.com/beefnoode"><img src="assets/readme/button-x.svg" width="180" alt="在 X 关注 @beefnoode"></a>
</p>

<p align="center">
  <a href="#产品演示">产品演示</a> ·
  <a href="docs/content/docs/overview/features.mdx">功能清单</a> ·
  <a href="QUICKSTART.md">开始使用</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

#### 产品演示

https://github.com/user-attachments/assets/94fe6a39-6933-44b3-a9a9-dbc28b2d284c

[下载产品演示视频](https://github.com/glanderness/BeefTV/releases/download/v1.5.5/beeftv-demo.mp4)

#### Why BeefTV

| High Performance | Lightweight | AI Native |
| --- | --- | --- |
| 面向复杂创作画布优化。视口渲染、节点加载、媒体预览与生成任务彼此解耦，让项目增长时仍能保持顺畅操作。 | 以低资源占用和低使用门槛为目标。一个桌面工作区即可开始创作，能力按需加载，追求轻量化 | AI 不是附加按钮，而是工作台中不可或缺的一部分。让Agent真正参与并且主导你的AIGC创作流程。 |

#### 一个画布，完整创作链路

- **生成**：从提示词或参考素材生成文字、图片、视频与音频。
- **组织**：用节点和连线建立素材关系、创作上下文与生成流程。
- **加工**：继续裁切、标注、局部重绘、拆分、引用和组合结果。
- **迭代**：保留过程、复用素材，让一次生成变成可持续演进的工作流。

BeefTV 同时提供项目库、个人资产库、异步任务、模型渠道与创作工具。完整范围见[功能清单](docs/content/docs/overview/features.mdx)。

#### 工作方式

```text
想法 / 参考素材
       ↓
AI Native 自由画布
       ↓
模型 + 创作工具
       ↓
文字 / 图片 / 视频 / 音频 / 分镜
       ↓
可编辑、可复用、可继续生成的工作流
```

#### Open by design

- 可以自由配置文本、图片、视频与音频模型渠道，不绑定单一 Provider。
- 项目、画布、素材与任务由统一工作区管理，数据可以本地保存和迁移。
- 桌面端基于 React、Go 与 Wails，模型协议和工作台能力可继续自定义或者扩展。

#### 开始使用

下载桌面版及 Mac 首次打开说明见 [快速开始](QUICKSTART.md#下载与首次打开)。

```bash
git clone https://github.com/glanderness/BeefTV.git
cd BeefTV
./scripts/build-beeftv-release.sh
```

详细环境要求、Windows 构建与本地开发方式见 [`QUICKSTART.md`](QUICKSTART.md) 和[桌面发布文档](docs/desktop-release.md)。首次启动后，添加自己的模型渠道即可开始创作。

#### 贡献与许可

欢迎提交 Issue 和 Pull Request。开发流程与测试要求见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

项目按照 [`LICENSE`](LICENSE) 发布；上游来源、保留声明与第三方归属见 [`NOTICE`](NOTICE)。

#### ⭐ Star History

<a href="https://www.star-history.com/?repos=glanderness%2FBeefTV&amp;type=date&amp;legend=bottom-right">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=glanderness/BeefTV&amp;type=date&amp;theme=dark&amp;legend=bottom-right" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=glanderness/BeefTV&amp;type=date&amp;legend=bottom-right" />
    <img alt="BeefTV GitHub Star History" src="https://api.star-history.com/chart?repos=glanderness/BeefTV&amp;type=date&amp;legend=bottom-right" />
  </picture>
</a>
---

## 二、README 英文部分中译（中文段落原样，见上）

- 标题图 alt："BeefTV — High-performance, lightweight, AI-native video workspace" → BeefTV —— 高性能、轻量、AI 原生的视频工作台
- 标语 "High-performance · Lightweight · AI Native" → 高性能 · 轻量 · AI 原生
- 徽章："Stars"→星标；"Release"→最新版本；"Desktop - macOS | Windows"→桌面版支持 macOS 与 Windows；"Workspace - Local-first"→本地优先工作区；"License - MIT"→MIT 许可证
- "## Why BeefTV" → 为什么选 BeefTV。表头 "High Performance | Lightweight | AI Native" → 高性能 | 轻量 | AI 原生（表格正文本身为中文）
- "## Open by design" → 天生开放（下列三条本身为中文）
- "## ⭐ Star History" → 星标增长曲线

---

## 三、QUICKSTART.md 原文（中文，无需翻译）

### BeefTV 本地桌面版快速开始

BeefTV 桌面版是无需登录的本地优先工作区。项目、画布、素材、任务记录和模型配置默认保存在本机；只有执行生成时，才会按你配置的渠道请求外部模型服务。

#### 下载与首次打开

从 [官方发布页](https://github.com/glanderness/BeefTV/releases/latest) 下载对应系统的安装包。Mac 的 Apple 芯片选择 `darwin-arm64`，Intel 芯片选择 `darwin-amd64`；解压后将 `BeefTV.app` 放入「应用程序」。

目前 Mac 版本尚未完成 Apple 开发者签名和公证。首次打开时，如果提示「Apple 无法验证 BeefTV.app 是否包含恶意软件」，请先确认安装包来自官方发布页，再打开「系统设置 → 隐私与安全性」，找到 BeefTV 并点击「仍要打开」，按系统提示确认。受组织管理的 Mac 可能需要联系管理员。

这是 macOS 对未公证应用的检查，换一个下载地址不会消除它。无需关闭整个系统的安全检查。具体操作见 [Apple 的打开应用说明](https://support.apple.com/zh-cn/102445)。

已经能正常打开的旧版本，可在应用内检查更新；更新器会校验更新清单签名和安装包哈希。这些校验不等于 Apple 公证。

#### 构建桌面版

环境要求：Go 1.25、Bun，以及 Wails 所需的系统组件。

在仓库根目录执行：

```bash
BEEFTV_GO_DIR=/path/to/go ./scripts/build-beeftv-release.sh
```

macOS 应用输出到 `backend/cmd/desktop/build/bin/BeefTV.app`。

Windows amd64 必须在 Windows 本机构建（需要 PATH 中的 Go、Bun，以及编译 go-sqlite3 的 GCC）：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\build-beeftv-windows-release.ps1
```

输出为 `backend\cmd\desktop\build\bin\BeefTV.exe`，官方插件在旁边的 `plugin-packages\`。前提与数据目录见 `docs/desktop-release.md`。

首次打开后直接进入本地工作区，不需要注册或登录。

#### 配置模型

打开“模型配置”。内置 BeefAPI 使用「连接 BeefAPI」，在系统浏览器中完成授权后即可拉取模型。其他渠道仍填写 Base URL 和密钥。密钥保存在本地工作区，不会写入画布、素材或任务列表。

模型请求可能访问外部供应商，但 BeefTV 不会把项目数据同步到 SaaS 存储。素材会先写入本地资源目录，再作为本地资源引用提交给模型渠道。

#### 本地开发与验证

需要同时调试前后端时，可参考 `scripts/beeftv-shared-dev.sh`。验证本地发行边界：

```bash
BEEFTV_GO_DIR=/path/to/go ./scripts/verify-beeftv-local-release.sh
```

#### 数据位置与备份

桌面运行时会在本地工作区保存 SQLite 数据库、资源文件、模型配置和迁移备份。升级迁移前会自动创建数据库备份；如需迁移或恢复，请先退出 BeefTV 并完整复制工作区数据目录。

登录、云存储、团队同步和计费不属于 BeefTV 本地版。以本地能力契约、精简 schema 和发行门禁为准，详见 `docs/local-first-architecture.md`。

---

## 四、NOTICE 原文（英文）

```text
BeefTV
Copyright (C) 2026 BeefTV contributors

BeefTV is distributed under the MIT License. The complete license text is
provided in LICENSE.

Project scope
-------------

BeefTV is a local-first, single-user desktop workspace for AI-assisted video
creation. The desktop application uses a React user interface embedded by
Wails and a Go backend that listens on loopback. Projects, canvas state,
generated assets, model-channel settings, and durable task state are stored in
the user's local workspace. Requests leave the device only when a user invokes
an externally configured model provider or another explicitly networked tool.

Upstream source
---------------

This repository contains code derived from:

  Infinite Canvas
  https://github.com/basketikun/infinite-canvas
  Base version: v0.5.0
  Base commit: 568f0f1838df8de31fe885a4e130e2f346dd14ab

The upstream project is maintained under the basketikun account. Upstream
authors and contributors retain copyright in their respective contributions.
The upstream project was relicensed to MIT in commit
890ba95858bbb13496d23978003716656109abb2. Its copyright and permission notice
are preserved in LICENSE.

BeefTV changes
--------------

BeefTV adds and maintains the local Go application layer, SQLite and local
asset persistence, durable generation tasks, provider and protocol adapters,
the Wails desktop shell, media workflows, timeline tools, the local Agent, and
substantial canvas and workspace UI changes.

Third-party software and assets
-------------------------------

Dependencies and bundled assets remain subject to the licenses and notices of
their respective authors. Important runtime components include Wails,
FFmpeg.wasm, Excalidraw, MediaPipe, React, Gin, GORM, and SQLite bindings.
Provider and product names are used only to identify compatible protocols or
services and do not imply affiliation or endorsement.

See THIRD_PARTY_NOTICES.md for the audited dependency and bundled-asset
inventory distributed with the public source snapshot.
```

### NOTICE 中文全译

BeefTV
版权所有 (C) 2026 BeefTV 贡献者

BeefTV 以 MIT 许可证发布，完整许可文本见 LICENSE。

**项目范围**

BeefTV 是一个本地优先、单用户的 AI 辅助视频创作桌面工作区。桌面应用使用由 Wails 内嵌的 React 用户界面，以及只监听回环地址（loopback）的 Go 后端。项目、画布状态、生成的素材、模型渠道设置和持久化任务状态都存放在用户本地工作区。只有当用户调用外部配置的模型服务商或其他明确联网的工具时，请求才会离开本机。

**上游来源**

本仓库包含派生自以下项目的代码：

  Infinite Canvas
  https://github.com/basketikun/infinite-canvas
  基线版本：v0.5.0
  基线提交：568f0f1838df8de31fe885a4e130e2f346dd14ab

上游项目由 basketikun 账号维护。上游作者与贡献者对各自贡献保留版权。上游项目在提交 890ba95858bbb13496d23978003716656109abb2 中改为 MIT 许可，其版权与许可声明保留在 LICENSE 中。

**BeefTV 的改动**

BeefTV 新增并维护：本地 Go 应用层、SQLite 与本地素材持久化、持久化生成任务、服务商与协议适配器、Wails 桌面壳、媒体工作流、时间线工具、本地 Agent，以及大量画布与工作区 UI 改动。

**第三方软件与素材**

依赖与随附素材仍受各自作者的许可与声明约束。重要运行时组件包括 Wails、FFmpeg.wasm、Excalidraw、MediaPipe、React、Gin、GORM 和 SQLite 绑定。服务商与产品名称仅用于标识兼容的协议或服务，不代表隶属或背书关系。

经审计的依赖与随附素材清单见 THIRD_PARTY_NOTICES.md（随公开源码快照分发）。
