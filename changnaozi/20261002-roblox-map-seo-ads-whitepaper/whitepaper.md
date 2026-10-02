# Roblox Map SEO Ads · 白皮书（目标·现状·Fresh最优方案·双轨Skill）

**2026-10-02 CST · 长脑子了起草 · Researchy Fresh方案已核验对齐（见 §5 / 附录 C）**

---

## 1. 一句话玩法与变现目标

**热门 Roblox 地图 → 英文 SEO 攻略站 → 站内 Adsterra 变现。**

选数据密度高、SERP 窗口仍开的地图，用可核验事实 + YouTube 字幕供给厚页，挂 Native Banner / 300×250，靠 Google 自然流量吃广告。不做 AI 空壳、不做无核验 Codes「Working」、不换 AdSense 栈。

---

## 2. 三站对照表

| 站 | Apex | CF Pages 项目 | Ads | Codes |
|----|------|---------------|-----|-------|
| Anime Dice | https://animedice.top | `anime-dice-guides` | Native Banner + 300×250（bauval） | unverified；无核验不进 Working |
| Loot To Forge | https://loot2forge.top | `loot-to-forge-guides` | 同上 | 同上 |
| Fish It | https://robloxfish.top | `fish-it-guides` | 同上 | 同上 |

> 注：`anime-dice-guides` / `loot-to-forge-guides` / `fish-it-guides` 是 **Cloudflare Pages 项目名**，不是站点 URL 路径；对外入口为各站 Apex。

三站共用：Adsterra only（无 pop）、双闸（Researchy 事实 + UI 视觉）、远程控制负责 Upload/编码、长脑子了仅 GSC + Notion。

---

## 3. 现状快照 2026-10-02

| 项 | 状态 |
|----|------|
| Sprint-Fresh-1 | **结案** |
| Anime Soft | `27efab43` 清 Screenshot |
| Anime GSC | Domain sitemap **Success**；discovered **20** |
| 角色锁 | **远程控制**：Upload / 编码；**长脑子了**：仅 GSC + Notion（不碰 gated zip） |

下一阶段：按 §5 Researchy 核验的 Fresh P0 包跑 1–2 轮，Playbook 厚站轨与 Freshener 72h 轨双轨并行。

---

## 4. 硬规则

1. **Codes**：无核验 / 无 `source_url` → **不得**标 Working。
2. **Fish ≠ Fisch**：禁 RNG 预测类工具与文案混名。
3. **Adsterra only**：无 pop / 无换 AdSense 栈。
4. **双闸**：Researchy 事实 PASS + UI 视觉 PASS 后才能 Upload；空票 skip。
5. **无 ludusdex**：周更已 stale；关键词只用 Trends / YouTube / Reddit / GSC。
6. **不 fork H5 / R2**：不偷 scrape/wash，不托管游戏本体；只在现有 CF Pages 仓做最小 diff。

---

## 5. 最优 Fresh 方案（下一 1–2 轮）· Researchy 核验 · 2026-10-02

> **状态：Researchy 核验 · 2026-10-02**（输入：`/workspace/roblox-map-seo-ads/fresh-optimal-plan-researchy-2026-10-02.md`，全文见 **附录 C**）。  
> 排序原则：先补「可核验缺口 + 过审/AI 可抽取地基」，再内容加厚；仍走 value filter（≥1 hard）；空票 skip。  
> 硬锁：不换 Adsterra（Native + 300×250）；Codes 永不 Working/未局内核验；禁 ludusdex；无发明 CCU/点击。

**一句话结论（Researchy）：** 下一轮 Fresh 最优包 =「合规信任页（Anime/Loot Privacy）+ AI/Snippet 可抽取层（FAQPage JSON-LD + ≤150 直答）+ 索引闭环（sitemap/GSC）+ 情境内链」；内容加厚仍跟 72h value filter。推流靠可索引可引用结构与真实需求信号，**不靠** sitemap 成功态。

映射：SEO43 + AI五步 + Perplexity四步（详见 Researchy 输入 §1）。

### P0-1 — Anime + Loot `/privacy/`（Fish 已有）+ 页脚可点

| | |
|--|--|
| **为何** | AdSense五要素第一大漏项；SEO43「像正经站」；保留 AdSense 选项且**不换**现网 Adsterra。Fish 已 200，Anime/Loot 公开 404（Researchy 本轮 curl）。 |
| **验收** | `https://{anime,loot}/privacy/` → 200；页脚有 Privacy；文内无 `[Company]`/`[Email]` 占位；写明 cookies/ads（含 Adsterra）与联系邮箱；**不**要求本轮卸 Adsterra。 |
| **风险** | 模板未替换 → 可信度减分；过长法律文干扰攻略权重（控制短页）。**非**流量银弹。 |
| **Owner** | 远程控制（实现）· Researchy（事实闸）· PM 验收 |

