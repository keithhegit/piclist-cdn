# 腾讯云开源 Octop：本机单进程自托管 AI 助手全家桶

> 来源：掘金GitHub《腾讯开源版 WorkBuddy，一个进程跑全家桶》（2026-09-30 11:25 北京时间 = 2026-09-29 20:25 PT）· [原文](https://mp.weixin.qq.com/s/P1t6Z0OHDA07phC7Jkxrgw) · 全文见 `transcript.md`

## 攻略摘要

### 一句话定位

腾讯云开源的 **Octop**：本机单进程跑 Web 控制台 / CLI / 飞书钉钉等入口 + 多 Agent + Terminal/Browser AI + ACP（对接 Claude Code 等），数据默认落在 `~/.octop/`，偏隐私向自托管 AI 助手平台（非 SaaS 聊天窗）。

### 上手顺序 / 核心步骤

1. **认清定位**：不是又一个云端 Chat，而是「可并行运作的数字生命体」——用户 / Agent / 专家三层；多人可共用一实例、数据隔离。  
2. **一键安装（macOS/Linux，原文）**：`curl …/octop/install.sh | bash` → `octop run`（脚本用 uv 拉 Python 3.12，号称免 Docker、免手装 Python）。  
3. **选入口**：Web 控制台、CLI，或飞书 / 钉钉 / QQ / Discord / 企业微信；各入口进同一 Agent 管线。  
4. **配 Agent 与专家**：按角色建多个 Agent；需要时切「技术顾问 / 文案 / 数据分析」等专家库；可上 RAG 与可迁移记忆。  
5. **用执行层**：Terminal AI+、Browser AI+、远程桌面；编码任务可走 ACP 双向——`octop acp --agent main` 或把任务委派给 Claude Code / OpenCode / Codex。  
6. **接扩展**：Connector（OAuth + MCP）接腾讯文档等；存储可换 SQLite / PostgreSQL / COS/S3。  
7. **过安全习惯**：敏感 shell 需审批；注意命令白名单与 PII 脱敏；凭据默认本机。

### 能力或要点表

| 层 | 要点（原文归纳） |
|---|---|
| 入口 | Web、CLI、HTTP/SSE/WebSocket、飞书、钉钉、QQ、Discord、企微；共享消息管线 |
| 智能 | 多 Agent、16 种 MBTI 模板、专家库、知识库 RAG、harness-memory 可迁移记忆 |
| 执行 | Terminal AI+、Browser AI+（无头 Chromium）、远程桌面、ACP ↔ Claude Code / OpenCode / Codex |
| 扩展 | Connector（OAuth+MCP）、插件、本地/Docker/PostgreSQL/COS/S3 |
| 架构 | Python 3.12+ FastAPI + React；单进程 HarnessProcessor；数据 `~/.octop/` |
| 安全 | JWT 多用户隔离、工具审批、Shell 白名单、PII 脱敏；默认 SQLite |
| 许可/宣称 | MIT；文称约 2,728 Star；GitHub：`TencentCloud/Octop` |

### 可复制提示词 / 金句（verbatim）

文中几乎无「对话提示词」；可复制的是安装与 ACP 命令，以及金句：

```
# macOS / Linux 一键安装
curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash

# 安装后启动
octop run
```

```
octop acp --agent main
```

**金句短引**

- 「你的 AI 助手，数据存在谁那里？」
- 「所有数据留在你自己的机器上，一个进程启动，Web 控制台、CLI、飞书、钉钉、定时任务全部跑起来。」
- 「不是聊天窗口，是数字生命体」/「可并行运作的数字生命体」
- 「让 AI 跑在你的机器上，为你所用。」
- 「腾讯云出品，代码质量有保障。」（作者宣传语）

### 坑

- **标题 ≠ 产品名**：原标题写 WorkBuddy，正文讲的是 **Octop**；勿按 WorkBuddy 去搜安装包。  
- **管道安装脚本**：`curl | bash` 来自腾讯云 COS 域名；执行前应自行审脚本与供应链风险。  
- **「免 Docker / 免 Python」依赖 uv 隔离环境**：机器无外网、公司代理、或 ARM/老系统时可能翻车；文未给排错手册。  
- **单进程全家桶**：简单，但高并发/多 IM 桥接下的稳定性与资源占用文中未量化。  
- **Shell / 远程桌面 / Browser AI**：能力强 = 攻击面大；务必开工具审批，勿对不可信用户开放管理端。  
- **Star / 质量口号**：2,728 Star、「腾讯云出品有保障」为宣传口径，部署前应自己看仓库活跃度与 Issue。  
- **非 SEO/变现教程**：不讲收录、广告或站群；价值在本地 Agent 基建。

### 适合谁

- 想自托管、对话/凭据不出本机的个人开发者。  
- 家庭或小团队共用一套 AI、要账号隔离。  
- 已用 Claude Code / Cursor / 飞书钉钉，想把入口和记忆收拢到一台机器。  
- **对 Keith（Roblox 攻略/工具站 + 广告变现）**：间接相关——可作本机 agent 控制台、IM 触发批处理、Browser/Terminal 自动化沙盒；**不是** SEO/AdSense/Roblox Map 主线文。更贴标签：**AI 工具 / 自托管 Agent 基建 / 学习向**。  
- 不适合：只想用网页 Chat、不愿维护本机服务，或需要纯云端免运维的人。

### 章节导航

| 原文章节 | 要点 |
|---|---|
| 导语 | 云端助手数据外流 vs Octop 本机单进程；MIT / Star 宣称 |
| 01 数字生命体 | 用户 / Agent / 专家；家庭多 Agent 隔离 |
| 02 十二项核心能力 | 入口 / 智能 / 执行 / 扩展；ACP 双向 |
| 03 技术栈 | FastAPI + React；harness-*；`octop run` |
| 04 安全 | JWT、审批、白名单、PII；`~/.octop/octop.db` |
| 05 适合谁 | 开发者 / 家庭团队 / 合规 / 运维 |
| 结尾 | GitHub：https://github.com/TencentCloud/Octop |
