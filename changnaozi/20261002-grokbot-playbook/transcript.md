# 逐字稿 / 结构化摘录 · Grok Bot 玩法全景手册

- 源 URL：https://grokbot.aihuangshu.com
- 站名：Grok Bot 玩法全景手册 · 橙皮书 × Awesome 清单合并版
- 抓取日：2026-10-02（CST）
- 说明：网页长文；以下为校对级结构化摘录（保留关键原话与表格要点）。完整案例库以原站为准。账号剪辑 vs 官方口径已在条目标注。

## Meta

这本手册由 Grok Bot 自己盯、自己改、自己发，偷懒会被自己抓。  
点选场景，直达第08章同类案例。  
今日更新 · 2026-09-27 · Global 现场

### 今日更新七条（摘要）

1. Finance 理财插件经 Plaid 只读连 Revolut；xAI 不保存银行登录。@techdevnotes  
2. 「総務マン」卡在验证码，把电脑交给人 Verify 后继续取消宿舍（US$45 手续费为作者自述）。@GOROman  
3. 蚊取り線香予報Bot：一句话把指数换成图标，Routine 当场更新。@tomo_klotho  
4. Ticket Snagger 订挪威餐厅，成功页截回聊天（确认靠短信邮件）。@KevinMThorsen  
5. Degen 新建盯币 Routine「Zoo Corner watch」（非投资建议）。@0x3Matt  
6. 博客标题 Cron → cron，PR #1028 已合入 release，未证明已上线。@fumokmm  
7. Rona Manager 挑对口型最差三段交给剪映。@NancyKim294702  

## 产品本质（官方 + 橙皮书）

一句话定义（橙皮书序章）：  
「Grok Bot 是 xAI 与 Cursor 联合推出的云端多智能体办公平台。每个 Bot 拥有自己的云端电脑，用『像人一样操作界面』的方式登录你授权的应用和网站干活；你合上电脑、关掉手机，它们继续上班。」

官方三句（手册引用）：  
1. Bots are AI teammates that do real work for you…  
2. A chief of staff sits on top, with a specialist for each lane…  
3. They pass work, assign ownership, and only pull you in for judgment calls.

三大原则：记忆 / 协作 / 学习。  
代差：云端常驻（雇佣 vs 借用）+ 群体分工（分工 vs 全能）。  
安全：Bots are not a security boundary（隔离按账号不按 Bot）。

### Grok vs Grok Bot

| | Grok | Grok Bot |
|---|---|---|
| 是什么 | 聊天助手 | AI 工作团队 |
| 怎么用 | 提问 | 派活 |
| 在哪 | 对话框 | 云端虚拟机 |
| 交付 | 一段话 | 一个结果 |

## 上手 · 价格 · 第一活

扩权节点：2026-08-21 起 SuperGrok Plus / Cursor Pro+ / Teams + 限量免费试用（社区约 7 天）。  
个人最低付费档：Cursor Pro $20（8-26 起含 Grok Bot，见冲突二）。  
选型：个人 Pro 试水 → Pro+/Ultra 或关联 SuperGrok；团队 Teams $40/席。

大脑倾倒 → 魔法提问 → 派第一个真活（竞品监控 / 发票整理 / 选题分析）。  
心态：派完就走，你是审批者不是监工。

## 核心机制（表摘要）

建 Bot 起名定岗；总监模式；多 Bot Channels（每命名空间最多 6）；Teach ≤10 分钟；Routine；模板分享（导出 skills 曾空）；Auto-review；secret card；X / Microsoft / Teams / 1Password / Google Docs·Sheets·Slides / Finance / Team Bots / Voice·Voice notes / Cloud Agent 写码 / 工程模板市场 / 主动建议帮忙 等——以原站机制表与日期线为准（更新至 2026-10-01）。

## 多智能体

总监模式：所有任务丢给 CoS。  
官方 Bug 旅程：复现岗 → 工单 → 修复岗。  
五人舰队模板（Alex Finn 等转述）：Build / Barry / Dusty / Cindy / Reed；本土化需换信息源。  
扩编：一周一个新员工；每周 15 分钟三问复盘。

## Routine

适合步骤固定、判断少；不适合临场谈判。  
示范前四问：自己跑熟两次？可写成如果…就…？暗知识补进记忆？前三次人工核对？

## Auto-review

触发：支付 / 敏感 / 不确定。  
错误两端：什么都审 vs 什么都不看。  
低风险批量授权；碰钱逐张看。

## 省钱与无人值守

六吞金兽：重复交代背景、高薪干杂活、失败尝试、无意义轮询、无限连聊、杀鸡用牛车。  
无人值守三形态：哨兵 / 流水线 / 夜班。  
质控：验收前置、抽样复核、异常上报通道。

## 限制与坑（摘）

无本地 MCP；无 Compact；Bot 无 codebase 插件；周额度溢出无警告；Update Computer 重建镜像；模板 skills:[]；多插件 OAuth 故障史。

## 来源

- 《Grok Bot 橙皮书》Kin · v260823 · github.com/KinGao294/grok-bot-orange-book  
- Awesome / usegrokbot.com 玩法提示词  
- 界面截图：Flavio Copes 等（学习用途）  

## 冲突点状态（手册自标）

已解决：Linux 桌面、Cursor Pro 含 Bot、Android、iPad（docs 已跟上；Cursor 帮助 mobile 仍可能滞后）。  
仍注意：Teams 价格表述、Enterprise rolling out vs Cursor「问客户经理」。