### P0-2 — 核心 guides/codes 加 **FAQPage JSON-LD**（与可见 FAQ 同步）

| | |
|--|--|
| **为何** | SEO43 Schema + Perplexity「文末 ≥3 FAQ」+ AI五步骨架 FAQ；采样 **FAQPage=0 / ld+json=0**（Anime/Loot/Fish）。 |
| **验收** | 优先：how-to-redeem、codes、1–2 条最高价值 guide（每站）；合法 `FAQPage` JSON-LD；可见 Q/A 与 JSON-LD **一致**；FAQ 无 Working 声称、无未引证掉率。 |
| **风险** | 只写 schema 无可见 FAQ → 垃圾标记；FAQ 发明机制 → 事实闸 FAIL。 |
| **Owner** | 远程控制 · Researchy（事实闸）· 长脑子了（可选 GSC/Rich Results 抽检） |

### P0-3 — **≤150 字直答**（Quick Answer / TL;DR）硬化到 Snippet 规格

| | |
|--|--|
| **为何** | Perplexity 抢 Snippet：开头 ≤150 字完整答意图；AI五步 TL;DR；SEO43「答案短句直给」。现网已有 Quick Answer 痕迹，需对齐字数与「先答案后展开」。 |
| **验收** | 变更页首段/Quick Answer：**可见文字 ≤150 字**完整答主意图；后接列表/步骤/表；事实可引证或标 unofficial；Codes 页直答不得暗示已核验 Working。 |
| **风险** | 空话凑字；未证实奖励写进直答 → FAIL。 |
| **Owner** | Researchy（事实）· Copy Humanizer（可选）· 远程控制（落页） |

### P0-4 — **sitemap / robots 对齐 + GSC 提交状态闭环**

| | |
|--|--|
| **为何** | SEO43 地基；Perplexity 收尾对照 GSC。Anime：Domain sitemap processed · discovered 20（与公开 `sitemap-0` 20 loc 一致）。Loot robots→index→`sitemap.xml`（14）；Fish robots→`sitemap.xml`（15，含 privacy）。 |
| **验收** | 有价值部署后 sitemap `lastmod` 仅改触达 URL（禁空刷）；robots `Sitemap:` 指向可 200 的 index/urlset；**长脑子了**贴 Loot/Fish GSC「processed + discovered N」（**待长脑子了补**）；Researchy 用公开 loc 交叉核，**不**把 discovered 当 clicks。 |
| **风险** | 误把 sitemap 成功当流量；Loot/Fish GSC 未提交则索引慢——运维缺口非内容。 |
| **Owner** | 远程控制（对齐）· 长脑子了（GSC 只交真实 200 / 贴状态） |

### P0-5 — **情境内链**（hub↔codes↔guides，修孤立意图）

| | |
|--|--|
| **为何** | SEO43 内链/孤立页；Freshener Stage04 contextual links。 |
| **验收** | 每张变更 guide：≥2 条相关情境链（codes / hub / 兄弟 guide）；无跨站错链；无 rbxcdn。 |
| **风险** | 页脚堆链或同义词互链蚕食；价值滤不过 → skip。 |
| **Owner** | Researchy（开票）· 远程控制（实现）· 双闸 |

### P1-6 — About + Contact（三站）

| | |
|--|--|
| **为何** | AdSense五要素；信任架构。现网三站 about/contact **404**。 |
| **验收** | `/about/`、`/contact/` 200；底部可点；真实用途 + 可用邮箱；不伪称官方 Roblox。 |
| **风险** | 与 Privacy 同轮塞太多政策页稀释 Fresh 配额 → **P0 Privacy 先，About/Contact 下一票**。申 AdSense 前须卸竞品广告（与「不换 Adsterra」冲突时：**延后申 AdSense**）。 |
| **Owner** | 远程控制 · PM |

### P1-7 — 内容加厚（仍受 72h value filter）

| | |
|--|--|
| **为何** | AI五步/Perplexity：对比表、how-to、更新日；SEO43 刷新热门。 |
| **验收** | 有 cite 的 codes/mechanics 或 GSC gap；双闸 PASS；禁止 Working。 |
| **风险** | 无票硬写 = 否决。 |
| **Owner** | Researchy · 远程控制 · 双闸 |

### P2 / 可选 — `llms.txt`

