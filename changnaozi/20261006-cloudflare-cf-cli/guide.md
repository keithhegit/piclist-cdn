# Cloudflare 新 CLI（cf）：把 3000+ API 装进终端，让 Agent 接管云基建

## 攻略摘要

### 一句话定位
介绍 Cloudflare 官方新 CLI 工具 `cf`：把全平台 3000+ API 收进一条命令行，并按「给人用 + 给 Agent 用」设计，覆盖临时公网隧道、静态站部署、意图搜命令、D1 边缘数据库与 Agent 基建闭环。

### 上手顺序 / 核心步骤
1. **准备账号与环境**：注册 Cloudflare（免绑卡）→ 本机 Node.js v20/v22+。
2. **安装与登录**：`npm i -g cf` → `cf --version` → `cf auth login`（设备码浏览器授权）→ `cf auth whoami`。
3. **（可选）关遥测**：在 shell 配置里加 `export DO_NOT_TRACK=1`。
4. **玩法一 · 临时公网**：本地服务跑着时执行 `cf tunnels quick-start http://localhost:端口`，拿到 `*.trycloudflare.com` 分享；Ctrl/Cmd+C 即毁。
5. **玩法二 · 静态上线**：`cf init my-site` → 放入 `index.html` → `cd my-site && cf deploy` → 首次选 `workers.dev` 子域名。
6. **玩法三 · 意图搜命令**：`cf cli search "create database"`（英文意图；中文会空结果）。
7. **玩法四 · D1 数据库**：`cf d1 create --name my-db` → 用返回的 UUID 跑 `cf d1 query … --sql "…"`。
8. **玩法五 · 交给 Agent**：告知已装好并登录 `cf`，让 Agent 用 `cf cli search` 查命令、写 `cloudflare.config.ts`、执行 `cf deploy`。

### 要点表

| 主题 | 要点 |
|------|------|
| 工具定位 | 官方 `cf` CLI，打包计算/存储/网络/AI/安全等 3000+ API |
| 安装 | `npm i -g cf`（需 Node 20/22+） |
| 鉴权 | `cf auth login` 设备码流程，无需手动抠 API Token |
| 隐私 | 默认匿名遥测命令频次与 search 词；可用 `DO_NOT_TRACK=1` 关闭 |
| 临时分享 | `cf tunnels quick-start` → trycloudflare.com，免域名/SSL/服务器 |
| 持久静态站 | `cf init` + `cf deploy` → workers.dev，自带 HTTPS + CDN |
| 命令发现 | `cf cli search` 基于英文文档 MiniSearch；中文查询返回 `[]` |
| D1 | 边缘 SQLite；`create --name` + `query <uuid> --sql` |
| Agent | CLI 输出 MCP 风格工具描述；配置改为 `cloudflare.config.ts` 类型检查闭环 |
| 官方数据（文中引用） | Agent 调用占比：2025初个位数 → 2026-03 约 25% → 新 CLI 发布前一周约 48% |

### 可复制提示词 / 金句

**给 Agent 的提示词（原文）：**
```
我本地已经装好了 Cloudflare 的 cf 工具并完成了登录。请帮我用 cf CLI 查一下怎么创建 D1 数据库，帮我建一个名为 my-notes 的数据库，并在当前目录下把配置写好，然后执行 cf deploy 帮我上线。
```

**口语化意图示例（原文）：**
```
你需要帮我在 Cloudflare 上去建个数据库。
```

**金句 / 可摘录表述（原文）：**
- 在很多开发者圈子里，大家更习惯亲切地称它为「赛博菩萨」或「互联网大善人」。
- 日常折腾完全不用花一分钱，不用担心账单刺客。
- 它把整个 Cloudflare 平台涵盖计算、存储、网络、AI、安全在内的 3,000 多个 API 操作，全部打包进了一个小巧的命令行工具里。
- Cloudflare 在设计 cf 这个命令行工具时，就已经把 Agent 视作了一等公民。
- Agent 不在乎这些。Agent 更需要的是一个可以用文字对话的接口，一个稳定的、结构化的、可组合的接口。
- 基础设施的使用门槛，正在被 AI 全面重塑。

**常用命令速抄：**
```bash
npm i -g cf
cf --version
cf auth login
cf auth whoami
export DO_NOT_TRACK=1
cf tunnels quick-start http://localhost:4000
cf init my-site
cd my-site && cf deploy
cf cli search "create database"
cf d1 create --name my-db
cf d1 query <你的数据库UUID> --sql "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);"
cf d1 query <你的数据库UUID> --sql "INSERT INTO users (name) VALUES ('KK');"
cf d1 query <你的数据库UUID> --sql "SELECT * FROM users;"
```

### 坑
- **「完全免费 / 不用担心账单」**：Cloudflare 免费额度慷慨，但超额、企业功能、流量与请求仍可能产生费用；「日常折腾不用花钱」是营销口径，需自行核对当前 Free plan 限额。
- **「不需要绑定信用卡」**：注册门槛低属实，不等于永远零账单；开通部分产品或升级时仍可能要求付款方式。
- **中文 `cf cli search` 无效**：索引是英文文档，中文意图返回 `[]`；需英文关键词或交给 Agent 翻译后再搜。
- **隧道 vs 部署**：`tunnels quick-start` 依赖本机进程在线，关终端即断；要 24h 在线应用 `deploy`，且文中示例偏静态/前端，不是任意后端长驻方案。
- **D1 `create` 参数**：新 CLI 要用 `--name`，旧习惯可能踩坑。
- **首次 Workers 子域名**：每个账号设置一次 `workers.dev` 名，选前想好。
- **遥测默认开启**：命令频次与 search 词会匿名上报，隐私敏感环境务必设 `DO_NOT_TRACK=1`。
- **Agent「再也不会对抗」**：文中对比偏理想化；权限、配额、网络与错误处理仍需人盯。
- **引用的 Agent 调用占比数据**：来自 Cloudflare 官方博客的转述，未在文中给出可核链接与口径定义，宜当趋势参考而非精确统计。
- **「3000+ API 全部打包」**：覆盖面宣传语，具体子命令可用性、稳定度需以官方文档/实际 `--help` 为准。

### 适合谁
- 想快速把本地 Demo 分享给朋友、又不想买服务器的前端/独立开发者
- 需要免费静态站 / workers.dev 托管的个人站、简历页、小工具作者
- 已在用 AI Agent 写代码、希望 Agent 能直接操作云基建的人
- 被 Cloudflare 网页控制台劝退、更习惯终端的开发者
- 不太适合：完全无终端基础、需要复杂 VPC/传统云主机运维、或强监管下不能用境外 CDN 的场景（需自行评估合规与访问）

### 章节导航
1. 开篇：Cloudflare「赛博菩萨」印象与控制台劝退 → 引出新 CLI `cf`
2. 零门槛安装与登录（账号、npm 安装、设备码授权、关闭遥测）
3. 玩法一：`cf tunnels quick-start` 本地变公网
4. 玩法二：`cf init` + `cf deploy` 静态站上线
5. 玩法三：`cf cli search` 意图搜命令（中英差异）
6. 玩法四：D1 建库与 SQL 读写
7. 玩法五：把 `cf` 交给 Agent（MCP 描述 + `cloudflare.config.ts`）
8. 写在最后：Agent 调用占比数据与「基建门槛被 AI 重塑」
