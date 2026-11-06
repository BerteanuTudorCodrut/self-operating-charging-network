# 10-Minute Pitch & Customer Story: "The Invisible Network"

**Kempower Challenge | LahtiES Energy Tech Hackathon 2026**  
**Format:** 10-Minute Keynote & Live Demonstration  
**Setting:** Friday, November 13, 2029 (Looking back at November 13, 2026)

---

## 🎬 Cast & Characters

- **Maria Lindholm**: Fleet Operations Director, *Pohjolan Liikenne* (operating 60 electric buses across Depot North S1 and Depot South S5).
- **The Competitor / Legacy World (2026)**: Humans in the loop, frantic phone calls, night shift staff moving 18-ton buses in -14°C snow, €150/departure transit fines.
- **The Autonomous World (2029)**: The Self-Operating Charging Network — zero manual replugs, predictive self-healing, guaranteed departure readiness.

---

## ⏱️ Minute-by-Minute Pitch Script

### [0:00 – 2:00] ACT I: The 3:00 AM Nightmare (Friday Nov 13, 2026)

*(Visual: Dim slide showing a blizzard in Finland. -14°C thermometer. A ringing phone screen glowing in the dark).*

**Speaker:**
> "Three years ago, on Friday the thirteenth of November 2026, Maria Lindholm’s phone rang at 3:12 in the morning.
>
> It was minus fourteen degrees outside. On the other end of the line was Jari, the night yard supervisor at Bus Depot North. He was shouting over the wind:
>
> *'Maria, Cabinet Three tripped on overtemperature! Four chargers are completely dead. Twelve buses are waiting for their morning runs, and the screen just says Ground Fault Derate! What do I do?'*
>
> What did Jari do? He did what the industry had been doing for a decade: he put on thick winter gloves, grabbed a heavy frozen charging cable, and spent the next two hours in a snowstorm manually shuffling 18-ton buses between dispensers. Nine manual vehicle replugs. Ninety-seven minutes of emergency technician travel. 
>
> But it wasn’t enough. At 5:35 AM, Bus B18 and Bus B20 rolled out of the depot gate into the morning rush with **eight percent battery**. 
>
> They didn't make it two kilometers before dying on the ring road. Route 4 to the regional hospital was canceled. Hundreds of morning commuters were left standing in the freezing cold. Maria’s company was hit with €1,350 in transit authority penalties. And to top it off, because the remaining chargers ran wide open during the evening peak, the depot bought electricity at **€799 per megawatt-hour**.
>
> That morning, Maria looked at her invoice and asked a question every fleet operator has thought:
> 
> *'Why did we spend millions of euros on cutting-edge zero-emission vehicles, only to rely on tired humans freezing in the dark to make them work?'*"

---

### [2:00 – 4:00] ACT II: The Redesign — Where Does the Brain Live?

*(Visual: Architecture diagram transition from chaos to the 3-Tier Autonomic Hierarchy: Edge, Site Controller, Fleet Cloud).*

**Speaker:**
> "If humans were no longer allowed to continuously operate and maintain a charging network, how would you redesign it?
>
> We realized the industry made a fundamental mistake: **building dashboards for humans to stare at.** Adding more alerts, more telegram channels, and more buttons just gives human operators more ways to make mistakes under pressure.
>
> We don't need better dashboards. **We need to remove the human from the loop entirely.**
>
> Here is our design: **The Three-Tier Autonomous Charging Network.**
>
> 1. **At the Edge (The Charger & Cabinet):** Sub-second hardware reflexes. If a cooling fan starts degrading, the power cabinet doesn't wait to blow a fuse. It isolates the affected module, throttles back gently, and notifies the site controller.
> 2. **At the Site (The Autonomous Local Controller):** An industrial edge PC running on-site. It knows the departure schedule of every bus and truck. It calculates **Slack Time** — `(Time to Departure - Current Time) / kWh Needed`. It knows weather forecasts, so when it drops below minus ten, it automatically injects a fifteen percent battery preheating buffer. And crucially: **if the cellular connection drops, the site operates 100% autonomously.** No cloud dependency.
> 3. **In the Cloud (The Fleet Brain):** Multi-site orchestration. It watches 100 sites across five countries, trades on Nord Pool 15-minute spot markets, bids into Fingrid's FCR-D fast frequency reserve markets, and monitors fleet-wide component wear.
>
> And underpinning all three tiers is a **Predictive Health Engine** — a machine learning model we actually built for this hackathon. It trains on normal telemetry baselines and detects anomalies before they become faults. It's an Isolation Forest ensemble combined with physics-based thermal and connectivity rules. We trained it on Week 1 of this dataset and blind-tested it on Week 2. You can run it yourself from our repository."

---

### [4:00 – 6:30] ACT III: The Live Proof — Re-running Friday the 13th

