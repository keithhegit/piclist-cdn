# MonkeyCode 原文摘录（校对版）

```
作者: Chaitin（长亭）
平台: GitHub + 官网
校对说明: 依据官网与仓库 README，非视频 ASR
抓取参考日: 2026-10-11（Asia/Shanghai）
一手源:
  - https://monkeycode-ai.com/
  - https://github.com/chaitin/MonkeyCode
  - https://raw.githubusercontent.com/chaitin/MonkeyCode/main/README.md
  - https://raw.githubusercontent.com/chaitin/MonkeyCode/main/readme.cn.md
  - https://monkeycode-ai.com/online/install（安装脚本头）
```

---

## 1. 产品定义（README）

### English（README.md）

> MonkeyCode is an open-source **enterprise-grade AI development platform** with built-in development environment management, AI model management, AI task management, and project requirement management. Unlike typical vibe coding tools, MonkeyCode is designed as an AI assistant for professional engineering teams.
>
> - You can deploy MonkeyCode inside your **enterprise network** and share it with your R&D team, so developers can start development tasks quickly while engineering leaders manage AI development workflows centrally.
> - You can also use our **online environment** directly. It includes managed development environments, built-in large language models, and native mobile support, so you can use leading AI agents anywhere.

**中文翻译：**

> MonkeyCode 是一款开源的**企业级 AI 开发平台**，内置开发环境管理、AI 模型管理、AI 任务管理与项目需求管理。与常见的 vibe coding 工具不同，它面向专业工程团队的 AI 助手场景。
>
> - 可部署在**企业内网**并共享给研发团队：开发者快速启动任务，研发负责人集中管理 AI 开发流程。
> - 也可直接使用**在线环境**：托管开发环境、内置大模型、原生移动端支持，随时使用领先的 AI Agent。

### 中文原文（readme.cn.md）

> MonkeyCode 是一款开源的**企业级 AI 开发平台**，内置了开发环境管理、AI 模型管理、AI 任务管理、项目需求管理等能力，区别于其他的 vibe coding 工具，MonkeyCode 是真正面向专业开发团队的 AI 助手。
>
> - 你可以部署在**企业内网**，分享给研发团队使用，让你的研发团队可以方便、快捷地启动开发任务；作为研发负责人的你可以对企业内的 AI 开发流程进行统一管理。
> - 你可以直接使用我们的**在线环境**，内置了开发环境，内置了大模型，支持手机客户端，可以随时随地使用最领先的 AI Agent。

### GitHub 仓库元数据（API）

- `full_name`: `chaitin/MonkeyCode`
- `description`: `AI coding platform for teams`
- `homepage`: `https://monkeycode-ai.net/`
- `license.spdx_id`: `AGPL-3.0`
- `language`（主语言）: `TypeScript`（另有大量 Go / Rust 等）
- `stargazers_count`（抓取时）: `4812`
- 最新 Release tag（抓取时）: `v26072801`（名：MonkeyCode v26072801，published 2026-07-28 UTC）

---

## 2. 功能列表（README Features）

### English

> You do not need to assemble tools, set up environments, or jump between workflows. Give MonkeyCode a requirement and it carries the work from development to validation, turning AI coding into a sustainable workflow.
>
> - **Free to start**: No client download and no local environment setup. Open the browser, create an account, and start your first AI development task in seconds.
> - **Cloud development environments**: No dependency on a local development machine. Every task runs behind a real server-side environment, with build, test, and preview workflows completed in the cloud.
> - **Broad model support**: GLM, Kimi, MiniMax, Qwen, DeepSeek, and other mainstream models are integrated. You can switch by task type or select a model manually.
> - **Native mobile support**: Deep iOS and Android support keeps PC and mobile data in sync, so agents can continue running tasks while you are away from your desk.
> - **Fully open source**: The core code is public on GitHub. Anyone can audit, fork, and extend it while keeping control over technical choices and security policies.
> - **Private offline deployment**: Enterprises and teams with strict data privacy requirements can deploy MonkeyCode inside their own networks and keep data local.

**中文翻译：**

> 你不必自己拼工具、搭环境、来回切换流程。把需求交给 MonkeyCode，它会从开发到验证一路承接，把 AI 编程变成可持续工作流。
>
> - **免费起步**：无需下载客户端、无需本机环境；浏览器打开、注册账号，数秒即可开始第一个 AI 开发任务。
> - **云端开发环境**：不依赖本地开发机；每个任务背后是真实服务端环境，构建、测试、预览在云上完成。
> - **广泛模型支持**：已接入 GLM、Kimi、MiniMax、Qwen、DeepSeek 等主流模型；可按任务类型切换或手动指定。
> - **原生移动支持**：深度适配 iOS / Android，PC 与手机数据同步；离开工位时 Agent 仍可继续跑任务。
> - **完全开源**：核心代码公开于 GitHub；可审计、fork、扩展，技术选型与安全策略自主掌控。
> - **私有化离线部署**：对数据隐私要求高的企业/团队可部署在自有网络内，数据留在本地。

