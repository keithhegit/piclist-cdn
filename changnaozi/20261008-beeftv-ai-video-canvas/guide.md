# 本地优先 AI 视频创作画布 BeefTV - GitHub

> 来源：[glanderness/BeefTV](https://github.com/glanderness/BeefTV) · MIT · 897★ / 183 forks · 最新 v1.7.12（2026-10-08 00:07 UTC+8）· 抓取于 2026-10-08 12:30（UTC+8）

## 一句话定位

**BeefTV 是一个开源的桌面版 AI 视频创作工作台。** 你在一张无限画布上用节点和连线串起提示词、参考图、图片/视频/音频生成和剪辑，模型用你自己的 API Key（约 85 种协议适配）。数据默认留在本机，不需要注册登录。它和 LibTV / Lovart / 即梦画布类工具同一赛道，并不是 IPTV 或影视聚合播放器。

## 上手顺序

1. **直接用（推荐）**：到 [Releases](https://github.com/glanderness/BeefTV/releases/latest) 下载安装包。Mac 的 Apple 芯片选 `darwin-arm64`，Intel 选 `darwin-amd64`；Windows 选 `windows-amd64.zip`。
2. **Mac 首次打开**：安装包还没做 Apple 签名和公证，会提示「无法验证是否包含恶意软件」。到「系统设置 → 隐私与安全性」里点「仍要打开」。
3. **配模型**：打开「模型配置」，二选一：
   - 用内置 **BeefAPI**：点「连接 BeefAPI」，在浏览器里授权（这是作者方的付费聚合渠道）。
   - 自己添加 OpenAI / Gemini / 火山方舟 / 兼容服务：填 Base URL 和 API Key，读取模型目录后勾选需要的模型。
4. **先做一次模型测试**：测试会产生真实费用，等任务出结果再正式使用。
5. **开画布**：新建项目，选「自由空白画布」或「短剧流水线」。中央的加号可以加文本、图片、视频、音频、分镜或工作流节点，节点之间连线引用素材。
6. **出片**：在项目详情里进入「剪辑成片」时间线，编排分镜视频后导出。字幕转写要先配 whisper.cpp，导出需要 ffmpeg。

## 能力表

| 模块 | 能做什么 |
|---|---|
| 自由画布 | 节点和连线组织素材与流程，支持框选、对齐、自动整理、版本记录、手动保存或强制覆盖 |
| 生成 | 文 / 图 / 视频 / 音频生成；批量创作表；提示词放大编辑；「智能引用」（用 `图1`、`image1` 这类写法引用已连接素材） |
| 图片加工 | 裁切、标注、局部重绘、4 到 25 宫格切分、3D 多角度视角 |
| 提示词优化器 | 五种模式：扩展想法、精修已有提示词、强化风格、按目标模型适配、结合参考素材。结构化输出正向词和规避项 |
| 短剧 / 分镜 | 章节提取角色、场景、道具；分镜规划、首帧、视频；角色三视图；短剧大纲 |
| 剪辑成片 | 浏览器内时间线：拆分、修剪，200 步撤销；语音转字幕；ffmpeg 导出；用自然语言描述剪辑意图（超过 3 条命令时先预览差异） |
| 模型渠道 | 约 85 个协议插件：OpenAI、Gemini/Veo、Grok、Seedance/Seedream/即梦、可灵、Vidu、海螺、万相、混元、Runway、Luma、ComfyUI、Ollama、OpenRouter、NewAPI 等 |
| 素材 | 项目库、个人资产库、Eagle 外部素材库插件、异步任务中心、诊断包导出（已脱敏） |
| 部署形态 | 桌面版（Wails，SQLite，单用户）；另有 Docker / 服务端模式（Postgres + Redis），带注册、积分、支付插件、后台运营 |

## 部署与构建命令

```bash
# 桌面版（macOS），需要 Go 1.25、Bun 和 Wails 系统依赖
git clone https://github.com/glanderness/BeefTV.git
cd BeefTV
BEEFTV_GO_DIR=/path/to/go ./scripts/build-beeftv-release.sh
# 产物：backend/cmd/desktop/build/bin/BeefTV.app
```

```powershell
# Windows amd64 只能在 Windows 本机构建（PATH 里要有 Go、Bun 和 GCC）
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\build-beeftv-windows-release.ps1
# 产物：backend\cmd\desktop\build\bin\BeefTV.exe，插件放在同级 plugin-packages\
```

```bash
# 本地 Docker 版（SQLite，web 端口 3000，默认关闭注册）
docker compose up -d --build
# 公网服务端：docker-compose.deploy.yml（Postgres 17 + Redis 7 + ghcr.io/glanderness/beeftv-backend 镜像）
# 上线要求见 SECURITY.md：必须 HTTPS；CANVAS_CORS_ORIGINS 写明确的前端域名；先注册首个管理员再暴露公网；.settings-key 只给服务账号读权限
```

## 坑与风险

- **项目很新、迭代很猛**：仓库 2026-09-24 才创建，10-07 一天连发 4 个版本，文档和实现不同步。比如功能清单写着「内置 Agent 已退场」，同时又有 PR 在重新加 Agent、MCP 和 CLI。生产环境要先锁定版本。
- **Mac 安装包未签名、未公证**：只从官方 Releases 下载。应用内更新器会校验签名和哈希，但这不等于 Apple 公证。
- **内置 BeefAPI 是商业渠道**：代码里有 `beefapi.com`、`enterprise.beefapi.com` 和更新服务器 `updates.beefapi.com`。如果不想走它，自己配渠道就行。另外桌面版有在线更新检查。
- **花钱的是模型 API**：视频模型（Seedance、Veo、可灵等）按条计费，测试和重试都会扣费。建议在供应商后台设好预算和告警。
- **「本地优先」只针对项目数据**：生成时素材会提交给你配置的外部模型服务商。
- **许可证不是全 MIT**：FFmpeg.wasm core 是 GPL-2.0-or-later，二次分发打包了它的版本要满足 GPL 源码义务。代码派生自 basketikun/infinite-canvas，上游已改为 MIT，署名要保留。
- **服务端模式的边界**：功能清单里的支付、积分、后台运营属于服务端或 SaaS 形态，本地桌面版不含登录、计费和云同步。别把两者混在一起评估。
- **版权与内容合规**：工具本身不聚合影视资源，没有盗版问题。生成内容的肖像权和版权（比如「Seedance 真人」档）由使用者负责。
- **Windows 旧版升级**：v1.6.20 到 v1.6.22 的更新器识别不了新目录结构，需要手动解压完整包，保留原数据目录。

## 适合谁

- 想要一套**可自托管、可自带 Key** 的 AI 视频或短剧创作画布，作为 LibTV、即梦画布、Lovart 这类 SaaS 替代品的人
- 想研究「画布 + 节点 + 多模型协议适配 + 时间线剪辑」完整实现的开发者（React + Go + Wails，代码量大，测试也多）
- 想基于它二开、搭自己的 AI 创作 SaaS 的团队：服务端模式自带积分、支付插件、品牌外观和后台
- 不太适合：完全不想碰 API Key、只想用现成会员的纯小白；或者对 GPL 组件和二次分发很敏感、又不打算处理合规的商用打包方

## 链接

- 仓库：https://github.com/glanderness/BeefTV
- 下载：https://github.com/glanderness/BeefTV/releases/latest
- 官网：https://beeftv.app/
- 功能清单：https://github.com/glanderness/BeefTV/blob/main/docs/content/docs/overview/features.mdx
- 快速开始：https://github.com/glanderness/BeefTV/blob/main/QUICKSTART.md
- 上游：https://github.com/basketikun/infinite-canvas

## 章节导航（transcript.md）

1. 仓库元数据表
2. README.md 原文
3. README 英文部分中译
4. QUICKSTART.md 原文
5. NOTICE 原文与中文全译
