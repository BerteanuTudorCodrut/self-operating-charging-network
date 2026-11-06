import pandas as pd

sched = pd.read_csv('fleet_schedule.csv')
sched['arrive_ts'] = pd.to_datetime(sched['arrive_ts'])
sched['depart_ts'] = pd.to_datetime(sched['depart_ts'])
deps = pd.read_csv('departures_baseline.csv')
deps['depart_ts'] = pd.to_datetime(deps['depart_ts'])
nov13_deps = deps[deps['depart_ts'].dt.strftime('%Y-%m-%d') == '2026-11-13']
merged = pd.merge(nov13_deps, sched, on=['vehicle_id', 'site_id', 'depart_ts', 'required_soc_pct'], how='left')
failed = merged[merged['below_required'] == 1]
for idx, r in failed.iterrows():
    print(f"{r['vehicle_id']} ({r['site_id']}): Arrive {r['arrive_ts']} (SoC {r['arrive_soc_pct']}%) -> Depart {r['depart_ts']} (Required {r['required_soc_pct']}%, Baseline Got {r['depart_soc_pct']}%)")
