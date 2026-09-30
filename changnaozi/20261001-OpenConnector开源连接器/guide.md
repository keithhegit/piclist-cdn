# OpenConnector 开源 Agent 连接器网关 - 抖音

> **抖音成片未得；依据开源仓库/介绍页。**  
> 源：`oomol-lab/open-connector` · openconnector.io · OOMOL 自部署指南。  
> 抖音：作者 **许工跑得通** · 视频 `7661284688006253876` · https://www.douyin.com/video/7661284688006253876

## 一句话定位

把「Agent 调 1000+ SaaS」收成一层**可自托管的连接器网关**：凭据进 runtime，Agent 只拿结构化 Action（MCP / HTTP / SDK / CLI）。

## 适合谁

- 在做 Agent / Bot 产品，要接 GitHub、Gmail、Notion、Slack 等，又不想 token 进 prompt。
- 想要 Composio/Pipedream 同类能力，但要开源、可审查、可私有化。
- 先用 OOMOL 托管 OAuth 跑通，再迁自托管的团队。

## 上手顺序（建议 30–60 分钟）

1. **克隆并起 Docker**：`docker compose up` → 打开 `http://localhost:3000`。
2. **无鉴权冒烟**：`POST /v1/actions/hackernews.get_top_stories`。
3. **设加密与管理令牌**（本机也建议设）：`OOMOL_CONNECT_ENCRYPTION_KEY` + `OOMOL_CONNECT_ADMIN_TOKEN`。
4. **接一个 API Key provider**（GitHub PAT）→ `github.get_current_user`。
5. **给 Agent 开 runtime token** → 配 MCP：`http://localhost:3000/mcp`（或 SDK baseUrl）。
6. （可选）为 Gmail 等配 OAuth：设 `OOMOL_CONNECT_ORIGIN`，callback 填 `{ORIGIN}/oauth/callback`。
7. （可选）用 `OOMOL_CONNECT_ALLOWED_ACTIONS` 收紧可执行 Action。

## 能力表

| 能力 | 说明 |
|---|---|
| Catalog | 1,000+ provider / 10,000+ Action（动态数字以 catalog 为准） |
| 鉴权 | API key、OAuth2、自定义凭据、无鉴权 provider |
| 暴露面 | MCP、HTTP `/v1`、OpenAPI、Web Console、Action `agent.md` |
| 策略 | connection alias、runtime token、allow/block Action、脱敏 run logs |
| 部署 | Docker/Node 本地、Cloudflare Workers(D1+R2)、Fly 等；或 OOMOL 托管 |
| 多账号 | `connectionName` + `x-oo-connector-alias` |

## 可复制命令 / 金句

**冒烟**

```bash
curl -s -X POST http://localhost:3000/v1/actions/hackernews.get_top_stories \
  -H 'content-type: application/json' \
  -d '{"input":{}}'
```

**存 GitHub 连接 + 调用**

```bash
curl -s -X PUT http://localhost:3000/api/connections/github \
  -H 'content-type: application/json' \
  -d '{"authType":"api_key","values":{"apiKey":"github_pat_..."}}'

curl -s -X POST http://localhost:3000/v1/actions/github.get_current_user \
  -H 'content-type: application/json' \
  -d '{"input":{}}'
```

**MCP 地址**

```text
http://localhost:3000/mcp
```

**SDK 骨架**

```typescript
import { OpenConnector } from "@oomol-lab/connector";
const connector = new OpenConnector({
  baseUrl: "http://localhost:3000",
  runtimeToken: process.env.OOMOL_CONNECT_RUNTIME_TOKEN,
});
```

**口诀（源思想压缩）**：*Connect once → Discover Action → Execute under policy；secret stays in gateway.*

## 坑（必看）

1. **Admin token ≠ Runtime token** — `/api`、控制台用 admin；`/v1`、`/mcp` 用 `oct_…`。混用会 401。
2. **ENCRYPTION_KEY 丢了等于凭据库报废** — 必须进密钥管理；换 key 无法解密旧数据。
3. **OAuth callback 必须一字不差** — 改端口/域名后要同步改 provider 应用里的 callback，并设 `OOMOL_CONNECT_ORIGIN`。
4. **公开部署必须双令牌 + 防火墙** — 镜像默认绑 `0.0.0.0`；暴露前先私有创建第一个 runtime token。
5. **Action policy 与 Proxy policy 分开** — `ALLOWED_ACTIONS` 不自动覆盖 provider proxy；proxy 另有 `ALLOWED_PROXIES` / token 的 `allowedProxies`。
6. **Blocked 优先于宽 allowlist** — 例如允许 `github.*` 仍可单独 block `github.delete_repository`。
7. **Catalog 里有 ≠ 你已验证** — 用前查该 Action 的源码修订与 verification；目录定义、本地 executor、上游 API 成功是三层证据。
8. **抖音成片未得** — 勿把本攻略当成口播逐字引用；数字（星标、Action 数）以仓库/徽章实时值为准。
9. **Node 版本** — 源码开发路径要求 Node 22+。
10. **多账号忘记 alias** — 默认连接 vs `connectionName: work`；调用时漏 `x-oo-connector-alias` 会打到错误账号或找不到凭据。

## 章节导航（对照一手源）

| 想做的事 | 去哪看 |
|---|---|
| 项目是什么 | https://openconnector.io/zh-cn/ · `docs/README.zh-CN.md` |
| 本地 5 分钟 | `docs/quickstart.md` · Docker Compose |
| 自部署加固 | https://oomol.com/zh-cn/docs/openconnector-self-hosting/ |
| Runtime / MCP API | `docs/runtime-api.md` |
| GHCR 镜像 | `docs/docker-ghcr.zh-CN.md` |
| Cloudflare | `docs/cloudflare.md` / quickstart Cloudflare 段 |
| 凭证与 OAuth | `docs/credentials.md` |

## 和本助手栈的关系（启发式备注）

若目标是给 Grok Bot / Cursor / MCP 客户端扩工具面：优先自托管或托管 OpenConnector → 配 runtime token → MCP 指到 `/mcp`，再按 Action allowlist 收权。具体是否入库挂「Grokbot应用修炼」见属性推荐，由用户确认。
