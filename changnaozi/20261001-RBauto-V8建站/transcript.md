# RBauto V8：Roblox 游戏站搜索意图驱动自动化建站 - 微信公众号

> **微信条目**：七鹿AI（作者署名：七只路）·《roblox 自动化建站一气呵成了》
> **原推文标题**：roblox 自动化建站一气呵成了
> **源 URL**：https://mp.weixin.qq.com/s/5SW3KyzFJ7a7jyyTgAay6w
> **公众号**：七鹿AI（alias: qiluai_；biz: MjM5OTEyNTM3NA==；user_name: gh_7fc663d26b87）
> **发布时间**：2026-09-13 21:45 CST（页面 ct=1789307146；Asia/Shanghai）
> **合集**：游戏出海（album_id=3957145241999638536）
> **体裁**：微信新图文（item_show_type=8 / appmsg_type=9）——正文为分享文案 + 4 张产品截图轮播；非经典 rich_media HTML 长文。
> **校对说明**：curl 拉取 mp.weixin.qq.com HTML，自 `content_noencode` / `og:description` / `window.desc` 抽出完整分享文案（三者一致）；自 `picture_page_info_list` 下载 4 张主图并人工识读画面文字。本稿为**公众号原文校对整理**，**非直播 ASR**。配图内英文 UI 按画面转写；价格与流量数字为文中/图中展示，**非本账号实测**。
> **校对日期**：2026-10-01 Asia/Shanghai

---

## 开篇：RBauto 迭代到 V8

最近把 Roblox 游戏站全自动化 Agent 工具迭代到了 V8 版本。

不得不说，是真强，基本一次成型，效果真不错，SEO 抢排名的能力又强了一点。

这个版本核心解决的是**内容单薄**的问题。

---

## 痛点：关键词有了，内容却无法满足搜索意图

做过 Roblox 游戏站的兄弟，很容易遇到一个问题：关键词找了一堆，页面也生成了不少，但内容都是泛泛介绍，玩家看完依然不知道怎么操作，完全无法满足用户搜索意图。只能靠后续不断手动加词优化页面内容，手疼。

这个版本把**研究和内容生产串起来**，从 Wiki、视频、社区中提取具体数值、操作步骤和适用条件，再对应到玩家的问题。通过一系列具体的流程约束和规范，让 AI 照着流程走。总算能做到每个内页都能聚焦一个关键词，并提供详实的答案了。

再就是，这次总算是优化出了能适配不同游戏的版本。

---

## 首页搜索意图设计引擎

另一个重点，Roblox 游戏品类太多，之前的 Agent 搞出来的站首页首屏都是千篇一律的 wiki guide。这个版本搞了个**首页搜索意图设计引擎**。

先判断玩家搜这个游戏最想解决什么，再决定首页放哪些内容、怎么排序、哪些直接回答、哪些需要工具或深入攻略承接。每个游戏的首页，都跟着它的实际需求走。

---

## 案例站：AnimeDice.org

拿 Anime Dice 案例站来说，一次成型，大家可以看看成品站效果：**AnimeDice.org**

首页围绕「下一颗骰子怎么买、什么时候买」展开。输入当前现金、每秒收入和目标骰子，就能算出还差多少钱、需要等多久，还能比较：先升级角色增加收入，会不会更快攒够钱？

围绕后续需求，再承接角色养成、Trait／Grade 重洗概率、重生回本时间等内容。玩家从首页进入，就有一条清楚的决策路径。

---

## 开发思路（三句话）

七鹿的 RBauto 全自动化 Agent 工具的开发思路就是：

1. **用搜索意图决定网站结构**
2. **用游戏资料做实内容**
3. **用玩家能否完成任务来验收**

让一个人借助 AI 持续上站，也能把每个站的内容做扎实。

---

## 配图识读（picture_page_info_list，4 张）

> 以下按轮播顺序转写画面可见信息，补全文案未写到的产品 UI / 定价 / 流量展示。

### 图 1｜Anime Dice 案例站首页（约 2262×1290）

站点标题：**ANIME DICE: THE PLAYER GUIDE**（Roblox 游戏玩家攻略站）。