| | |
|--|--|
| **为何** | SEO43 #43；成本低、采用率作者称低。 |
| **验收** | 根路径可取；指向主要 guides；无虚假声明。 |
| **风险** | 预期收益弱；勿挤掉 P0。 |
| **Owner** | 远程控制（可选） |

### 明确不进 Fresh（或需 Keith 另开）

- Reddit/站外推 → Growth，需明示授权  
- 换广告网络 / Popunder / SmartLink  
- ludusdex、发明 CCU、空 lastmod  
- Ahrefs KD（本桌无一手；选题用 Trends/YT/Reddit/GSC）

### Day14 基线侧（可核 · Researchy 表）

| Site | 公开 sitemap | loc 数 | Privacy | GSC |
|---|---|---:|---|---|
| **Anime** animedice.top | index→`sitemap.xml`→`sitemap-0.xml`（robots: `sitemap-index.xml`） | **20** | **404** | Domain `sc-domain:animedice.top`：**Sitemap index processed successfully** · discovered **20** · last read **2026-10-02**（长脑子了 22:05 CST） |
| **Loot** loot2forge.top | robots→`sitemap-index.xml`→`sitemap.xml` | **14** | **404** | **待长脑子了补** |
| **Fish** robloxfish.top | robots→`sitemap.xml` | **15**（含 `/privacy/`） | **200** | **待长脑子了补** |

补充：采样 guides 多有 Quick Answer；Fish Ghostfinn 另有 TL;DR；采样页无 FAQPage JSON-LD。Day14 判据用 **GSC Performance（impressions/clicks/queries）** + 收录/覆盖；**禁止**用 sitemap processed/discovered 代替流量结论。

## 6. 早期推流（Researchy §3）

### 能做

1. **把站做成可索引、可引用**：P0 Privacy（Anime/Loot）+ FAQPage + ≤150 直答 + 情境内链 + sitemap/GSC 闭环。  
2. **72h Fresh 有价值才上**（Routine 双闸后 Upload；空票 skip）。  
3. **需求信号**：Google Trends / YouTube / Reddit / GSC（有数才判）。  
4. **索引卫生**：长脑子了按需提交/复核 sitemap；修 404（如 privacy）。  
5. **保留 AdSense 选项**：政策页齐、广告位不抢内容；申 AdSense 前再议是否临时卸 Adsterra。

### 不做

1. **不拿 sitemap「processed / discovered」当流量或 Day14 过线。**  
2. 不买量/不刷点击；不硬广 Reddit（无授权）。  
3. 不为「显得活」空刷 lastmod / 同义改写。  
4. 不标未核验 Working；不用 ludusdex。  
5. 不把「过审作者经验数字」写成 Google 官方保证。  
6. 不在白皮书里承诺排名 / Featured Snippet / AI 提名。

## 7. Playbook Skill 摘要

完整正文见 **附录 A**。要点：

| 段 | 内容 |
|----|------|
| **§A Select** | 七鹿 Must M1–M8；一站一图；锁 Place/Universe |
| **§B Intent→结构** | Home / Codes(全字段) / ≥3 Guides / ≥1 任务工具 / About·Privacy / sitemap+robots+canonical+OG |
| **§C Keywords** | seed + SERP + Suggest + YT 标题；≤30 优先词；一词一主 URL |
| **§D YT Content Gen** | 有字幕视频 → 转写分析 → SEO skeleton → 非洗稿 → 落 `.tsx` |
| **§E Art/media** | 实机图 / embed 配额 / 禁「纯 CSS 空壳」过 content gate |
| **§F Ship** | 静态导出 → CF Pages Direct Upload → GSC（长脑子了 1:1） |
| **§G Accept** | **Day0** 内容闸 · **Day7** 产线+GSC · **Day14** impressions>0 · **Day30** continue/kill |

角色：PM 闸日历；Researchy 事实与词；远程控制仓与构建；UI 装潢视觉；长脑子了 GSC+Notion；Copy Humanizer 在事实锁后可选润色。

---

## 8. Freshener Skill 摘要

完整正文见 **附录 B**。要点：

- **周期**：每站关键词 delta **72h**（可错开）。
- **价值过滤**：硬条件 ≥1（新 codes/机制带 cite、GSC gap+缺 TL;DR/FAQ、长尾薄页、技术债）；任一 veto（同义改写、只刷 lastmod、无核验 Working、rbxcdn、广告位回退）→ 否决。
- **空票 → skip**，不计有价值部署。
- **双闸后**：Keith 授权下 **72h Routine 可 auto Upload**；长脑子了仍不碰 gated zip。
- **非目标**：不 fork H5/R2、不用 ludusdex、不无闸 Upload。

---

## 9. 双轨用法

