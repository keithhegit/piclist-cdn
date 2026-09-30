# OpenConnector 开源 Agent 连接器网关 - 抖音

> **校对说明（重要）**  
> **抖音成片未得；依据开源仓库/介绍页。**  
> 箱内拉取抖音成片/字幕失败：`yt-dlp` 报 *Fresh cookies are needed*；分享页 SSR 无口播文案；iesdouyin iteminfo 返回 `encrypt_data_miss`。  
> **本稿不是抖音口播 ASR**，而是据一手源整理的校对稿（仓库 README / 官网 / 自部署文档）。账号剪辑口径 vs 源文档口径请分开引用。

| 字段 | 值 |
|---|---|
| 平台 | 抖音 |
| 作者 | 许工跑得通 |
| 原视频标题（分享文案节选） | 我们开源了Open Connector 介绍我们刚… |
| 视频 ID | `7661284688006253876` |
| 正式链接 | https://www.douyin.com/video/7661284688006253876 |
| 短链 | https://v.douyin.com/rqh3HexPf2A/ |
| 一手源 | https://github.com/oomol-lab/open-connector · https://openconnector.io/zh-cn/ · https://oomol.com/zh-cn/docs/openconnector-self-hosting/ |
| 许可证 | Apache-2.0（以仓库 LICENSE 为准） |

---

## 一句话定位（源口径）

OpenConnector 是面向 AI Agent 的**开源 connector gateway**，可视为 Pipedream / Composio 的开源替代：账号只连一次，就把 **1,000+ provider、10,000+ 预置 Action** 的共享 catalog，通过 SDK / CLI / MCP / HTTP / OpenAPI 暴露给 Agent；**provider 凭据留在 runtime 边界内**，不交给 Agent 进程。

---

## 它解决什么问题

- Agent 要调 GitHub、Gmail、Notion、Slack 等真实 SaaS，但**不想把 token 塞进环境变量 / prompt**。
- 需要统一的 Action 契约（输入 schema、required scope、可审查的 executor），而不是每个服务手写胶水。
- 希望先用托管 OAuth 快速上线，同时保留**自托管 / 私有化**迁移路径（开源版与 OOMOL 托管共用 provider id / Action id / schema）。

---

## 架构（源口径摘要）

```
AI Agent / App  --SDK/CLI/MCP/HTTP-->  OpenConnector Gateway
                                       ├ Credential & OAuth Boundary
                                       ├ Provider Catalog
                                       ├ Action Executors（按需加载）
                                       ├ Tokens / Scopes / Allow-Block Policy
                                       └ Run Logs（脱敏）
                                              │
                                              ▼
                                       1,000+ Providers
```

Agent 看到的是：schema、scope、安全账号标签、执行结果；**原始 provider secret 不离开 runtime**。

---

## 使用路径（两选一，可迁移）

| 路径 | 适合谁 | 提供什么 |
|---|---|---|
| **开源自托管** | 要掌控基础设施 | Docker / Node、SQLite（或 PG）、MCP、HTTP、OpenAPI、Web 控制台；OAuth app 自己申请 |
| **OOMOL 托管** | 想立刻授权账号 | 托管 OAuth + runtime + Connect 点数；契约与开源版兼容，后续可迁回自托管 |

官网入口：https://openconnector.io/zh-cn/  
托管入口：https://oomol.com/apps  

---

## 快速开始（自托管 · 可复制）

### 1）Docker Compose 起 runtime

```bash
git clone https://github.com/oomol-lab/open-connector.git
cd open-connector
docker compose up
# 或从源码构建：docker compose -f docker-compose.yml -f docker-compose.build.yml up --build
```

预构建镜像：`ghcr.io/oomol-lab/open-connector`（`latest` / 具体版本 / `tip`）。

控制台与文档：

```text
http://localhost:3000
http://localhost:3000/docs
```

### 2）无鉴权冒烟（Hacker News）

```bash
curl -s -X POST http://localhost:3000/v1/actions/hackernews.get_top_stories \
  -H 'content-type: application/json' \
  -d '{"input":{}}'
```

### 3）接 GitHub（API Key / PAT 最简单）

```bash
curl -s -X PUT http://localhost:3000/api/connections/github \
  -H 'content-type: application/json' \
  -d '{"authType":"api_key","values":{"apiKey":"github_pat_..."}}'

curl -s -X POST http://localhost:3000/v1/actions/github.get_current_user \
  -H 'content-type: application/json' \
  -d '{"input":{}}'
```

命名多账号连接时加 `"connectionName":"work"`；调用时用 header `x-oo-connector-alias: work`（或 `alias` query）。

### 4）给 Agent：MCP 入口

```text
http://localhost:3000/mcp
```

MCP 面向发现的工具包括：`list_apps`、`search_actions`、`get_action_guide`、`execute_action`。

单 Action 可读指南：

```bash
curl -s http://localhost:3000/api/actions/hackernews.get_top_stories/agent.md
```

### 5）TypeScript SDK 示例（官网）

```typescript
import { OpenConnector } from "@oomol-lab/connector";

const connector = new OpenConnector({
  baseUrl: "http://localhost:3000",
  runtimeToken: process.env.OOMOL_CONNECT_RUNTIME_TOKEN,
});

const stories = await connector.hackernews.get_top_stories({});
console.log(stories);
```

### 6）oo CLI 示例（官网）

```bash
oo connector login http://localhost:3000
oo connector search "Hacker News"
oo connector schema hackernews.get_top_stories
oo connector run hackernews --action get_top_stories --data '{}'
```

---

## 生产必设环境变量（自部署文档口径）

| 变量 | 用途 |
|---|---|
| `OOMOL_CONNECT_ADMIN_TOKEN` | 保护 Web 控制台 / `/api` / `/docs` |
| `OOMOL_CONNECT_ENCRYPTION_KEY` | 加密存储的凭据与 OAuth client；**丢失则已加密数据不可恢复** |
| `OOMOL_CONNECT_ORIGIN` | 公开 origin，用于拼 OAuth callback：`{ORIGIN}/oauth/callback` |
| Runtime tokens（`oct_…`） | Agent/SDK 调 `/v1` 与 `/mcp`；控制台 Access 创建，只显示一次 |
| `OOMOL_CONNECT_ALLOWED_ACTIONS` / `BLOCKED_ACTIONS` | Action 白/黑名单（blocked 优先） |

公开暴露时：管理面用 admin token，运行面用 runtime token；二者不要混用。

OAuth callback（默认本地）：

```text
http://localhost:3000/oauth/callback
```

须与 provider OAuth app 里填的 **一字不差**。

---

## 生态与相关项目

- 仓库：https://github.com/oomol-lab/open-connector  
- Connector SDK：https://github.com/oomol-lab/connector-sdk  
- oo CLI：https://github.com/oomol-lab/oo-cli  
- 桌面 Agent **Wanta**（配 OpenConnector 用已连 SaaS）：https://github.com/oomol-lab/wanta  

要求 Node.js **22+**（源码开发路径）。

---

## 引用边界提醒

- 抖音口播具体措辞、演示画面、星标数字等：**本稿未覆盖**（成片未得）。  
- 星标数、provider/Action 计数以 GitHub / catalog 动态徽章为准，会随时间变化。  
- 「账号剪辑说开源了」≠ 本仓库每一段都已亲测；落地前仍应对照当前 `main` / release tag 与具体 Action 验证说明。