*(Visual: Switch to live demo screen showing [dashboard.html](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/dashboard.html). Headline numbers pop up).*

**Speaker:**
> "Don't take our word for it. Let's look at the actual dataset from that Friday the thirteenth, re-run through our Autonomous Simulation Engine.
>
> But first — we split the dataset in half. Week 1 is the normal baseline. Week 2 contains Friday the 13th. We trained our Predictive Health Model on Week 1 — learning what 'normal' looks like — then ran it blind on Week 2. **Nine out of ten real faults were detected, with an average warning lead time of seven hours.** The only miss was a communication fault on a brand-new charger at S5 that had zero training data — which actually proves the model needs baseline data, exactly what our autonomous commissioning system would provide.
>
> Here is what happens when the exact same crisis hits the autonomous network:
>
> **First: Depot North (S1) and the Fan Failure.**  
> In the baseline, Cabinet C1-3 overheated at 2:25 AM, cutting four dispensers and leaving three buses at 8% battery.  
> Under our autonomous system, the predictive telemetry agent detected the declining fan RPM and rising thermal gradient on Thursday afternoon — eighteen hours before the failure. Our model detected thermal anomalies on Cabinet C1-3 — faults F015 and F016 — with alerts firing hours before the critical 2:25 AM shutdown. Even if the cabinet had shut down instantly, the Site Controller dynamically reallocated power across the remaining eight healthy dispensers, prioritizing buses by departure time.  
> **Result: Zero failed departures. All 32 buses left at over 92% SoC. Zero human staff minutes.**
>
> **Second: Depot East (S2) and the DSO Grid Curtailment.**  
> At 2:00 PM, the grid company notified the site that power would be capped from 800 kW to 400 kW between 16:00 and 19:00. In 2026, the human operator gave power to trucks staying until tomorrow, starving the four short-turnaround trucks (T01–T04).  
> Our system received the digital DSO notice at 14:00. It calculated that T01 through T04 were departing during the curtailment window. Between 14:20 and 16:00, it delivered a **300 kW burst charge**, filling all four trucks to 78% SoC *before* the curtailment began. Then, during the €799 price spike, it paused overnight trucks, shifting their charge to the €28 night window.  
> **Result: Four delivery trucks saved. Zero logistics delays. €375 saved on electricity in two hours.**
>
> **Third: Highway Hub (S3) and the 2-Hour Offline Outage.**  
> When cellular backhaul dropped from 11:00 to 13:00, the legacy chargers throttled to 50 kW, creating massive queues and driving away 76 drivers.  
> Our local Edge Controller maintained full 1,500 kW load balancing locally. Combined with our dynamic wait-time API feeding in-car navigation, queue abandonment dropped by **76 percent**, generating **€1,920 in additional net revenue** on that day alone.
>
> Across the five sites on Scenario Day:
> - **Failed departures dropped from 13 to ZERO.**
> - **Human workload dropped from 265 minutes to ZERO.**
> - **Energy costs dropped by 24.2%.**
> - **SLA penalties: €1,350 completely eliminated.**
> - **Predictive fault detection: 90% of real Week 2 faults caught an average of 7 hours before failure.**"

---

### [6:30 – 8:30] ACT IV: The Commercial Model — What Does the Customer Buy?

*(Visual: Slide displaying the One-Page Service Level Agreement (SLA) from [03_one_page_service_agreement.md](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/03_one_page_service_agreement.md) and [01_autonomous_system_architecture_and_sla.md](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/01_autonomous_system_architecture_and_sla.md)).*

**Speaker:**
> "Now, the crucial commercial question:  
> **When nobody operates the network, what does the customer actually buy?**
>
> Maria doesn't buy kilowatt-hours. She doesn't buy chargers. She doesn't buy technician hours.  
> In 2029, Maria buys **Departure Readiness as a Service.**
>
> Here is our **One-Page Service Agreement**:
>
> 1. **The Contracted Promise:** Every bus plugged in at least two hours before departure is guaranteed to leave at required SoC.
> 2. **What the System Decides Alone:** Power dispatch, charging order, price-spike dodging, battery cycling, and preventive technician dispatch.
> 3. **What Requires Human Approval:** CapEx grid upgrades over €25,000 and physical site design.
> 4. **Who is Accountable When It Decides Wrong:** If the autonomous scheduler ever causes an under-charged departure, **Kempower automatically pays a €150 penalty per bus, credited instantly to the customer's account.** No claims forms, no arguments. Parametrically insured by global underwriting partners.
>
> And look at the network economics at scale: across 100 sites, this architecture creates **€3.86 million per year in new value** — from eliminating manual replugging labor, peak demand charge shaving, and reserve market flexibility."

---

### [8:30 – 10:00] ACT V: Maria's Morning in 2029

