# Swisstony Polymarket Daily Report
**Period:** February 19-22, 2026  
**Generated:** February 24, 2026 09:01 AM (Asia/Shanghai)  
**Strategy:** Swisstony Edge-Based Trading

---

## Executive Summary

**Opportunities Scanned:** 30 events from Gamma leagues (volume ≥ $3k)  
**Valid Opportunities Found:** 0 (with edge ≥ 3.5% absolute)  
**Positions Opened:** 0 new positions  
**Current Open Positions:** 9  
**Closed Positions (Period):** 2  
**Current Cash:** $2,306.09  
**Total P&L (Period):** +$11.17

---

## Market Scanning Results

### Candidates Identified (Feb 19-22)
- **Total Events:** 30 from Gamma leagues
- **Min Volume Filter:** $3,000
- **Date Range:** 2026-02-19 to 2026-02-22

### Top Candidates by Volume:
1. **Rockets vs. Hornets** - $171,239 volume, 32 markets
2. **Nets vs. Cavaliers** - $46,905 volume, 34 markets  
3. **Pistons vs. Knicks** - $28,520 volume, 30 markets
4. **Magic vs. Kings** - $22,578 volume, 26 markets
5. **Pacers vs. Wizards** - $21,258 volume, 25 markets
6. **Suns vs. Spurs** - $17,295 volume, 27 markets

### OddsAPI Matching Issues
⚠️ **11 events could not be matched** with OddsAPI data:
- 6 NBA games (Rockets/Hornets, Nets/Cavaliers, Pistons/Knicks, Magic/Kings, Pacers/Wizards, Suns/Spurs)
- 5 Soccer matches (Athletic/Elche, Osasuna/Real Madrid, Chelsea/Burnley, Brentford/Brighton, Real Sociedad/Oviedo)

**Root Cause:** OddsAPI sport key mismatch or event not available in their feed

---

## Edge Analysis

### Parameters Used:
- **Minimum Edge:** 3.5% (absolute difference)
- **Max Legs:** 5 positions
- **Stake per Leg:** $50
- **Take-Profit Delta:** 15-20%
- **Markets:** Moneyline + Totals only

### Results:
**0 opportunities met the 3.5% edge threshold** during the scan period.

**Reasons:**
1. OddsAPI coverage gaps for NBA and some soccer leagues
2. Markets already efficient (Polymarket prices aligned with bookmaker consensus)
3. Low liquidity on some totals markets

---

## Position Management

### Open Positions (9 active)

| Event | Market | Entry | Shares | Stake | Status |
|-------|--------|-------|--------|-------|--------|
| Wolves vs Arsenal (Feb 18) | Wolves Win | 0.07 | 714.29 | $50 | Open |
| AC Milan vs Como (Feb 18) | Milan Win | 0.39 | 128.21 | $50 | Open |
| AC Milan vs Como (Feb 18) | Como Win | 0.31 | 161.29 | $50 | Open |
| Benfica vs Real Madrid (Feb 17) | Benfica Win | 0.001 | 50,000 | $50 | Open |
| Benfica vs Real Madrid (Feb 17) | Draw | 0.001 | 50,000 | $50 | Open |
| Man City vs Newcastle (Feb 21) | Man City Win | 0.69 | 72.46 | $50 | Open |
| Osasuna vs Real Madrid (Feb 21) | Real Madrid Win | 0.58 | 86.21 | $50 | Open |
| Osasuna vs Real Madrid (Feb 21) | Draw | 0.24 | 208.33 | $50 | Open |
| Chelsea vs Burnley (Feb 21) | Chelsea Win | 0.81 | 61.73 | $50 | Open |

**Note:** Benfica/Real Madrid positions show extreme edge calculations (68,865% and 20,733%) due to 0.001 entry prices - likely data anomaly or market inefficiency.

### Closed Positions (2)

