import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

train_df = pd.read_csv("telemetry_week1_train.csv")
test_df = pd.read_csv("telemetry_week2_blind_test.csv")
faults = pd.read_csv("../faults.csv")

train_df['ts'] = pd.to_datetime(train_df['ts'])
test_df['ts'] = pd.to_datetime(test_df['ts'])
faults['start_ts'] = pd.to_datetime(faults['start_ts'])

feature_cols = [
    'power_kw', 'cabinet_temp_c', 'dt_15m', 'dt_1h',
    'thermal_res_ma', 'error_velocity', 'conn_drop_1h', 'cab_max_temp'
]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(train_df[feature_cols].fillna(0))

iso_model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
iso_model.fit(X_train_scaled)
print("Model trained on Week 1 telemetry.")

X_test_scaled = scaler.transform(test_df[feature_cols].fillna(0))
test_df['ml_alert'] = (iso_model.predict(X_test_scaled) == -1).astype(int)

rule_thermal = (
    (test_df['cabinet_temp_c'] > 48.0) |
    ((test_df['power_kw'] > 20.0) & (test_df['cabinet_temp_c'] > 40.0)) |
    (test_df['thermal_res_ma'] > 0.35) |
    (test_df['dt_15m'] > 5.0)
)
rule_comm = (test_df['conn_drop_1h'] >= 1) | (test_df['error_velocity'] >= 2)

test_df['raw_alert'] = np.where(rule_thermal | rule_comm | (test_df['ml_alert'] == 1), 1, 0)
test_df['persistent_alert'] = test_df.groupby('charger_id')['raw_alert'].transform(
    lambda x: (x == 1) & (x.shift(1) == 1)
).astype(int)

week2_faults = faults[faults['start_ts'] >= '2026-11-09'].copy()
results = []
LOOKAHEAD_HOURS = 12

for _, row in week2_faults.iterrows():
    ch, cab, st, ft = row['charger_id'], row['cabinet_id'], row['site_id'], row['start_ts']
    w_start = ft - pd.Timedelta(hours=LOOKAHEAD_HOURS)
    if pd.notna(ch):
        sub = test_df[(test_df['charger_id'] == ch) & (test_df['ts'] >= w_start) & (test_df['ts'] <= ft)]
    elif pd.notna(cab):
        sub = test_df[(test_df['cabinet_id'] == cab) & (test_df['ts'] >= w_start) & (test_df['ts'] <= ft)]
    else:
        sub = test_df[(test_df['site_id'] == st) & (test_df['ts'] >= w_start) & (test_df['ts'] <= ft)]
    anomalies = sub[sub['persistent_alert'] == 1]
    detected = 1 if len(anomalies) > 0 else 0
    lead_time_min = (ft - anomalies['ts'].min()).total_seconds() / 60.0 if detected else np.nan
    results.append({
        'fault_id': row['fault_id'],
        'category': row['fault_category'],
        'charger_id': ch if pd.notna(ch) else 'Cabinet-level',
        'cabinet_id': cab,
        'detected': detected,
        'alert_count': len(anomalies),
        'lead_time_min': lead_time_min
    })

eval_df = pd.DataFrame(results)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print()
print("=== BLIND TEST EVALUATION METRICS (WEEK 2) ===")
print(eval_df.to_string(index=False))
det_rate = eval_df['detected'].mean() * 100
det_count = int(eval_df['detected'].sum())
det_total = len(eval_df)
avg_lead = eval_df['lead_time_min'].mean() / 60.0
med_lead = eval_df['lead_time_min'].median() / 60.0
print(f"\nWeek 2 Blind Test Detection Rate: {det_rate:.1f}% ({det_count}/{det_total} faults caught)")
print(f"Average Warning Lead Time: {avg_lead:.2f} hours")
print(f"Median Warning Lead Time: {med_lead:.2f} hours")
