# 需求信号雷达：太难/头痛/买了就解决 + 搜索意图（what is trends）

> 调研日 2026-10-14 CST · 来源：X 公开搜索 round1–5 + Reddit 网页搜（日期 WARN）· 同步 2026-10-15


---

## whatistrends

需求信号与搜索意图雷达。云电脑项目目录（根路径 `/whatistrends` 无写权限，实际落在 `/workspace/whatistrends`，`/home/box/whatistrends` 为同名软链）。

## Notion 项目

- **Projects 行**：[what is trends](https://app.notion.com/p/3f9b35b6a57f81ce92e1f389a0dcb920)（Area：工作 + 投资/精进；Date 2026-10-14；同步日 2026-10-15 CST）
- 子页：method · strong-signals · search-intent-keywords · runs · scan index

## 目录

| 文件 | 说明 |
|------|------|
| `strong-signals.md` | 截至当前的强信号领域汇总（可迭代） |
| `search-intent-keywords.md` | 「太难 / 头痛 / 担心 → 搜什么来解决」关键词表 |
| `runs/` | 各轮扫描原始产出的索引与副本说明 |
| `method.md` | 怎么扫、怎么记、什么算强信号 |

原始扫描明细仍在：`/workspace/research/pain-signal-scan-2026-10-14/`（round1–5）。

## 当前结论（2026-10-14）

1. **AI agent 评测** — 抱怨 + 搜索意图都强；现有工具难上手；缺「买了就解决」共识。Keith 手头有方案。
2. **PC 硬件 / 游戏故障** — 抱怨、搜索、「买了就解决」三样齐。
3. **运营商 / 宽带** — 量与互动高，但换了仍常解决不了。

---

## 方法

## 信号三类（漏斗入口）

- **A 太难**：too hard / struggling / can't figure out / nightmare to …
- **B 头痛 / 担心**：headache / frustrating / pain in the ass / worried about …
- **C 买了就解决**：I bought / I switched to / I finally paid for / started using X and …

另加一类 **搜索意图**：how to / best X for / alternative to / looking for a tool / what do you use for …

## 平台

- **X**：自带公开搜索（不登录用户账号）；每分钟 30 / 每天 1000；每次最多 25 条。排除加密刷量模板。
- **Reddit**：浏览器常被拦；Parallel CLI 需 API key；临时用网页搜索限定 reddit.com（日期常不准确）。

## 什么算强信号

同时满足越多越好：

1. 同领域 ≥5 条干净第一人称样本（本周或近窗）
2. 有搜索意图问法（how / best / vs）
3. 有「买了 / 换了」或明确方案空白
4. 互动不是刷量投票抬起来的

## 记录规矩

- 强信号与关键词写进本目录文档，不只写记忆。
- 每轮扫描在 `runs/` 登记路径与日期。
- 引用必须带链接和日期，不编造。

---

## 强信号汇总

更新：2026-10-14 21:30 CST（X round 1–5 + Reddit 网页搜索替代）

## Tier 1

### AI agent 评测（Keith 已标记：手头有方案）

- **痛点**：定义「好」难；多步 / 工具调用错误抓不到；trace 堆着不回灌 eval；LLM-as-judge 不稳；Promptfoo 全绿仍亏钱；现成工具（Langfuse / LangSmith / Braintrust / Arize）上手吓人。
- **搜索意图**：how to evaluate ai agents、how to write llm evals、evaluate multi-turn agent、rag evaluation metrics、llm-as-judge rubric、langsmith / langfuse alternative。
- **缺口**：几乎没有第一人称「买了 X 评测就好了」；可能空白 = 核对 AI 评委 vs 人工标注、自动给中间步骤打分。
- **R5 新问法**：LLM-as-a-judge rubric drift / positional bias 难复现；golden dataset 才是难点；RAG「trusting its answers」清单帖。
- **样本来源**：`pain-signal-scan-2026-10-14/round2`（X 15 + Reddit 10）、`round4`（搜索意图 10）、`round5`（4，偏薄）

### PC 硬件 / 游戏故障

- **痛点 + 购买**：KVM、SSD 克隆转接器等「买了就解决」干净。
- **搜索意图**：游戏崩溃、手柄被认成 Xbox、显示器无信号、Fn lock 等 how-to fix。
- **R5 新主题**：「is it worth upgrading」RAM（按价格问、为本地大模型问）/ 显示器刷新率；coil whine 待机啸叫。
- **样本**：round3（6）、round4（13）、round5（6）

## Tier 2

### 运营商 / 宽带（尼日利亚、印度、美国）

- 换运营商量大；经常换了仍不行。
- 搜索：best network / A vs B / Starlink vs fiber 价格。
- 互动高，但投票帖会抬高数字。
- R5：「keeps dropping / disconnecting」「cheapest data plan」；新地区南非（Vumatel）；主播断流影响直播；媒体「WiFi keeps disconnecting fix」帖 205 赞，印证搜索需求。样本 round5（7）。

## 新候选（R5）

### AI 订阅用量上限（Claude / Codex / SuperGrok 等）

- 痛点 + 付费直接共现：升级 $50→$200 仍两天撞限；加 $10 很快烧完；「is it worth upgrading to Claude Max 20x」。
- 样本：round5（8），仅一轮，待复核是否本周热点。

## Tier 3（弱，先记着）

家居 / 睡眠、健康穿戴 / 助听器、房贷 / 小企业付款、网购退货尺码、创作软件买断 vs 订阅。

## 几乎无信号

Notion/Linear 类效率 SaaS、Airbnb/Expedia、Coursera/Udemy（本轮加品类词后多为噪音）。

## 待办

- [ ] Parallel API key 到位后补 Reddit 本周评论（带日期）
- [ ] 对 Tier 1 关键词做搜索量 / SERP 竞争（等 Keith 点头）
- [ ] AI agent 评测领域社媒前三账号对标（等 Keith 点头）

---

## 搜索意图关键词

来源：2026-10-14 X round4–5（+ Reddit 侧面印证）。用于后续 Trends / SERP / GSC，不是已验证的搜索量。

## AI agent 评测

- how to evaluate ai agents
- how to write llm evals
- evaluate multi-turn agent
- rag evaluation metrics
- llm-as-judge rubric
- langsmith alternative
- langfuse alternative
- monitor background agent runs
- how to test tool calling agents
- llm as a judge positional bias（R5）
- how to build golden dataset llm eval（R5）
- rag evaluation checklist（R5）

## PC / 游戏故障

- pc crashes when playing games fix
- fortnite crashing pc fix
- oblivion remastered gpu crash
- ps4 controller showing as xbox controller pc
- 8bitdo buttons swapped fix
- monitor no signal pc turns on
- how to turn off fn lock
- is it worth upgrading ram 48gb to 96gb（R5）
- ram for local llm 5090（R5）
- 240hz vs 500hz worth it（R5）
- coil whine at idle fix（R5）

## 运营商 / 宽带

- best network in nigeria 2026
- mtn vs airtel
- starlink vs jio price india
- starlink india price per month
- should i switch to starlink from fiber
- airtel 5g router not connecting after reset
- wifi keeps disconnecting windows 11 fix（R5）
- internet keeps dropping every few minutes（R5）
- cheapest data plan india 2026（R5）
- vumatel internet down（R5）
- best mesh wifi 2026（R5）

## AI 订阅用量上限（R5 新）

- claude usage limit reset
- is claude max worth it
- codex weekly limit
- chatgpt usage limit workaround

## 扩词模板（漏斗入口）

问法骨架：`how to [症状]` / `best [品类] for [场景]` / `[A] vs [B]` / `alternative to [工具]` / `looking for a tool that [结果]` / `what do you use for [任务]`

痛点共现词：too hard, struggling, headache, frustrating, nightmare, worried about, can't figure out

---

## 扫描轮次索引

| 轮次 | 日期 | 平台 | 路径 | 摘要 |
|------|------|------|------|------|
| 1 | 2026-10-14 | X（+ Reddit 失败） | `/workspace/research/pain-signal-scan-2026-10-14/` | 试水；词表噪音大；X 13 条有效 |
| 2 | 2026-10-14 | X + Reddit 网页搜 | `…/round2/` | 收紧第一人称；AI eval 成形；Reddit 19 条日期未确认 |
| 3 | 2026-10-14 | X | `…/round3/` | 排除 AI eval；ISP 6 + PC 硬件 6 |
| 4 | 2026-10-14 | X | `…/round4/` | 搜索意图词；PC fix 13 / ISP 10 / AI eval how-to 10 |
| 5 | 2026-10-14 | X | `…/round5/` | Tier-1 新问法 + 新赛道；AI 订阅额度 8（新）；ISP 7；PC 升级/啸叫 6；AI eval 4 |

项目文档入口：`/workspace/whatistrends/`
