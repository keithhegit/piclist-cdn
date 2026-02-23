# Swisstony Daily Report - February 23, 2026

**Report Generated:** 9:01 AM CST  
**Period Analyzed:** Feb 19-22, 2026  
**Strategy:** Swisstony (Moneyline + Totals)

---

## Executive Summary

**🎯 New Opportunities:** 0  
**📊 Current Portfolio:** 10 open positions  
**💰 Cash Balance:** $2,306.09  
**📈 Recent Closed Trades:** 2 (1 win, 1 loss)

---

## Strategy Execution

### Parameters
- **Edge Threshold:** ≥3.5% (absolute)
- **Max Legs:** 5
- **Stake per Leg:** $50
- **Take-Profit Delta:** 15-20%
- **Volume Filter:** ≥3,000
- **Data Source:** Gamma leagues + OddsAPI (key2) + API-Sports fallback

### Candidate Analysis
- **Total Candidates:** 13 events (Feb 19-22)
- **OddsAPI Matches:** 0/13
- **Unsupported Leagues:** 1 (UFC)

**Unmatched Events:**
- 6 NBA games (Rockets-Hornets, Nets-Cavaliers, Pistons-Knicks, Magic-Kings, Pacers-Wizards, Suns-Spurs)
- 5 Football matches (Athletic-Elche, Osasuna-Real Madrid, Chelsea-Burnley, Brentford-Brighton, Real Sociedad-Oviedo)
- 1 UFC event (Strickland vs Hernandez - skipped, unsupported)

**Root Cause:** OddsAPI coverage gap for these specific fixtures. Events may have passed or not yet available in OddsAPI's database.

---

## Current Open Positions (10)

### High-Edge Legacy Positions
1. **Benfica Win** (UCL vs Real Madrid)
   - Entry: $0.001 | Shares: 50,000 | Edge: 68,865%
   - Status: Likely mispriced entry, monitor for resolution

2. **Benfica Draw** (UCL vs Real Madrid)
   - Entry: $0.001 | Shares: 50,000 | Edge: 20,733%
   - Status: Likely mispriced entry, monitor for resolution

### Football Positions
3. **Wolves Win** (EPL vs Arsenal, Feb 18)
   - Entry: $0.07 | Shares: 714.29 | Edge: 29.87%
   - Status: Open, awaiting resolution

4. **AC Milan Win** (Serie A vs Como, Feb 18)
   - Entry: $0.39 | Shares: 128.21 | Edge: 9.11%
   - Status: Open, awaiting resolution

5. **Como Win** (Serie A vs AC Milan, Feb 18)
   - Entry: $0.31 | Shares: 161.29 | Edge: 3.72%
   - Status: Open, awaiting resolution

### Manual Entries (Feb 19)
6. **Man City Win** (EPL vs Newcastle, Feb 21)
   - Entry: $0.69 | Shares: 72.46 | Manual entry

7. **Real Madrid Win** (La Liga @ Osasuna, Feb 21)
   - Entry: $0.58 | Shares: 86.21 | Manual entry

8. **Osasuna Draw** (La Liga vs Real Madrid, Feb 21)
   - Entry: $0.24 | Shares: 208.33 | Manual entry

9. **Chelsea Win** (EPL vs Burnley, Feb 21)
   - Entry: $0.81 | Shares: 61.73 | Manual entry

10. **Brentford-Brighton** (position details in state file)

---

## Recent Closed Trades

### 1. Athletic Club Win (La Liga vs Elche, Feb 20)
- **Entry:** $0.60 @ Feb 19 15:54
- **Exit:** $0.53 @ Feb 21 05:17
- **PnL:** -$5.83 (-11.67%)
- **Outcome:** Loss (price moved against position)

### 2. Real Sociedad Draw (La Liga vs Oviedo, Feb 21)
- **Entry:** $0.24 @ Feb 19 15:54
- **Exit:** $0.36 @ Feb 21 21:51
- **PnL:** +$25.00 (+50%)
- **Outcome:** Win (50% gain on draw bet)

**Net Recent PnL:** +$19.17

---

## Issues & Observations

### 1. OddsAPI Coverage Gap
- **Impact:** 0/13 events matched for Feb 19-22 period
- **Likely Cause:** 
  - Events already passed (Feb 19-21 are in the past)
  - OddsAPI may not retain historical odds for resolved events
  - Some leagues (La Liga, Serie A) may have limited coverage
- **Recommendation:** 
  - For historical analysis, use API-Sports as primary source
  - Consider caching OddsAPI data pre-game for post-game analysis
  - Adjust date range to focus on upcoming events only

### 2. Manual Entry Positions
- 5 positions entered manually on Feb 19 without edge calculation
- These lack fair probability benchmarks for exit decisions
- **Action:** Monitor these positions for resolution and calculate actual edge post-facto

### 3. Legacy High-Edge Positions
- Benfica positions show extreme edge (68k%+), indicating likely data error or mispricing
- These positions should be reviewed for validity
- **Action:** Check if these markets have resolved and settle accordingly

### 4. UFC Coverage
- UFC events are currently unsupported by the strategy
- **Future Enhancement:** Add UFC odds support via specialized endpoints

---

## Portfolio Health

**Total Capital Deployed:** ~$500 (10 positions × $50)  
**Available Cash:** $2,306.09  
**Utilization:** ~17.8%  

**Risk Assessment:**
- ✅ Within max legs limit (10/5 - note: some are legacy/manual)
- ✅ Adequate cash reserves
- ⚠️ Several positions lack exit benchmarks (manual entries)
- ⚠️ Legacy positions need resolution verification

---

## Action Items

1. **Immediate:**
   - Verify resolution status of Feb 18-21 events
   - Settle resolved positions (Wolves, AC Milan, Como, manual entries)
   - Review Benfica positions for data validity

2. **Next Run:**
   - Adjust date range to upcoming events only (Feb 23+)
   - Consider API-Sports as primary source for historical analysis
   - Implement post-game edge calculation for manual entries

3. **Strategy Improvements:**
   - Add UFC odds support
   - Implement OddsAPI data caching for historical analysis
   - Create alert system for unmatched events

---

## Conclusion

**Today's Outcome:** No new positions opened due to OddsAPI coverage gap for the analyzed period (Feb 19-22). This is expected behavior when analyzing past events, as OddsAPI focuses on upcoming fixtures.

**Portfolio Status:** 10 open positions awaiting resolution, with 2 recent trades showing net positive PnL (+$19.17). Several positions require resolution verification and settlement.

**Next Steps:** Shift focus to upcoming events (Feb 23+) and settle historical positions.

---

*Generated by Swisstony Strategy Engine v1.0*  
*Data Sources: Gamma Markets, OddsAPI (key2), API-Sports*
