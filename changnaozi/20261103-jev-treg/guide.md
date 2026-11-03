# Jev×Treg 开源找人：Agent 按次获客

> **来源说明：视频号口播未得；依据公开报道+仓库。** GeekTechs 视频号成片（2026-11-01）被扫码墙挡住，没听到口播。本攻略依据量子位 2026-11-01 报道（与视频高度同题）、网易转载、深度调教、Treg GitHub 仓库和 Broch Builds 安装说明整理。数字都标了出处：「官方」= Treg/TypeSafe 公布，「自测」= 官方自建测试，没有第三方复现。

## 一句话定位

TypeSafe AI（Jev 母公司）和 Treg 把「找人 + 查邮箱」做成 Claude Code 等 Agent 能直接调用的工具链：你描述目标客户画像，Agent 自己去人库捞人、筛选、查邮箱、验邮箱。按条计费，最低约 6 分钱一条线索，找不到不收费。

## 上手顺序

1. **装 Treg**：在 Claude Code 里装插件，或者用 skills / CLI 装（命令见下）。新用户约有 $1 免费额度（官方）。
2. **说画像**：用自然语言描述目标人群，比如行业、职位、地区、公司规模、数量。
3. **先看价再付费调用**：让 Agent 先报预估条数和费用，确认后再跑查邮、验邮、补 LinkedIn 这些收费步骤。
4. **抽检结果**：随机挑几条人工核对任职和邮箱，再决定要不要批量外联。

## 流程拆解（官方描述）

画像 → Treg 调人库 → Jev 判断闸门（筛掉不匹配的人）→ 查邮箱 / 验邮箱 / 补 LinkedIn 履历

## 能力与数字

| 项 | 内容 | 出处标签 |
|---|---|---|
| 单价 | 最低 $0.0089/条邮箱线索（约 6 分钱），找不到不收费；验邮、补履历、公司动态另计 | 官方 |
| vs Clay（同批 292 人） | Treg：$1.49 / 289 个邮箱 / 264 完全匹配；Clay：$10.34 / 280 / 262 → 称便宜超 85% | 官方自测 |
| People Search Bench（119 任务） | B2B 拓客：Claude Code 单独 43% → 接 Treg 78.2%；另三类 80% / 76.3% / 62.9% | 自建榜，无第三方复现 |
| 自带 key | 接自己的 Hunter 等 key，不走 Treg 计费 | 官方 |
| 免费额度 | 新用户约 $1 | 官方 |
| 许可 | Apache 2.0 + 附加限制：可以自托管给自己团队用，未经许可不能做成对外托管服务 | 仓库 |
| GitHub Star | 量子位发文时约 6400；网易 11/2 称约 6958 | 时间点数据 |

## 可复制命令

Claude Code 插件：

```
/plugin marketplace add superdesigndev/treg
/plugin install treg@treg
```

Skills 方式：

```
npx skills add superdesigndev/treg
```

CLI：

```
curl -fsSL https://treg.to/install.sh | sh
```

（`curl | sh` 会直接执行远程脚本，建议先打开 install.sh 看一眼再跑。）

## 示例 prompt（中文精简版，改编自 Broch Builds「Build me a lead list…」）

```
帮我建一份线索名单：美国 50–500 人规模的 B2B SaaS 公司，职位是增长或市场负责人（Head of Growth / VP Marketing），先找 50 人。
先告诉我预计能找到多少人、查邮箱和验邮箱大概花多少钱，等我确认再执行。
结果输出成表格：姓名、职位、公司、LinkedIn、邮箱、邮箱验证状态。
```

## 坑

- **准头**：有用户实测搜自己或队友可能搜不到；冷门地区和小公司的覆盖率要自己抽检。
- **合规**：个人邮箱、任职信息的采集和外联（GDPR、CAN-SPAM、国内个保法等）由使用者自负。
- **许可**：严格说是 source-available，不是纯开源。可以自托管给内部团队，不能未经许可做对外托管服务。
- **开源 ≠ 数据自持 ≠ 免费**：代码开放，但人库和邮箱数据在 Treg 那边，按条付费。
- **自测榜**：对 Clay 便宜 85%、Bench 从 43% 到 78.2% 都是官方自测，没有第三方复现，引用时要带上这个标签。

## 适合谁

- 做 B2B 外联、拓客的独立开发者和小团队，想用 Agent 替代 Clay / Apollo 这类按席位收费的工具
- 已经在用 Claude Code 等 Agent，想给 Agent 加「找人」能力的人
- 不太适合：要求极高覆盖率和准确率的大规模销售团队，或者合规要求严格的行业

## 章节导航

1. 一句话定位
2. 上手顺序
3. 流程拆解
4. 能力与数字
5. 可复制命令
6. 示例 prompt
7. 坑
8. 适合谁

## 源与账号剪辑区分

- **账号口径（GeekTechs 视频号）**：只拿到标题和封面：「杀疯了！…6 分钱一条线索，AI 获客工具要变天」。口播没听，具体怎么讲的、有没有额外实测都不清楚。
- **一手/对照源**：
  - Treg 仓库 https://github.com/superdesigndev/treg
  - 量子位 https://www.qbitai.com/2026/11/506922.html
  - 网易转载 https://www.163.com/dy/article/LANT0S3R0556OXHR.html
  - 深度调教 https://deeptame.com/a/jev-treg-open-source-person-search-tool
  - Broch Builds https://brochbuilds.com/leads
  - Jason Zhou LinkedIn / treg.to/people-search
- 「AI 获客工具要变天」「杀疯了」是账号的标题话术，不代表实际效果；数字以上表的出处标签为准。
- 用户源链：https://weixin.qq.com/sph/AdAdYc7F27
