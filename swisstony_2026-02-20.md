# Swisstony Daily Report - February 20, 2026

**Generated:** 2026-02-20 09:01 AM (Asia/Shanghai)  
**Strategy:** Swisstony Polymarket Trading Loop  
**Period:** Feb 19-22, 2026

---

## Executive Summary

- **Candidates Identified:** 30 events (volume >= $3k)
- **OddsAPI Status:** ❌ Quota exhausted (all 13 queries failed)
- **New Positions Opened:** 0 (no valid opportunities due to API failure)
- **Active Positions:** 12 legs ($600 total exposure)
- **Cash Balance:** $2,150

---

## 🚨 Critical Issues

### OddsAPI Quota Exhausted
All 13 odds fetch attempts failed with `quota_exhausted` error:
- 6 NBA games (Rockets-Hornets, Nets-Cavaliers, Pistons-Knicks, Magic-Kings, Pacers-Wizards, Suns-Spurs)
- 5 Soccer matches (La Liga, EPL)
- 1 UFC event (Seabass-Anthony)

**Impact:** Unable to compute fair probabilities or identify new edges.

**Fallback Status:** API-Sports client available but not automatically triggered.

---

## 📊 Candidate Events (Top 10)

| Rank | Event | Date | Volume | Markets | Score |
|------|-------|------|--------|---------|-------|
| 1 | Sport Lisboa e Benfica vs. Real Madrid CF | Feb 17 | $747k | 3 | 777.2 |
| 2 | Rockets vs. Hornets | Feb 20 | $171k | 32 | 491.2 |
| 3 | AS Monaco FC vs. Paris Saint-Germain FC | Feb 17 | $450k | 3 | 479.6 |
| 4 | BV Borussia 09 Dortmund vs. Atalanta BC | Feb 17 | $385k | 3 | 414.9 |
| 5 | Abilene Christian vs. Tarleton State | Feb 17 | $341k | 6 | 401.1 |
| 6 | Nets vs. Cavaliers | Feb 20 | $47k | 34 | 386.9 |
| 7 | Syracuse Orange vs. Duke Blue Devils | Feb 17 | $291k | 8 | 370.5 |
| 8 | Houston Cougars vs. Iowa State Cyclones | Feb 17 | $326k | 4 | 365.8 |
| 9 | Wolverhampton Wanderers FC vs. Arsenal FC | Feb 18 | $332k | 3 | 362.0 |
| 10 | Coppin State vs. South Carolina State | Feb 17 | $248k | 10 | 347.8 |

---

## 💼 Current Portfolio (12 Positions)

### Open Positions

| Event | Market | Entry | Shares | Stake | Edge | Status |
|-------|--------|-------|--------|-------|------|--------|
| **Wolves vs Arsenal** (Feb 18) | Wolves Win | 0.07 | 714.3 | $50 | 29.9% | Open |
| **AC Milan vs Como** (Feb 18) | Milan Win | 0.39 | 128.2 | $50 | 9.1% | Open |
| **AC Milan vs Como** (Feb 18) | Como Win | 0.31 | 161.3 | $50 | 3.7% | Open |
| **Benfica vs Real Madrid** (Feb 17) | Benfica Win | 0.001 | 50,000 | $50 | 68,866% | Open |
| **Benfica vs Real Madrid** (Feb 17) | Draw | 0.001 | 50,000 | $50 | 20,733% | Open |
| **Athletic Club vs Elche** (Feb 20) | Athletic Win | 0.60 | 83.3 | $50 | N/A | Manual |
| **Man City vs Newcastle** (Feb 21) | Man City Win | 0.69 | 72.5 | $50 | N/A | Manual |
| **Osasuna vs Real Madrid** (Feb 21) | Real Madrid Win | 0.58 | 86.2 | $50 | N/A | Manual |
| **Osasuna vs Real Madrid** (Feb 21) | Draw | 0.24 | 208.3 | $50 | N/A | Manual |
| **Chelsea vs Burnley** (Feb 21) | Chelsea Win | 0.81 | 61.7 | $50 | N/A | Manual |
| **Real Sociedad vs Oviedo** (Feb 21) | Sociedad Win | 0.65 | 76.9 | $50 | N/A | Manual |
| **Real Sociedad vs Oviedo** (Feb 21) | Draw | 0.24 | 208.3 | $50 | N/A | Manual |

**Total Exposure:** $600  
**Manual Entries:** 8 positions (no edge data)

---

## 📈 Strategy Parameters

- **Edge Threshold:** 3.5% (absolute)
- **Take-Profit Delta:** 15-20%
- **Max Positions:** 5 legs
- **Stake per Leg:** $50
- **Market Types:** Moneyline + Totals only

---

## 🔍 Analysis & Recommendations

### Immediate Actions Required

1. **Restore OddsAPI Access**
   - Check quota reset date (likely monthly)
   - Consider upgrading plan or rotating keys
   - Implement API-Sports fallback automation

2. **Monitor Existing Positions**
   - 5 positions from Feb 17-18 may have resolved
   - Check Benfica-Real Madrid outcome (suspicious 0.001 entry price)
   - Update price history for delta tracking

3. **Manual Position Review**
   - 8 manual entries lack edge calculation
   - Retroactively compute fair probabilities if possible
   - Document entry rationale

### Risk Assessment

- **Concentration Risk:** 12 positions across 8 events (within 5-leg limit per event)
- **Data Risk:** No fresh odds data for 24+ hours
- **Execution Risk:** Manual entries without systematic edge validation

---

## 📝 Next Steps

1. **Immediate (Today)**
   - Check resolution status of Feb 17-18 events
   - Update paper_state.json with outcomes
   - Verify Benfica-Real Madrid positions (likely data error)

2. **Short-term (24-48h)**
   - Implement API-Sports fallback in swisstony_strategy.py
   - Set up quota monitoring alerts
   - Review manual entry process

3. **Medium-term (Next Week)**
   - Analyze hit rate on manual vs systematic entries
   - Optimize candidate filtering (reduce low-volume events)
   - Consider alternative odds providers

---

## 🎯 Performance Metrics (Pending)

- **Realized PnL:** TBD (awaiting Feb 17-18 settlements)
- **Unrealized PnL:** TBD (no current price data)
- **Hit Rate:** TBD
- **Avg Edge:** 3.5% (systematic), N/A (manual)

---

## Appendix

### Files Generated
- `docs/daily_reports/candidates_2026-02-20.json` - Gamma candidate list
- `swisstony_odds/opportunities_today.json` - Empty (API failure)
- `logs/paper_state.json` - Current portfolio state

### Logs
```
⚠️  OddsAPI 获取失败: nba-hou-cha-2026-02-19 (quota_exhausted)
⚠️  OddsAPI 获取失败: nba-bkn-cle-2026-02-19 (quota_exhausted)
... (11 more failures)
```

---

**Report Status:** ⚠️ Incomplete (API failure prevented full analysis)  
**Next Report:** 2026-02-21 09:00 AM