*(Visual: Warm sunrise over Helsinki. Electric buses gliding smoothly through snow-covered streets. A sleek smartphone showing a single calm notification).*

**Speaker:**
> "Let's return to Maria Lindholm.
>
> It is Friday, November 13th, 2029. 
>
> Outside, it is minus fourteen degrees again. The wind is howling across the depot asphalt.
>
> But at 3:12 in the morning, Maria’s phone does not ring. Maria is fast asleep. Jari isn't freezing in the yard. 
>
> Inside the depot, thirty-six charging dispensers quietly communicate with the on-site controller. The system preheated the bus batteries using off-peak power at two in the morning. It scheduled every vehicle according to its exact departure route. 
>
> When Maria wakes up at 6:45, she checks her phone over a warm cup of coffee. There is a single silent notification:
>
> *'All 36 morning departures 100% ready. Spot price spike successfully avoided. Depot North operating at 100% availability.'*
>
> Maria takes a sip of coffee, smiles, and watches her electric buses roll silently down the street, on time, into the city.
>
> When charging networks operate themselves, electric mobility stops being an operational headache.  
> **It becomes an invisible, flawless utility.**
>
> Thank you."

---

## 🛡️ Judge Q&A Defense Strategy

| Likely Judge Question | Winning Response | Data Reference |
|---|---|---|
| **"What happens if the local Site Controller hardware dies completely?"** | "Each power cabinet runs autonomous fallback firmware. Even if the site industrial PC is physically severed, cabinets default to static fair-share current limits safe for the grid connection limit (`offline_fallback_kw_per_dispenser` in `site_config.csv`). No charger stops charging." | `site_config.csv` offline parameters |
| **"Isn't €150 penalty per missed bus risky for Kempower?"** | "In 2026 baseline, human operators caused 13 failures and €1,350 in penalties on one bad day. Under autonomous scheduling, failure rate is 0.0% on this exact dataset. The risk is actuarially negligible and backed by parametric performance insurance." | `contracts.csv`, C1 contract terms |
| **"How does this handle dynamic grid curtailment when lead time is zero?"** | "Sub-second PWM curtailment. If the DSO drops grid limit via physical dry contact or digital signal with zero lead time, the edge controllers throttle within 200 milliseconds, well within grid compliance thresholds." | `grid_events.csv`, limit_cap response |
| **"How do you justify BESS investments at €375k per MWh?"** | "At SE-21 (bus depot with 147h over grid and no DSO upgrade available), BESS avoids €100k+ in route cancellation penalties and earns €35k/yr in FCR-D reserves, achieving payback in 3.2 years." | `reserve_market_prices.csv`, `equipment_costs.csv` |
| **"Is the predictive maintenance just a concept or did you actually build it?"** | "We built it. Model/12.py trains an Isolation Forest on Week 1 telemetry. It runs blind on Week 2 and detects 90% of the 10 real faults (9/10) with a 7-hour average lead time. The only miss was on a newly commissioned charger with no prior baseline. No data leakage — scaler is fit on Week 1 only." | `Model/12.py`, `Model/EV_Charger_Predictive_Health_Full_Report.docx` |
| **"What's the false alarm rate?"** | "We use a persistence filter — two consecutive 15-minute anomaly windows must fire before an alert is raised. This eliminates transient spikes. The Isolation Forest contamination parameter is set to 2%, tuned to the expected fault rate." | `Model/12.py` |

---

## 📁 Hackathon Deliverables Mapping Checklist

- [x] **Deliverable 1: Network Design & Intelligence Distribution** -> See [01_autonomous_system_architecture_and_sla.md](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/01_autonomous_system_architecture_and_sla.md) (Section 1)
- [x] **Deliverable 2: Scenario Day Demonstration on Data** -> See [autonomous_engine.py](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/autonomous_engine.py), [dashboard_dark_mode_before.html](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/dashboard_dark_mode_before.html) (BEFORE) & [dashboard_dark_mode.html](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/dashboard_dark_mode.html) (AFTER)
- [x] **Deliverable 3: Commercial Model & One-Page SLA** -> See [03_one_page_service_agreement.md](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/03_one_page_service_agreement.md) & [01_autonomous_system_architecture_and_sla.md](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/01_autonomous_system_architecture_and_sla.md) (Sections 2 & 3)
- [x] **Deliverable 4: 10-Minute Pitch & 2029 Customer Story** -> See [02_ten_minute_pitch_and_customer_story.md](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/02_ten_minute_pitch_and_customer_story.md)
- [x] **Deliverable 5: Predictive Health Model (Bonus)** -> See [Model/12.py](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/Model/12.py) + [Model/EV_Charger_Predictive_Health_Full_Report.docx](file:///C:/Users/Codrut/Desktop/kempower-challenge-data/Model/EV_Charger_Predictive_Health_Full_Report.docx)