### 中文原文（readme.cn.md）

> - **免费即用**：无需下载客户端，也不用折腾环境。浏览器打开、注册账号，几秒钟就能开始执行第一个 AI 开发任务。
> - **云端开发环境**：不依赖本地开发机。每个任务背后都有一台真实服务器提供运行环境，编译、测试、预览都在云上完成。
> - **全量主流模型**：GLM、Kimi、MiniMax、Qwen、DeepSeek 等都已接入，支持按任务类型切换，也能手动指定。
> - **移动端原生支持**：深度适配 iOS / Android，PC 和手机数据实时同步。通勤路上也能把任务交给 Agent 继续跑。
> - **完全开源**：核心代码全部公开在 GitHub。任何人都能审计、fork、二次开发，技术选型和安全策略自己掌控。
> - **私有化离线部署**：对数据隐私要求高的企业和团队，可以把 MonkeyCode 独立部署到自己的内网中，数据不出本地。

---

## 3. 官网补充：用例与桌面 / 私有化要点

### 官网定位句（English UI 抓取）

> The all-in-one AI platform for work & code
>
> Start working right in the browser, with research, writing, development, and task execution flowing from the same workspace. When work needs local code, files, or runtime environments, hand it to MonkeyWork for continuous execution, keep up from mobile, and deploy privately inside the enterprise when needed.

**中文翻译：**

> 面向工作与代码的一体式 AI 平台。
>
> 直接在浏览器开工：调研、写作、开发与任务执行同一工作区流转。需要本地代码、文件或运行环境时交给 MonkeyWork 持续执行，可用移动端跟进，也可在企业内私有化部署。

### 用例「Security review」（官网 CASE / 03）

> Run a health check before launch. AI scans common vulnerabilities, hardcoded secrets, and dependency risks, then outputs a fixable list.
>
> OWASP Top 10 · Dependency CVEs · SAST rules

**中文翻译：**

> 上线前做健康检查。AI 扫描常见漏洞、硬编码密钥与依赖风险，并输出可修复清单。标签：OWASP Top 10、依赖 CVE、SAST 规则。

> 校对注：此项为官网**用例**，不是 README 六大 Features 的并列主标题。

### 私有化部署（官网）

> When teams need AI development capabilities inside the corporate intranet, MonkeyCode can be deployed independently to manage developers, environments, and model configuration in one place.
>
> - Deploy inside the enterprise intranet so repositories, task records, and engineering data stay within your network boundary.
> - Centrally manage team members, development environments, AI models, and task workflows for governance and auditability.
> - Connect existing enterprise models, Git platforms, and environment hosts to fit internal engineering infrastructure.
> - Install online or offline for teams with network isolation, compliance requirements, or local compute resources.

**中文翻译：**

> 当团队需要把 AI 开发能力放进企业内网时，可独立部署 MonkeyCode，统一管理开发者、环境与模型配置。
>
> - 部署在企业内网，仓库、任务记录与工程数据留在网络边界内。
> - 集中管理成员、开发环境、AI 模型与任务流程，便于治理与审计。
> - 对接已有企业模型、Git 平台与环境宿主机。
> - 支持在线或离线安装，适配网络隔离、合规或本地算力场景。

### 定价与版本边界（官网，摘录要点）

- Individual：Basic ¥0（Free forever）；Pro ¥99/月；Ultra ¥499/月（抓取时页面文案）。
- Free 示例额度：1 concurrent task；Cloud 1C/4G；Daily quota 10M tokens/day；Basic models。
- OSS：Full source code, free to clone / fork, community support → GitHub。
- ENT：Private offline deployment, enterprise-grade security and auditing, commercial support → Contact us。
- FAQ 片段：*The personal Free tier is available long term. We mainly make money through Pro subscriptions and commercial support for enterprise self-hosting.*  
  **译：**个人 Free 档长期可用；主要通过 Pro 订阅与企业自托管商业支持盈利。

---

## 4. 安装 / 部署要点

### README 推荐配置与联网安装

**English：**

> Recommended configuration:
>
> - MonkeyCode console: at least `2C / 4 GB / 40 GB`
> - Development environment host: at least `8C / 16 GB / 100 GB`
>
> Online installation:
>
> ```bash
> bash -c "$(curl -fsSL 'https://monkeycode-ai.com/online/install')"
> ```
>
> For more deployment methods, configuration details, and operations guidance, see the deployment documentation:  
> https://monkeycode.docs.baizhi.cloud/node/019eb0f3-9424-7c93-9489-4e584f989527

**中文原文（readme.cn.md）：**

