# MonkeyCode 企业级 AI 开发平台 - GitHub/官网

> 一手来源：[官网 monkeycode-ai.com](https://monkeycode-ai.com/) · [GitHub chaitin/MonkeyCode](https://github.com/chaitin/MonkeyCode) · [中文 README](https://github.com/chaitin/MonkeyCode/blob/main/readme.cn.md)  
> 校对说明：依据官网与仓库 README/安装脚本摘录整理，非视频 ASR。作者组织：Chaitin（长亭）。  
> 说明：部分旧口径或第三方转述会写成「源码安全助手」；**当前官网与 README 正式定位为「企业级 AI 开发平台」**。安全审查仅为官网用例之一，勿当作产品主定义。

## 一句话定位

开源、可私有化部署的**企业级 AI 开发平台**：内置开发环境管理、AI 模型管理、AI 任务管理与项目需求管理，面向专业研发团队做统一治理；也可直接用在线环境 + 云端运行时 + 移动端续跑。

## 章节导航

1. [上手顺序](#上手顺序)
2. [能力表](#能力表)
3. [可复制命令 / 金句](#可复制命令--金句)
4. [坑与限制](#坑与限制)
5. [适合谁](#适合谁)
6. [源链接](#源链接)

## 上手顺序

按文档公开路径，由浅入深：

1. **在线试用（最快）**  
   - 中文 README：打开 [https://monkeycode-ai.com/](https://monkeycode-ai.com/)  
   - 英文 README：也写了 [https://monkeycode-ai.net/](https://monkeycode-ai.net/)  
   - 浏览器注册账号即可开始 AI 开发任务（无需本机装环境）。

2. **阅读开源仓库**  
   ```bash
   git clone https://github.com/chaitin/MonkeyCode.git
   cd MonkeyCode
   ```
   - 看 `README.md` / `readme.cn.md`、`LICENSE`（AGPL-3.0）。

3. **自托管 / 私有化（文档有）**  
   - 配置建议（README）：  
     - MonkeyCode 控制台：最低 `2C / 4 GB / 40 GB`  
     - 开发环境宿主机：最低建议 `8C / 16 GB / 100 GB`  
   - 联网安装（README 原样）：  
     ```bash
     bash -c "$(curl -fsSL 'https://monkeycode-ai.com/online/install')"
     ```  
   - 安装脚本侧可见约束（脚本本身，非 README 全文）：需 **root**、仅 **Linux**、架构 **amd64 / arm64**；在线安装包版本字符串曾见 `v261009`（与 GitHub Releases 最新 tag 可能不一致，见「坑与限制」）。  
   - 更多部署方式 / 运维：官方指向 [部署文档](https://monkeycode.docs.baizhi.cloud/node/019eb0f3-9424-7c93-9489-4e584f989527)。  
   - 官网宣称支持**在线或离线安装**；仓库内存在 `install_offline.sh.tmpl`、以及基于 Docker Compose 的后端编排（Postgres / Redis / ClickHouse 等）——细节以部署文档为准，**勿仅靠 clone 后手搓服务当官方推荐路径**。

4. **桌面 / 移动（可选）**  
   - 官网提供 Windows / macOS / Linux 桌面端，以及 Android APK / iOS App Store。  
   - 桌面侧强调本地文件夹授权、接云端任务、自定义模型与 MCP、浏览器扩展辅助等（以官网功能描述为准）。

## 能力表

| 能力 | 来源表述 | 备注 |
|---|---|---|
| 企业级 AI 开发平台 | README：开发环境 / 模型 / 任务 / 需求管理 | 核心定位 |
| 免费即用 / 浏览器开箱 | 官网 & README | 个人 Free 档官网有配额说明 |
| 云端开发环境 | 编译、测试、预览在云上完成 | 对比表称相对 Cursor 等为优势项 |
| 主流模型接入 | GLM、Kimi、MiniMax、Qwen、DeepSeek 等 | 可按任务切换或手动指定 |
| 移动端原生 | iOS / Android，PC 与手机同步 | Agent 可离桌继续跑任务 |
| 完全开源 | GitHub 公开核心代码，可审计 / fork | 许可证 AGPL-3.0 |
| 私有化离线部署 | 内网部署，数据不出本地 | 企业版商业支持另见咨询入口 |
| 需求与 SPEC 管理 | 对比表 ✓ | 相对 Cursor / Claude Code / Codex 的差异点 |
| PR / MR 自动代码审查 | 对比表 ✓ | 官网用例「Implement a feature」含开 PR |
| 团队协作与治理 | 成员、环境、模型、任务流程集中管理 | 私有化场景强调审计 |
| 安全审查（用例） | 官网 CASE：OWASP Top 10、依赖 CVE、SAST rules | **用例级能力，非产品主标题** |
| 代码补全 | 对比表 ✕ | 明确不做 IDE 补全型体验 |
| 本地 IDE / 本地 CLI | 对比表 ✕ | 与 Cursor 等差异：偏浏览器 + 云环境 |
| 桌面 MonkeyWork | 本地文件 / 终端 / 浏览器扩展；可接云任务 | 官网 Desktop 章节 |
| 计费 / 套餐 | Free / Pro / Ultra；积分充值与邀请 | 官网 Pricing；私有化另有 ENT |

## 可复制命令 / 金句

**命令（README / 安装入口原样）：**

```bash
# 克隆仓库
git clone https://github.com/chaitin/MonkeyCode.git

# 联网一键安装（需按安装脚本要求以 root 在 Linux 上执行）
bash -c "$(curl -fsSL 'https://monkeycode-ai.com/online/install')"
```

**金句 / 定位句（摘自 README / 官网，便于引用）：**

- EN：*MonkeyCode is an open-source **enterprise-grade AI development platform** with built-in development environment management, AI model management, AI task management, and project requirement management.*
- ZH：*MonkeyCode 是一款开源的**企业级 AI 开发平台**，内置了开发环境管理、AI 模型管理、AI 任务管理、项目需求管理等能力。*
- EN：*Unlike typical vibe coding tools, MonkeyCode is designed as an AI assistant for professional engineering teams.*
- ZH：*区别于其他的 vibe coding 工具，MonkeyCode 是真正面向专业开发团队的 AI 助手。*
- EN：*Give MonkeyCode a requirement and it carries the work from development to validation.*
- ZH：*把需求交给 MonkeyCode，它会从开发到验证一路接住。*
- License 句：*MonkeyCode is open source under the GNU Affero General Public License v3.0.* / *MonkeyCode 使用 GNU Affero General Public License v3.0 开源。*

## 坑与限制

1. **许可证 AGPL-3.0**  
   - 网络服务场景下修改后对外提供服务，通常需向用户提供对应源码义务（AGPL 网络条款）。  
   - 纯内网自用与对外 SaaS 的合规边界不同；官网同时提供开源版（GitHub）与团队/企业私有化商业支持入口（Contact us / 企业咨询）。二次分发或改包对外服务前应自行法务评估，**勿把博客解读当法律意见**。

2. **自托管门槛不低**  
   - 控制台 + **独立开发环境宿主机** 两档资源建议；不是「单容器随便起」叙事。  
   - 安装脚本要求 root、Linux、amd64/arm64；Runner 相关模板对 x86_64 检查 **AVX**（不支持则安装失败）。  
   - 后端 compose 可见 Postgres、Redis、ClickHouse、对象存储等组件——运维面重于轻量玩具项目。

3. **版本号可能不一致（待核实对齐策略）**  
   - GitHub Releases 最新 tag 抓取时为 `v26072801`（2026-07-28）。  
   - 官网 `online/install` 脚本内版本字符串曾见 `v261009`。  
   - 以安装通道实际下发包为准，勿假设 GitHub tag == 在线安装包版本。

4. **与商业产品 / SaaS 边界**  
   - OSS：完整源码，clone / fork，社区支持。  
   - 在线 SaaS：Free / Pro / Ultra 订阅与积分；个人 Free「长期可用」但有并发、云规格、日 token 配额等限制（以官网 Pricing 为准）。  
   - ENT：私有化离线部署 + 企业级安全与审计 + 商业支持（联系销售）。  
   - 文档站另有「用户权益调整公告」类页面——配额与权益以当时公告为准。

5. **能力边界（对比表诚实项）**  
   - **不做**本地 IDE / 本地 CLI / 代码补全（对比表为 ✕）。  
   - 「安全扫描」出现在用例区，**不是** README 六大主功能 bullet 的标题级能力；写知识卡片时勿夸大成「源码安全专用产品」。

6. **文档站抓取限制**  
   - `monkeycode.docs.baizhi.cloud` 为前端应用，纯 HTTP 抓取正文有限；细粒度运维步骤以浏览器打开部署文档为准（本 captur 未逐条展开离线包步骤）。

## 适合谁

| 人群 | 为何适合（据源文档） |
|---|---|
| 企业研发负责人 / 平台组 | 内网统一管模型、环境、成员与任务流程 |
| 需要数据不出域的团队 | 私有化 / 离线部署叙事 |
| 想少折腾本机环境的个人开发者 | 浏览器注册即用 + 云端环境 |
| 跨设备（办公室电脑 / 平板 / 手机）续任务的人 | 桌面 + 移动原生 |
| 需要国产主流模型接入的团队 | GLM / Kimi / MiniMax / Qwen / DeepSeek 等 |
| **不太适合**强依赖本地 IDE 补全、本地 CLI 工作流的人 | 产品对比表明确不主打这两项 |

## 源链接

| 类型 | URL |
|---|---|
| 官网 | https://monkeycode-ai.com/ |
| 在线服务（README EN 另列） | https://monkeycode-ai.net/ |
| GitHub | https://github.com/chaitin/MonkeyCode |
| 中文 README | https://github.com/chaitin/MonkeyCode/blob/main/readme.cn.md |
| 英文 README | https://github.com/chaitin/MonkeyCode/blob/main/README.md |
| LICENSE | https://github.com/chaitin/MonkeyCode/blob/main/LICENSE |
| 使用文档站 | https://monkeycode.docs.baizhi.cloud/ |
| 私有化部署文档节点 | https://monkeycode.docs.baizhi.cloud/node/019eb0f3-9424-7c93-9489-4e584f989527 |
| 企业咨询 | https://baizhi.cloud/consult |
| Discord | https://discord.gg/2pPmuyr4pP |
| Issues | https://github.com/chaitin/MonkeyCode/issues |
| 联网安装脚本 | https://monkeycode-ai.com/online/install |