| 轨 | 何时用 | 产出 | 闸 |
|----|--------|------|-----|
| **Fresh**（Freshener） | 已上线三站的定期加厚 / 修债 | keyword-delta → change ticket → 最小 diff zip | 双闸 → Routine 可 auto Upload |
| **Playbook** | 新站 / 把薄站拉到 Day0 content PASS | §A–G 全流水线 + YT 工厂 | Day0/7/14/30 |
| **Soft 截图轨** | 清坏图 / Soft 工单（如 Anime Soft `27efab43`） | Screenshot 清理与替换 | UI 视觉闸；不替代 Fresh/Playbook 内容闸 |

三轨不互相替代：Soft 清图 ≠ Fresh 有价值更新 ≠ Playbook 厚站验收。

---

## 10. 不要照搬

- 不要把 RB Auto 付费产品当阻塞项；只抄意图→结构→可核验源→任务工具骨架。
- 不要把 Anime Dice 试点的「薄壳+CSS」当成功范本；site 2+ 必须跑满 §D。
- 不要把 ludusdex / H5 scrape / R2 托管抄进本房间流水线。
- 不要把「交了 sitemap」当成「有了流量」。
- 不要在无 Researchy 事实闸时把 AI Codes 标 Working。
- 不要让长脑子了碰 Upload / gated zip（角色锁）。

---

## 11. 源链接

| 资源 | URL |
|------|-----|
| Notion Hub | https://www.notion.so/3edb35b6a57f81dca7a3ef16b20a37bd |
| Freshener Skill | https://www.notion.so/3edb35b6a57f812abd7cd191af48a18a |
| Playbook Skill | https://www.notion.so/3ecb35b6a57f817695d1e48d33ce23a0 |
| Researchy Fresh 输入（附录 C） | `/workspace/roblox-map-seo-ads/fresh-optimal-plan-researchy-2026-10-02.md` |

本地 Skill 路径：

- Playbook：`/home/box/agent-data/workflows/roblox-seo-site-playbook/SKILL.md`
- Freshener：`/home/box/agent-data/workflows/roblox-seo-site-freshener/SKILL.md`

---

## 12. 附录 A · Playbook 全文

```markdown
---
name: Roblox Map SEO Ads
description: >-
  use this when running or thickening Keith’s Roblox Map SEO Ads play (map heat
  → Google SEO guide sites → on-site ads), including Anime Dice and Loot To
  Forge—follow the full private pipeline, not a thin CSS shell
---
# Roblox Map SEO Ads (private playbook)

**Canonical name:** Roblox Map SEO Ads  
Method: Roblox map heat → Google SEO guide sites → on-site ads.

**Notion Skill (keep in sync):** https://app.notion.com/p/3ecb35b6a57f817695d1e48d33ce23a0

Reusable method distilled from Anime Dice pilot + 七鹿 (RBauto V8 methodology, not the paid product) + YouTube Content Gen. **Second site and later sites must run this end-to-end.** First site (Anime Dice) only partially followed it; thicken using §D–E.

## Sources of truth (Notion Linked)
- Project: Roblox Map SEO Ads — `https://app.notion.com/p/3ebb35b6a57f80ba8651f68c94c605a9`
- Notion Agent-Skills page — `https://app.notion.com/p/3ecb35b6a57f817695d1e48d33ce23a0`
- 30-day plan: `https://app.notion.com/p/3ecb35b6a57f815d9650d3882df7e41a`
- RBauto V8 guide (method skeleton): `https://app.notion.com/p/3ebb35b6a57f8179ab4ec55cc7fcb77c`
- YouTube Content Gen: `https://app.notion.com/p/3ecb35b6a57f812da911c1b573f9b100` · GitHub `kennyzir/7deer_skills/youtube-content-gen`
- 七鹿选图框: `https://app.notion.com/p/3ecb35b6a57f81aa92a3df7f74deda22`
- CDN guides under `https://cdn.jsdelivr.net/gh/keithhegit/piclist-cdn@master/changnaozi/`

**Do not require buying RB Auto.** Copy the skeleton: intent → page structure → verifiable sources → task-type tool. Open-source YT skill is the content supply; paid product is optional later.

## Roles
| Role | Owns |
|------|------|
| Projects Manager | Gate Day0/7/14/30; Notion Tasks; force skill checklist |
| Researchy | Select game; keyword map; Codes with sources; SERP gaps; YT video shortlist with license notes |
| 远程控制 | Repo, Cursor CLI build, integrate youtube-content-gen or equivalent, deploy artifacts |
| UI装潢 | Guide-site visual system; image/video slots; QA after deploy |
| 长脑子了 | CF Pages Direct Upload; walk Keith GSC; Linked Resources |
| Copy Humanizer | Humanize drafts after facts locked |