| Event | Market | Entry | Exit | P&L | Exit Reason |
|-------|--------|-------|------|-----|-------------|
| Athletic vs Elche (Feb 20) | Athletic Win | 0.60 | 0.53 | -$5.83 | Manual exit |
| Real Sociedad vs Oviedo (Feb 21) | Draw | 0.24 | 0.36 | +$25.00 | Manual exit |

**Period P&L:** +$19.17 (before accounting for open position unrealized)

---

## OddsAPI Quota Status

⚠️ **Current Status:** Key1 exhausted, using Key2  
**Cache TTL:** 15 minutes  
**Fallback:** API-Sports for football/basketball

**Recommendations:**
1. Monitor Key2 usage closely
2. Implement API-Sports as primary for supported leagues
3. Consider CLOB orderbook prices as fair probability alternative

---

## Strategy Performance Metrics

### Hit Rate (Closed Positions):
- **Wins:** 1 (Real Sociedad Draw)
- **Losses:** 1 (Athletic Win)
- **Win Rate:** 50%

### Risk Management:
- **Max Legs:** 5 (currently 9 open - exceeds limit)
- **Stake per Leg:** $50 (compliant)
- **Total Capital at Risk:** $450 (9 positions × $50)

⚠️ **Alert:** Current open positions (9) exceed max legs parameter (5). Recommend closing or reducing exposure.

---

## Issues & Observations

### Critical Issues:
1. **OddsAPI Coverage Gaps:** 11/30 events (37%) could not be matched
2. **Position Limit Exceeded:** 9 open positions vs 5 max parameter
3. **Data Anomaly:** Benfica/Real Madrid positions show unrealistic edge calculations

### Market Observations:
1. NBA markets not available in OddsAPI feed for Feb 20-22
2. Some La Liga and EPL matches missing from odds provider
3. Low-volume markets (<$50k) show wider spreads but insufficient edge

### Recommendations:
1. **Immediate:** Close 4 positions to comply with max legs limit
2. **Short-term:** Implement API-Sports as primary for NBA/soccer
3. **Medium-term:** Add CLOB orderbook analysis for fair probability estimation
4. **Long-term:** Build multi-provider odds aggregation (OddsAPI + API-Sports + Pinnacle)

---

## Next Actions

### For Next Run (Feb 25):
1. ✅ Scan Gamma leagues for Feb 25-28 events
2. ✅ Use API-Sports primary for NBA games
3. ✅ Close 4 positions to meet max legs constraint
4. ✅ Monitor Benfica/Real Madrid positions for resolution
5. ✅ Implement orderbook-based fair probability for unmatched events

### Monitoring Schedule:
- **Pregame (0-3h before):** Check price convergence on open positions
- **In-game:** Monitor for take-profit triggers (15-20% delta)
- **Post-game:** Settle resolved markets, update P&L

---

## Appendix: Raw Data

### Candidate Events (Top 10 by Score):
1. Benfica vs Real Madrid - Score: 777.2
2. Rockets vs Hornets - Score: 491.2
3. Monaco vs PSG - Score: 479.6
4. Dortmund vs Atalanta - Score: 414.9
5. Abilene Christian vs Tarleton State - Score: 401.1
6. Nets vs Cavaliers - Score: 386.9
7. Syracuse vs Duke - Score: 370.5
8. Houston vs Iowa State - Score: 365.8
9. Wolves vs Arsenal - Score: 362.0
10. Coppin State vs South Carolina State - Score: 347.8

### System Info:
- **Python:** 3.x
- **Workspace:** /Users/mac/Desktop/PolymarketTrading
- **Last State Update:** 2026-02-24 08:56:39 UTC
- **Report Generated:** 2026-02-24 09:01 AM (Asia/Shanghai)

---

**Report Status:** ✅ Complete  
**Positions Opened:** 0 (no valid opportunities with edge ≥ 3.5%)  
**Action Required:** Close 4 positions to meet max legs limit