导航：Next move（高亮）/ Codes / Dice / Characters / Traits & Grades / Progression / Rebirth / Towers / Resources / Update 4；右上「Play on Roblox」。

首屏文案：

- 面包屑：ANIME DICE / PLAYER FIELD GUIDE
- 主标题：Your next **move.**
- 副文：Make every roll count. Plan your next dice, build a better team, and know when to keep what you've got.
- CTA：Plan my next dice；另有「9 reported codes →」
- 视觉：角色 + 骰子插画，条幅「ROLL. EARN. UPGRADE.»；标注「Illustrated guide artwork - edited from game promotional art」
- 更新条：UPDATE 4 IS LIVE — New units. New choices. Keep your next move informed. / Read the update notes

功能区标题 **Plan your next dice**：说明输入当前骰子、目标骰子、现金与每秒收入后，规划器给出剩余现金、显示的 Luck 增幅、以及按当前收入攒够目标所需时间；并写明 **does not predict your next pull**（不预测下一次抽取结果）。

### 图 2｜「Plan your next dice」规划器 UI（约 1423×1285）

输入示例：

| 字段 | 示例值 |
|---|---|
| Your current dice | Storm · $200M |
| Your target dice | Shadow · $1.5B |
| Cash saved | 800M（支持 K/M/B/T/Qa/QD/Qi/Sx 后缀） |
| Current income / second | 1M |
| Target price override / Target displayed Luck | 可选覆盖 |
| Upgrade cost（对比升级） | 100M |
| Extra income / second | 250K |

主按钮：**Compare my next move**；旁有 Reset example。

结果面板：

- Cash to Shadow：**$700M**
- Save directly：**11m 40s**
- Displayed Luck gain：**+87.5%**
- 摘要：Save directly in 11m 40s. Upgrade-first total: 10m 40s. **1m 0s sooner with the upgrade.** Fixed income and unchanged boosts; additional purchases and rolls excluded.

→ 对应文案里「先升级角色增加收入，会不会更快攒够钱」的产品落地。

### 图 3｜RB Auto 产品落地页（约 1605×1027）

品牌：**RB Auto**（Roblox 游戏站工具）。

导航（中文）：真实案例 / 你能得到什么 / 流量与矩阵 / 怎么使用 / 版本价格 / 关于七鹿；右上 CTA：**预约演示 →**

主文案：

- 标题：Roblox 游戏站，**不用每次从头来。**
- 副文：已经会用 AI 做站，想持续测试更多游戏？在 Codex 里用 RB Auto，研究选词、生成网站，把上线和后续运营接起来。
- 交付：**你买到: Agent 工具源码 + 操作说明 + 首站陪跑**
- 按钮：看真实案例 → / 看看具体工具
- 价格行（画面）：**个人 Plus 6 折价 $899.40 美元 · 域名与模型等费用另计**

右侧产品窗：**RB_AUTO / REAL_PROJECT_01**，预览「Anime Squadron Wiki Hub」类英文攻略站；底部三点：

1. **01 独立源码 / 留在自己的项目里**
2. **02 预览与上线 / 查看结果，再确认上线**
3. **03 数据与广告 / 接入自有平台账号**

脚注：已有站点截图 · 英文攻略与工具站。

### 图 4｜案例站搜索表现截图（约 1839×639）

搜索控制台类仪表盘（24 hours / Web；约 4 hours ago 更新）：

| 指标 | 数值 |
|---|---|
| Total clicks | **3.32K** |
| Total impressions | **18.2K** |
| Average CTR | **18.3%** |
| Average position | **4.8** |

时间轴约从 9/5 19:00 至 9/6 14:00；凌晨后点击与展示急剧抬升。文中「SEO 抢排名的能力又强了一点」的视觉佐证；**具体站点与是否含品牌词未在图中标明，引用时当作案例晒图即可**。

---

## 文末信息（页面元数据）

- 作者署名：七只路
- 公众号：七鹿AI
- 合集入口：游戏出海
- 成品案例域名（文中）：AnimeDice.org
- 产品名（图中）：RB Auto / RBauto