## Pipeline (mandatory for site 2+)

### A. Select (七鹿 Must)
1. Fill Must M1–M8 checklist; Avoid list.
2. Prefer data-dense games (forge/enhance/tier/codes) with open SERP window.
3. Lock Place + Universe IDs; one game per site; no parallel Anime-Breaker-with-Anime-Dice style cannibalization.

### B. Intent → structure (RBauto V8 skeleton)
Minimum pages before claiming “content ready”:
1. Home (Top1 intent above the fold)
2. Codes (every row: code, source_url, verified_at, verifier, status; **unverified never in Working**)
3. ≥3 Guides mapped to real player jobs (not generic FAQ fluff)
4. ≥1 task tool (planner/compare/enhance table)—inputs/outputs clear; no RNG prediction
5. Sources / About / Privacy; ad slots reserved, not competing with content
6. sitemap.xml + robots Sitemap line + canonical + OG

### C. Keywords
1. Seed: `{game} codes|wiki|guide|tier|builds|calculator|values|forge|enhance|…`
2. SERP + Suggest + **YouTube titles** for long tails (≤30 priority terms)
3. One primary URL per term; map to page types in §B

### D. YouTube Content Gen (mandatory content supply)
For each priority long-tail / guide page:
1. Find videos **with captions**; skip no-caption.
2. Extract transcript → structured analysis (type, player question, steps, FAQ candidates, uncertain facts).
3. Generate SEO skeleton: Title, slug, meta, Quick Answer, sections, FAQ, embed, OG, schema, WebP thumb.
4. **Non-spin check**: embed source video; cite sources; second-source or self-test facts; reorganize for scan-reading—not paraphrase-the-script.
5. Write `.tsx` (or site stack equivalent) into the repo; no orphan Markdown-only dumps.
6. Researchy gates facts; Copy Humanizer optional after gate.

Open-source path: adapt `youtube-content-gen` to brand/domain/categories; do not invent items/NPCs/maps without transcript evidence.

### E. Art / media
- Prefer real in-game screenshots / map stills with attribution rules Researchy lists.
- YouTube embeds per UI slot quotas; lazy-load / facade.
- Pure CSS “pretty empty” is a fail for content gate.

### F. Ship
1. Build static export (or agreed stack) → shared out path on box.
2. CF Pages project per site; Direct Upload if API token flaky.
3. Keith GSC verify + submit sitemap (长脑子了 1:1).
4. Codes stay unverified until human/bot recheck with source.

### G. Accept gates
- **Day0 content gate**: §B pages live locally; ≥N YT-backed guide pages (default **5** for site 2; Anime Dice thicken toward this); Codes 100% sourced fields; tool page clickable.
- **Day7**: prod URL + sitemap/robots + GSC property + sitemap submit.
- **Day14**: GSC impressions > 0 sitewide; ≥1 Codes recheck log.
- **Day30**: continue/kill writeup; impressions threshold from plan (tunable).

## Anime Dice (site 1) gap — do before calling “thick”
Pilot shipped skeleton Codes + thin guides + CSS polish; **did not** run full youtube-content-gen factory or V8 task-tool density. Remediation:
1. Researchy: priority keywords + captioned YT list for Anime Dice.
2. 远程控制: run/adapt youtube-content-gen → add pages; keep Codes rules.
3. UI装潢: image/video slots QA.
4. 长脑子了: redeploy; GSC already on track—don’t reset Day14 calendar.

## Site 2 (Loot To Forge) hard rules
- Must complete §A–G before Day7 content PASS.
- Empty shell OK for engineering start; **content PASS requires §D**.
- Place `118805555015549` · Universe `10684750879` unless Researchy re-locks.

## Anti-patterns
- Buying RB Auto as a blocker
- AI codes with no source_url
- FAQ walls with no transcript/wiki evidence
- Matrix of thin sites before one thick site proves GSC
- Declaring UI PASS when pages lack media + YT-backed depth
```

---

## 13. 附录 B · Freshener 全文

```markdown
---
name: roblox-seo-site-freshener
description: >-
  use this when running Sprint-Fresh-1 or refreshing Keith’s three Roblox SEO
  guide sites (Anime Dice / Loot / Fish): map 七鹿 roblox-site-architect stages
  into the room pipeline—keyword delta → value filter → gated zip → dual gate →
  Upload—without forking H5/R2 stacks
---
# roblox-seo-site-freshener

