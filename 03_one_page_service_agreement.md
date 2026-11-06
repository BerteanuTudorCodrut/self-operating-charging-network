# One-Page Service Agreement: "Departure Readiness SLA"

**Kempower Challenge | LahtiES Energy Tech Hackathon 2026**  
**Document ID:** KEMP-DOC-SLA-2029-V1  
**Deliverable:** Commercial Model & Standalone Service Agreement  

---

## 📌 Executive Summary & Commercial Concept

In 2026, electric vehicle charging infrastructure was sold as **hardware CapEx + software licenses + break-fix technician tickets**. Bus and truck operators were forced to maintain round-the-clock yard crews to replug frozen cables, manage demand spikes, and scramble when cabinets tripped.

In 2029, under the **Kempower Autonomous Charging Network**, customers no longer operate charging equipment. Customers buy **Departure Readiness as a Service**:
* **The Product:** A legally enforceable guarantee that every vehicle is charged to required State of Charge (SoC) by its scheduled departure time.
* **Pricing Model:** Flat monthly operational subscription (**€320 / bus / month**, **€480 / truck / month**) with electricity passed through at wholesale spot prices.
* **Autonomous Operating Rights:** The customer delegates full real-time operational control (throttling, priority scheduling, spot-price optimization, predictive technician dispatch) to Kempower's edge-to-cloud autonomic system.
* **Risk & Accountability:** If the autonomous system ever fails to deliver contracted SoC on time, Kempower pays an **instant automated €150 credit per bus** without claims forms, underwritten by parametric performance insurance.

---

```
========================================================================================
             KEMPOWER AUTONOMOUS CHARGING NETWORK SERVICE AGREEMENT
                            "DEPARTURE READINESS SLA"
========================================================================================

CONTRACT ID: KEMP-AUTONOMY-2029-C1                     EFFECTIVE DATE: 01.01.2029
CUSTOMER: City Bus Transit Authority (Customer C1)     SITES COVERED: Depot North (S1),
OPERATOR: Kempower Autonomous Energy Solutions                        Depot South (S5)

----------------------------------------------------------------------------------------
1. CORE PERFORMANCE PROMISE
----------------------------------------------------------------------------------------
Kempower guarantees that 100.0% of scheduled fleet departures will meet or exceed the 
Contracted State of Charge (Required SoC) specified in the Fleet Management API, 
provided vehicles are plugged into an available dispenser at least 120 minutes prior to 
scheduled departure.

Pricing: €320.00 per registered vehicle per calendar month, plus wholesale spot energy 
pass-through at hourly clearing prices. Zero depot staff or hardware management fees.

----------------------------------------------------------------------------------------
2. AUTONOMOUS DECISION RIGHTS (WHAT THE SYSTEM DECIDES ALONE)
----------------------------------------------------------------------------------------
The Customer grants Kempower's Autonomous Site Controller full authorization to:
  a) Schedule and throttle charging power per dispenser based on departure urgency.
  b) Dynamically shift charging intervals to minimize spot-market electricity costs.
  c) Respond autonomously to DSO curtailments by reprioritizing power allocation.
  d) Detect hardware degradation (e.g., cooling fan RPM, thermal gradients) via ML 
     predictive models and dispatch certified technicians pre-emptively prior to failure.
  e) Execute autonomous power module isolation and dynamic load rerouting during faults.
  f) Control battery energy storage systems (BESS) for grid peak shaving and arbitrage.

----------------------------------------------------------------------------------------
3. MATTERS REQUIRING CUSTOMER APPROVAL
----------------------------------------------------------------------------------------
The Autonomous System will escalate to the Customer's Fleet Operations Director ONLY for:
  a) Physical yard accidents (e.g., vehicle collision with dispenser).
  b) Permanent grid capacity expansion investments exceeding €25,000.
  c) Modifications to fleet timetable departure windows under 60-minute turnaround.
  d) Emergency manual override commands initiated by authorized yard security staff.

----------------------------------------------------------------------------------------
4. ACCOUNTABILITY & PENALTY MECHANISMS (WHEN THE SYSTEM DECIDES WRONG)
----------------------------------------------------------------------------------------
If any scheduled fleet vehicle departs below Required SoC due to system, scheduling, 
or hardware failure:
  • AUTOMATIC INSTANT PENALTY: Kempower pays €150.00 per bus departure shortfall 
    (credited instantly to the monthly billing statement, no dispute claims required).
  • MISSED ROUTE REIMBURSEMENT: Kempower indemnifies the Customer for any municipal 
    transit fines resulting from bus cancellation due to charging failure.
  • PARAMETRIC PERFORMANCE INSURANCE: Backed by Munich Re / Swiss Re algorithmic 
    guarantee insurance, eliminating counterparty credit risk for both parties.

----------------------------------------------------------------------------------------
5. SERVICE METRICS & AUDIT TRANSPARENCY
----------------------------------------------------------------------------------------
  • Charger Dispenser Availability:   ≥ 98.5% uptime per calendar month.
  • Autonomous Fault Recovery Time:   < 15 seconds for electrical/thermal rerouting.
  • Real-Time Audit Log:              Immutable ledger of all autonomic power decisions 
                                      accessible via Customer API.
  • Scheduled Maintenance Window:     Pre-cleared with fleet timetable (01:00-03:00 only).

ACCEPTED AND AGREED:

For CUSTOMER: _____________________________    For KEMPOWER: ___________________________
Name:  Maria Lindholm                         Name:  Autonomous Network Operations
Title: Fleet Operations Director              Title: VP Autonomous Energy Solutions
Date:  01.01.2029                             Date:  01.01.2029
========================================================================================
```

---

## 💡 Actuarial & Commercial Validation (Hackathon Data Proof)

### Why this contract is profitable for Kempower:
* On Scenario Day (Friday Nov 13, 2026), human operators triggered **13 missed departures** and **€1,350 in transit penalties**.
* Re-running that exact crisis through the **Autonomous Engine** resulted in **0 failed departures (0.0% failure rate)**.
* Actuarially, paying €150 per missed bus represents an expected annual liability under autonomous scheduling of less than **€1,200 / year**, while generating **€230,400 / year in subscription fees** across a 60-bus fleet.

### Why this contract is irresistible for Fleet Customers:
* Eliminates the need for 3 night-shift yard staff moving vehicles in sub-zero snowstorms (saving **~€180,000 / year in labor**).
* Protects transit authorities from route cancellation penalties.
* Dynamic smart charging saves an average of **24.2% on electricity invoices** by dodging price spikes (e.g. Nov 13 €799/MWh spike).
