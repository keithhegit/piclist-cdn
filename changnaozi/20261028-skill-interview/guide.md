# 面试里的 Agent Skill 认知：不是更长 Prompt，是可复用能力包

> 攻略摘要 · 长脑子了  
> 疑似源片：牛马AI大模型《最近面了一个特别亮眼的 agent 开发男生》（2026-10-20）  
> **无口播 ASR**；上手路径与论点主要来自题面 + 同题二次整理文（知乎/阿里云）+ Anthropic Agent Skills 规范，分层见 `transcript.md` / `SOURCES.md`。

## 一句话定位

面试官追问「Skill 怎么写 / 什么叫高质量」时，亮眼答法不是「把 Prompt 写长」，而是把**一类高频任务的专家判断、反模式、输出标准与验证闭环**沉淀成 Agent 可按需加载的能力模块（`SKILL.md` 资产）。

## 适合谁

- 在面 / 准备面 **Agent / 大模型应用 / AI 工程** 岗，怕被问穿「Skill = Prompt」  
- 已在 Cursor / Claude Code / 自建 Agent 里堆 Skill，想从「能跑」升到「可评测、可治理」  
- 做 Grok Bot / 团队 skill 库，需要统一「何时该 Skill 化」的口径  

不适合：只想要一条万能提示词、或从不维护工作流资产的人。

## 上手顺序（今天就能做）

1. **换标签（5 分钟）**  
   把口头习惯从「写个 Prompt」改成：「这是不是值得沉淀成 Skill 的一类任务？」  
   判断公式（二次文共识）：**反复出现 × 足够复杂 × 有专家判断 × 对输出质量有要求**。

2. **挑 1 个重复任务写最小 Skill（30–60 分钟）**  
   只写清 4 块即可起步：  
   - 适用 / **不适用**  
   - 步骤或决策分支  
   - 输出格式 +「什么叫做好」  
   - 失败 / 信息不足怎么办  

3. **跑一轮对照（同日）**  
   同一任务：**不加载 Skill vs 加载 Skill**，记 3 个指标：成功率、格式错误、是否乱编。  
   有对比才算工程结论，不是「感觉更好」。

4. **本周验收**  
   - 是否完成 1 份可复用 `SKILL.md`（含反模式）  
   - 面试口述能否 60 秒讲清：Skill≠更长 Prompt、与 Tool/MCP 边界、按需加载  

## 能力表 / 核心论点

| 论点 | 要能讲清的一句话 |
| --- | --- |
| Skill ≠ 更长 Prompt | Prompt 解决**这一次**怎么说；Skill 解决**这一类**怎么稳定做 |
| 边界比步骤更值钱 | 必须写「什么时候不该用」；否则相似任务会误召回 |
| Tool / MCP / Skill | Tool/MCP 解决「连得上、做得了」；Skill 解决「何时用、怎么用稳、输出何为合格」 |
| 渐进式披露 | 先只注入 name/description；命中后再读正文 / references（Anthropic） |
| 质量可度量 | 任务成功率、误召回、格式稳定、人工返工、Token 成本——要有 A/B |
| 安全不只写在 Skill 里 | Skill 是软提醒；权限/审批/拦截在 Harness / Tool Registry |

### 高质量 Skill 最小清单（面试可背）

1. 适用场景  
2. **不适用场景（反模式）**  
3. 输入要求  
4. 操作步骤 / 决策树  
5. 工具使用原则（勿把 schema 写死）  
6. 输出格式  
7. 质量标准（什么叫做好）  
8. 失败与信息不足处理  
9. 安全边界（并声明工程层强制）

## 可复制金句 / 口述模板

**60 秒开场（可直接背）：**

> 我不把 Skill 理解成更长的提示词，而理解成 Agent 里一类任务的可复用能力单元。它要回答：何时触发、何时不触发、按什么专家逻辑走、禁止哪些行为、输出如何验收、失败如何修正。目标不是演示样例好看，而是换输入、换会话仍稳定。

**边界一句：**

> Tool 解决能不能做，Skill 解决怎么做得更稳；MCP 是接入协议，Skill 是使用策略。

**治理一句：**

> Skill 不是越多越好，是越准越好——按需加载，全量塞进上下文会变成噪声。

**SKILL.md 骨架提示（粘贴后改）：**

```markdown
---
name: your-skill-name
description: 何时用 + 何时不用（写进 description，供路由）
---

# 适用 / 不适用
# 输入清单
# 步骤或决策分支
# 输出格式
# 质量标准（验收）
# 失败处理
# 安全边界（软约束；硬拦截在工程层）
```

## 坑（先避开）

1. **Skill = 长 Prompt**：挤爆上下文，重点丢失。  
2. **只写步骤不写边界**：误召回比漏召回更危险。  
3. **全量强制加载**：上下文污染、Token 暴涨、互相冲突。  
4. **工具参数写死在 Skill**：工具一升级 Skill 全坏；原则归 Skill，schema 归 Registry。  
5. **无 Eval 只靠感觉**：堆一堆不敢删的历史规则。  
6. **安全只写在 Skill**：模型可忽略；高风险动作必须工程拦截。  
7. **短链/标题差异**：本条用户分享文案与疑似成片标题不完全一致；落地以认知框架为准，勿假装已有逐字口播。

## 章节导航（对应 transcript）

| 章 | 内容 |
| --- | --- |
| A | 官方标题、标签、元数据（无口播正文） |
| B | 据题面推断的讲述结构 + 同作者 Skill 面试系列索引 |
| C | 知乎/阿里云面试答法重构 + Anthropic progressive disclosure |

## 同源回看

- 疑似成片：https://www.douyin.com/video/7698677228170759433  
- 用户短链（未闭环）：https://v.douyin.com/b2EZ9HkLSVVa9/  
- 同作者 · Skill 渐进式披露：https://www.douyin.com/video/7677925939157749007  
- 同作者 · 海量 Skill 加载：https://www.douyin.com/video/7676419507023301942  
- 二次文 · 知乎面试答法：https://zhuanlan.zhihu.com/p/2042910624909366006  
- 二次文 · 阿里云高质量 Skill：https://developer.aliyun.com/article/1743992  
- 规范 · Anthropic Agent Skills：https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills  

