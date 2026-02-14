# Swisstony 策略说明（BTC 5m / 15m）

## 1) 核心定位
- **短期库存型**：以 CLOB 价差与快速回归为核心
- **市场**：BTC Up/Down 5m / 15m

## 2) 入场逻辑
- fair_prob = CLOB last_trade_price（USE_MARKET_FAIR_PROB）
- 触发阈值：BASE_BUY_DISCOUNT（当前 -0.1%）
- 方向：YES/NO 双向均可触发

## 3) 出场逻辑
- TP/SL：方向感知
- 超时强平：5m>10m、15m>15m
- Gamma 结算优先，CLOB end_date_iso 为 fallback

## 4) 监控与心跳
- 每 60 分钟心跳
- 记录 recent_trades + positions + m2m + remaining time

## 5) 风控
- 强平记录：SELL_TIMEOUT_10m / SELL_TIMEOUT_15m
- 仅允许单实例运行（supervisor 控制）
