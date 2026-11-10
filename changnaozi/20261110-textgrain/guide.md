# ChatGPT textGrain 文本水印与去除 - 抖音

## 一句话定位

49 秒科普：OpenAI 的 **textGrain** 会在 ChatGPT / Codex 文本里埋**看不见的统计水印**（复制粘贴仍可能带走）；成片演示用 GitHub 开源项目 **Watermarks Remover** 当「技能」去改写文本以打散水印图案——对留学场景（美国 / 澳洲等查 AI 率）很敏感，**攻略只整理机制与核实口径，默认不鼓励用它规避学校学术诚信政策**。

## 上手顺序

1. **先读官方，再信短视频**：打开 OpenAI 2026-10-05 文 [Our approach to EU text provenance rules](https://openai.com/index/eu-text-provenance/)——textGrain 在 ChatGPT / Codex **优先欧盟 rollout**；API 全球可**可选开启**、默认关。成片口语像「已经全面留水印」，口径偏简化。
2. **搞清水印是什么**：不是肉眼可见的角标，而是词选择里的**统计信号**；检测器找这个信号。编辑 / 同义替换会削弱信号（官方自测：400 token 文本，约 10% 同义替换检测率从 ~92% → ~66%；25% → ~17%）。
3. **若只是「自己内容的隐私清理」**：看仓库 [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) README——定位是 *privacy-first / content you own*；正式安装路径是 `install_skill.py` 装到 Claude Code / Codex / Cursor 等，**不是**成片里「把链接糊进 ChatGPT 网页对话框」那么随便（成片为演示压缩）。
4. **留学 / 作业场景**：把学校 Turnitin / 学术诚信规章当硬约束；用水印去除或强改写去「降 AI 率」属于高风险操作，本条攻略**不提供绕检 SOP**。
5. **需要引用政策时**：区分三层——OpenAI 官方页、本抖音成片剪辑口径、第三方工具 README。

## 能力表

| 能力 | 成片说法 | 核实后 |
|---|---|---|
| 产品名 | textGrain | ✅ 官方同名 |
| 作用范围 | ChatGPT + Codex 文本里 | ✅；消费端 **EU first**，非全球默认 |
| 可见性 | 普通用户完全看不到 | ✅ 统计隐写，非 UI 水印 |
| 复制粘贴 | 水印仍跟着走 | ✅ 信号在文本统计里，粘贴后仍可能可检 |
| 去除方式 | GitHub Watermarks Remover → 当 ChatGPT skill → 重写文本 | ⚠️ 仓库真实；安装/宿主与成片演示有落差；本质是**改写打散统计图案** |
| 检测 | 「不会被检测到」 | ⚠️ 绝对化；官方强调误检 / 漏检与编辑脆弱性 |

## 可复制提示词 / 金句（屏上原样）

- 顶栏：`chatgpt` / `AI水印在你所有文本里？`
- 公告卡：`Meet textGrain` · `Invisible. Inside the words.` · `EU first`
- 仓库：`github.com/guillaumemeyer/watermarks-remover`
- 对比条：`IT REWRITES THE TEXT ITSELF.` · BEFORE `Watermark pattern` / AFTER `No pattern, same meaning`
- 口播金句（英）：*The watermark is actually hidden inside of the words that ChatGPT writes, and even if you copy and paste the text, it still travels along with it.*

（成片未给出可粘贴的长 prompt；「Install this skill」是 UI 示意，不是完整提示词模板。）

## 坑

1. **地域口径**：成片没强调 **EU first**；人在美国 / 澳洲账号未必已默认打 textGrain。
2. **「安装技能」过度简化**：仓库 README 的安装目标是各类 agent host；ChatGPT 网页能否一键吃 GitHub 链接，以你账号实际能力为准，勿照搬成片。
3. **「去除 = 安全交作业」**：假的。学术场景看学校政策；水印 ≠ 证明「整篇是 AI」或「整篇是人写」。
4. **检测器不对公众全开**：官方称 detector 初期给受批研究人员 / 专业机构——短视频里的「检测/去除」演示往往是示意。
5. **硬字幕机翻**：成片中字有「法典」「回购协议」等误译，引用时以英文口播与屏上 UI 为准。

## 适合谁

- 想快速搞懂 **textGrain 是什么、和留学 AI 检测叙事有何关系** 的人。
- 需要把「短视频说法」对照 **OpenAI 一手文** 的研究者 / 内容创作者。
- **不适合**当作「美国 / 澳洲作业降 AI 率」操作手册。

## 章节导航

| 时间 | 内容 |
|---|---|
| 0:00–0:09 | 钩子：ChatGPT/Codex 开始带文本水印；60 秒教识别与去除 |
| 0:09–0:23 | textGrain 介绍：不可见、藏在用词里、复制粘贴仍带走 |
| 0:23–0:38 | 演示：打开 GitHub Watermarks Remover，链粘贴进 ChatGPT「安装技能」 |
| 0:38–0:49 | 效果：改写文本本身以摆脱水印图案 |

## 一手源（建议对照）

- OpenAI：https://openai.com/index/eu-text-provenance/ （2026-10-05）
- 工具仓：https://github.com/guillaumemeyer/watermarks-remover
- 本抖音成片：https://www.douyin.com/video/7706172500329172287
