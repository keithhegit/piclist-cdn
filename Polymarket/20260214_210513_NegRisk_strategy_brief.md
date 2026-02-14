# NegRisk 策略说明（独立程序）

## 1) 定位
- **中期偏回归 / 错价捕捉**
- 仅监控：web3/crypto + football

## 2) 入场逻辑
- 使用 Gamma negRisk 市场
- 机会定义：|price - 0.5| >= 0.02
- Top N 机会（默认 5）按偏离 & 流动性排序
- price < 0.5 → BUY YES；price > 0.5 → BUY NO

## 3) 出场逻辑
- 回归平仓：0.5 ± 0.005
- 超时平仓：默认 12h（可迭代）
- 结算优先（未来接 Gamma outcome）

## 4) 资金与仓位
- 每笔资金 BET_SIZE 默认 25
- 记录 cash / positions / trades

## 5) 监控
- 10 分钟扫描 + 即时机会推送
- 心跳：机会数量 + 交易/持仓日志