Room Skill for **Sprint-Fresh-1+**: keep [animedice.top](https://animedice.top) / [loot2forge.top](https://loot2forge.top) / [robloxfish.top](https://robloxfish.top) fresh with **valuable** updates only.

**Notion Resource (canonical):** https://www.notion.so/3edb35b6a57f812abd7cd191af48a18a  
**Notion draft:** https://www.notion.so/3edb35b6a57f816a9d2fc8f254c6adad  
**Hub:** https://www.notion.so/3edb35b6a57f81dca7a3ef16b20a37bd  
**Upstream (read, don’t fork):** https://github.com/kennyzir/7deer_skills/tree/main/roblox-site-architect  
**Parallel playbook Skill:** https://www.notion.so/3ecb35b6a57f817695d1e48d33ce23a0

## Locked decisions (2026-10-02)
- Pilot: **all three sites** together
- Keyword cadence: **72h** per site (stagger OK)
- Encode + gated zip: **远程控制** only
- Human approval = **双闸** (Researchy事实 + UI视觉)
- **Routine exception (Keith):** after dual-gate PASS, **72h Routine may auto Upload**; empty tickets → **skip** (no deploy)
- **Do not** steal H5 scrape / wash / R2 game hosting
- ludusdex weekly: **stale — do not use**; Trends / YouTube / Reddit / GSC only

## Architect Stage → room mapping

| Architect stage | Artifact idea | Room owner | Our action |
|---|---|---|---|
| 01 Opportunity | pursue/hold/reject | Researchy + Keith | Only when **new game/site**; skip for routine thicken of existing three |
| 02 Keywords | keyword-delta | Researchy | Every **72h**: Trends + YT + Reddit + GSC → `02-keyword-delta.md` per site |
| 03 Evidence | change ticket | Researchy | Value filter → `03-change-ticket.md` with URL + excerpt + `observed_at` |
| 04 Site plan/build | IA + local impl | 远程控制 | Min diff in **existing** CF Pages repos; TL;DR + FAQ(q/a) + contextual links |
| 05 SEO QA / deploy | audit + release | 远程控制 + 双闸 | gated zip → dual PASS → Upload (Routine OK) → UUID; 长脑子了 GSC only if asked |
| 06 Freshness | freshness log | PM + 长脑子了(GSC) | `06-freshness.md`: last **valuable** deploy, next crawl, open tickets |
| 07 Growth | backlog | PM + Keith | After MVP; outreach needs explicit auth |

Status vocabulary: `complete` / `partial` / `blocked`. Never claim deploy/send/schedule without a real result.

## Value filter (before dual gate)

**Hard (need ≥1):** new codes/mechanics with cite; GSC gap + missing TL;DR/FAQ; proven long-tail with no/thin page; tech debt (404/orphan/sitemap miss).

**Veto (any):** synonym-only rewrite; lastmod bump only; Working without in-game redeem; rbxcdn; ad-slot regression.

Empty refreshes / empty tickets → **skip** (do not count as valuable deploys).

## Runbook (one Fresh cycle)
1. Researchy: 72h delta for all three sites → tickets or skip
2. 远程控制: implement tickets → `*-gated-<BUILD>.zip` + change summary
3. Researchy事实 PASS + UI视觉 PASS
4. Upload (manual or **Keith 72h Routine** after dual PASS) → live spot
5. PM close; update hub 现状 one line
6. Optional: 长脑子了 GSC sitemap recheck

## Explicit non-goals
- Forking roblox-site-architect into a one-click site generator
- Feishu/Hermes wholesale; room bots are the orchestrators
- Upload without dual-gate PASS; empty-ticket deploys
- 长脑子了 touching gated zips
```

## 14. 附录 C · Researchy Fresh 最优落地优先级全文

> 源路径：`/workspace/roblox-map-seo-ads/fresh-optimal-plan-researchy-2026-10-02.md`  
> Observed_at: 2026-10-02 ~22:10 CST · 事实核验侧输入（已并入 §5 / §6）

```markdown
# Researchy → 长脑子了：三站 Fresh 最优落地优先级（白皮书输入）

**Observed_at:** 2026-10-02 ~22:10 CST (Asia/Shanghai)  
**Role:** 事实核验侧输入（非白皮书终稿）  
**Hard rules (locked):** 不换 Adsterra 单元形态（Native + Banner 300×250 only）；Codes 永不标 Working/未局内核验；禁 ludusdex；无发明 CCU/点击；空票 skip。

**Method sources consulted (Linked / CDN):**
- SEO43：`changnaozi/20261002-seo43-checklist` + Notion `3edb35b6a57f815e959df5accf16d95f`
- AI标准答案五步：`changnaozi/20261002-reddit-ai-seo5`
- Perplexity四步：`changnaozi/20261002-perplexity-seo4`
- AdSense过审五要素：Notion `3edb35b6a57f8184be2bee9c6b3a4097` / CDN `20261002-adsense-5fixes`
- Freshener Skill：`roblox-seo-site-freshener`（72h delta → ticket → dual gate → Upload）

**Live public probes (this desk, 2026-10-02):** FAQPage/`application/ld+json` = **0** on sampled codes+guides (Anime/Loot/Fish). Privacy **200** only on Fish; Anime/Loot privacy **404**. About/Contact **404** all three. Guide pages often have **Quick Answer** (Fish Ghostfinn also TL;DR). Sitemap URL counts: Anime `sitemap-0.xml` **20** loc · Loot `sitemap.xml` **14** · Fish `sitemap.xml` **15**.

---

## 1) Fresh 72h 最优落地优先级（每条：为何 / 验收 / 风险）

> 排序原则：先补「可核验缺口 + 过审/AI 可抽取地基」，再做内容加厚；仍走 value filter（≥1 hard 信号）；空票 skip。

### P0-1 — Anime + Loot `/privacy/`（Fish 已有）+ 页脚可点
| | |
|---|---|
| **为何** | AdSense五要素第一大漏项；SEO43「像正经站」；总案保留 AdSense 选项且**不换**现网 Adsterra。Fish 已 200，Anime/Loot 公开 404（本轮 curl）。 |
| **验收** | `https://{anime,loot}/privacy/` → 200；页脚有 Privacy 链接；文内无 `[Company]`/`[Email]` 占位；写明 cookies/ads（含 Adsterra）与联系邮箱；**不**要求本轮卸 Adsterra。 |
| **风险** | 模板照搬未替换 → 可信度减分；过长法律文干扰攻略权重（控制短页）。**非**流量银弹。 |

### P0-2 — 核心 guides/codes 加 **FAQPage JSON-LD**（与可见 FAQ 同步）
| | |
|---|---|
| **为何** | SEO43 Schema（项≈22）+ Perplexity「文末 ≥3 FAQ」+ AI五步骨架 FAQ；本轮采样 **FAQPage=0 / ld+json=0**。 |
| **验收** | 优先：how-to-redeem、codes、1–2 条最高价值 guide（每站）；HTML 含合法 `FAQPage` JSON-LD；页面可见 Q/A 与 JSON-LD **一致**；FAQ 答案无 Working 声称、无未引证掉率。 |
| **风险** | 只写 schema 无可见 FAQ → 垃圾标记风险；FAQ 发明机制 → 事实闸 FAIL。 |

### P0-3 — **≤150 字直答**（Quick Answer / TL;DR）硬化到 Snippet 规格
| | |
|---|---|
| **为何** | Perplexity 抢 Snippet：开头 ≤150 字完整答意图；AI五步 TL;DR；SEO43「答案短句直给」。现网已有 Quick Answer 痕迹，需对齐字数与「先答案后展开」。 |
| **验收** | 变更页首段/Quick Answer：**可见文字 ≤150 字**完整答主意图；后接列表/步骤/表；事实可引证或标 unofficial；Codes 页直答不得暗示已核验 Working。 |
| **风险** | 为凑字数写空话；或把未证实奖励写进直答 → FAIL。 |

### P0-4 — **sitemap / robots 对齐 + GSC 提交状态闭环**
| | |
|---|---|
| **为何** | SEO43 地基（sitemap+robots）；Perplexity 收尾对照 GSC。Anime：GSC Domain 已报 **Sitemap index processed · discovered 20**（与公开 `sitemap-0` 20 loc 一致）。Loot robots→`sitemap-index.xml`→`sitemap.xml`（14）；Fish robots→`sitemap.xml`（15，含 privacy）。 |
| **验收** | 有价值部署后 sitemap `lastmod` 仅改触达 URL（禁空刷）；robots `Sitemap:` 指向可 200 的 index/urlset；**长脑子了**贴 Loot/Fish GSC 同等「processed + discovered N」截图/数；Researchy 用公开 loc 数交叉核，**不**把 discovered 当 clicks。 |
| **风险** | 误把 sitemap 成功当流量；Loot/Fish GSC 未提交则索引慢——属运维缺口非内容。 |

### P0-5 — **情境内链**（hub↔codes↔guides，修孤立意图）
| | |
|---|---|
| **为何** | SEO43 内链/孤立页（≈32–34）；Freshener Stage04「contextual links」。 |
| **验收** | 每张变更 guide：≥2 条相关情境链（codes / hub / 兄弟 guide）；无跨站错链（Anime≠Loot≠Fish）；无 rbxcdn。 |
| **风险** | 页脚堆链或同义词互链蚕食；价值滤不过 → skip。 |

### P1-6 — About + Contact（三站）
| | |
|---|---|
| **为何** | AdSense五要素；信任架构。现网三站 about/contact **404**。 |
| **验收** | `/about/`、`/contact/` 200；底部可点；真实用途说明 + 可用邮箱；不伪称官方 Roblox。 |
| **风险** | 与 Privacy 同轮塞太多「政策页」稀释攻略 Fresh 配额——可 **P0 Privacy 先，About/Contact 下一票**。申请 AdSense 前须卸竞品广告（与「不换 Adsterra」冲突时：**延后申 AdSense**，先养站）。 |

### P1-7 — 内容加厚（仍受 72h value filter）
| | |
|---|---|
| **为何** | AI五步/Perplexity：对比表、how-to、更新日；SEO43 刷新热门。 |
| **验收** | 有 cite 的 codes/mechanics 或 GSC gap；双闸 PASS；禁止 Working。 |
| **风险** | 无票硬写 = 否决。 |

### P2 / 可选 — `llms.txt`
| | |
|---|---|
| **为何** | SEO43 #43；成本低、采用率作者称低。 |
| **验收** | 根路径可取；指向主要 guides；无虚假声明。 |
| **风险** | 预期收益弱；勿挤掉 P0。 |

### 明确不进 Fresh（或需 Keith 另开）
- Reddit/站外推（AI五步第4步）→ Growth，需明示授权  
- 换广告网络 / Popunder / SmartLink  
- ludusdex、发明 CCU、空 lastmod  
- Ahrefs KD 数字（本桌无一手 Ahrefs；选题用 Trends/YT/Reddit/GSC）

---

## 2) Day14 基线侧（可核）

| Site | 公开 sitemap | loc 数 | Privacy | GSC（本桌已知） |
|---|---|---:|---|---|
| **Anime** animedice.top | index→`sitemap.xml`→`sitemap-0.xml`（robots: `sitemap-index.xml`） | **20** | **404** | Domain `sc-domain:animedice.top`：**Sitemap index processed successfully** · discovered **20** · last read **2026-10-02**（长脑子了 22:05 CST 报） |
| **Loot** loot2forge.top | robots→`sitemap-index.xml`→`sitemap.xml` | **14** | **404** | **未见**本桌一手 GSC 状态；请长脑子了贴 processed/discovered |
| **Fish** robloxfish.top | robots→`sitemap.xml` | **15**（含 `/privacy/`） | **200** | **未见**本桌一手 GSC 状态；请贴同等状态 |

补充（结构，非流量）：
- 采样 guides 多有 **Quick Answer**；Fish Ghostfinn 另有 **TL;DR**。
- 采样页 **无** FAQPage JSON-LD。
- Soft 已清 Anime quests / how-to-redeem Screenshot pending（SVG soft）；不计入 sitemap=流量。

Day14 判据提醒：用 **GSC Performance（impressions/clicks/queries）** + 收录/覆盖；**禁止**用 sitemap processed / discovered 代替流量结论。

---

## 3) 早期推流：能做 / 不做

### 能做
1. **把站做成可索引、可引用**：P0 Privacy（Anime/Loot）+ FAQPage + ≤150 直答 + 情境内链 + sitemap/GSC 闭环。  
2. **72h Fresh 有价值才上**（Routine 双闸后 Upload；空票 skip）。  
3. **需求信号**：Google Trends / YouTube / Reddit / GSC（有数才判）。  
4. **索引卫生**：长脑子了按需提交/复核 sitemap；修 404（如 privacy）。  
5. **保留 AdSense 选项**：政策页齐、广告位不抢内容；申 AdSense 前再议是否临时卸 Adsterra。

### 不做
1. **不拿 sitemap「processed / discovered」当流量或 Day14 过线。**  
2. 不买量/不刷点击；不硬广 Reddit（无授权）。  
3. 不为「显得活」空刷 lastmod / 同义改写。  
4. 不标未核验 Working；不用 ludusdex。  
5. 不把「过审作者经验数字」写成 Google 官方保证。  
6. 不在白皮书里承诺排名/ Featured Snippet / AI 提名。

---

## 给白皮书的一句话结论

**下一轮 Fresh 最优包 =「合规信任页（Anime/Loot Privacy）+ AI/Snippet 可抽取层（FAQPage JSON-LD + ≤150 直答）+ 索引闭环（sitemap/GSC）+ 情境内链」；内容加厚仍跟 72h value filter。推流靠可索引可引用的结构与真实需求信号，不靠 sitemap 成功态。**
```

---

*完 · 长脑子了 · 2026-10-02 CST*