> 配置建议：
>
> - MonkeyCode 控制台：最低 `2C / 4 GB / 40 GB`
> - 开发环境宿主机：最低建议 `8C / 16 GB / 100 GB`
>
> 联网安装：
>
> ```bash
> bash -c "$(curl -fsSL 'https://monkeycode-ai.com/online/install')"
> ```

### 在线安装脚本头（https://monkeycode-ai.com/online/install，摘录可核对事实）

```sh
#!/bin/sh
set -eu

VERSION="v261009"
# ... 下载 amd64/arm64 在线包 ...

if [ "$(id -u)" -ne 0 ]; then
  echo "installer must run as root"
  exit 1
fi

OS="$(uname -s)"
if [ "$OS" != "Linux" ]; then
  echo "unsupported system: $OS"
  exit 1
fi
# 支持 x86_64|amd64 与 aarch64|arm64|armv8l
echo "Installing MonkeyCodePro online package $VERSION"
```

**中文说明：**脚本要求 root、仅 Linux、架构 amd64/arm64；抓取时包版本字符串为 `v261009`（可能与 GitHub Release tag 不同）。

### 仓库内部署相关线索（非完整运维手册）

- `backend/docker-compose.yml`：`name: monkeycode-ai`，含 `db`（Postgres）、`redis`、`clickhouse`、`rustfs` 等服务。
- `backend/templates/install.sh.tmpl` / `install_offline.sh.tmpl`：Runner/安装引导；x86_64 检查 AVX；需 root。
- 官方完整步骤仍指向 docs.baizhi.cloud 部署节点（HTTP 抓取正文有限，**细步骤待在浏览器中核实**）。

---

## 5. 对比表（README，原样结构）

| 对比维度 | MonkeyCode | Cursor | Claude Code | Codex |
|---|:---:|:---:|:---:|:---:|
| 在线使用 | 🟢 | 🟢 | 🟢 | 🟢 |
| 本地 IDE | 🔴 | 🟢 | 🟢 | 🟢 |
| 本地 CLI | 🔴 | 🟢 | 🟢 | 🟢 |
| 需求与 SPEC 管理 | 🟢 | 🔴 | 🔴 | 🔴 |
| 云端开发环境 | 🟢 | 🟡 | 🟡 | 🟡 |
| 代码补全 | 🔴 | 🟢 | 🔴 | 🔴 |
| PR / MR 自动代码审查 | 🟢 | 🟡 | 🟡 | 🟡 |
| 团队协作 | 🟢 | 🔴 | 🔴 | 🔴 |
| 适配国产大模型 | 🟢 | 🔴 | 🔴 | 🔴 |
| 私有化部署 | 🟢 | 🔴 | 🔴 | 🔴 |
| 开源 | 🟢 | 🔴 | 🔴 | 🔴 |

官网英文对比表附注：

> Data is based on publicly available product capabilities. Issues and PRs are welcome if something is missing.

**译：**数据基于公开产品能力；若有遗漏欢迎 Issue / PR。

---

## 6. 许可证与作者

### License（README）

> MonkeyCode is open source under the [GNU Affero General Public License v3.0](./LICENSE).
>
> （中文 README）MonkeyCode 使用 [GNU Affero General Public License v3.0](./LICENSE) 开源。

- SPDX：`AGPL-3.0`
- LICENSE 文件抬头：`GNU AFFERO GENERAL PUBLIC LICENSE` / `Version 3, 19 November 2007`
- Badge：`license-AGPL--3.0`

### 作者 / 组织

- GitHub Organization：`chaitin`（长亭）
- 仓库：`chaitin/MonkeyCode`
- 企业咨询入口（README）：https://baizhi.cloud/consult
- 社区：微信 / 飞书 / 钉钉群二维码（见仓库 README 图片）、Discord https://discord.gg/2pPmuyr4pP、GitHub Issues

---

## 7. 社区与支持链接（README 列表）

- Documentation: https://monkeycode.docs.baizhi.cloud/
- Online service: https://monkeycode-ai.net/ （中文 README 主推 https://monkeycode-ai.com/）
- Enterprise consultation: https://baizhi.cloud/consult
- Discord: https://discord.gg/2pPmuyr4pP
- GitHub Issues: https://github.com/chaitin/MonkeyCode/issues

---

## 8. 校对备注

1. H1 / 定位以「企业级 AI 开发平台」为准；「源码安全助手」未见于当前 README 主定义，仅官网有安全审查用例。
2. 官网域名同时出现 `monkeycode-ai.com` 与 `monkeycode-ai.net`，中英文 README 写法不完全一致，入口均可作为官方路径记录。
3. 文档站为 SPA，本次 WebFetch 未能完整抽出部署正文；安装命令与资源配置以 README + install 脚本为准。
4. 未编造未在源中出现的扫描引擎名、准确 CVE 覆盖率、SLA 或未公示的 Docker 一键 compose 用户命令。
