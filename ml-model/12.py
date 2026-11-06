import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# ==============================================================================
# STEP 1: LOAD THE TWO SPLIT DATASETS & FAULTS LOG
# ==============================================================================
train_df = pd.read_csv("telemetry_week1_train.csv")
test_df = pd.read_csv("telemetry_week2_blind_test.csv")
faults = pd.read_csv("faults.csv")

# Convert timestamps to datetime format
train_df['ts'] = pd.to_datetime(train_df['ts'])
test_df['ts'] = pd.to_datetime(test_df['ts'])
faults['start_ts'] = pd.to_datetime(faults['start_ts'])

# Feature column list for physical & anomaly modeling
feature_cols = [
    'power_kw', 'cabinet_temp_c', 'dt_15m', 'dt_1h',
    'thermal_res_ma', 'error_velocity', 'conn_drop_1h', 'cab_max_temp'
]

# ==============================================================================
# STEP 2: TRAIN MODEL STRICTLY ON WEEK 1 DATA
# ==============================================================================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(train_df[feature_cols].fillna(0))

# Train Isolation Forest on Week 1 baseline
iso_model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
iso_model.fit(X_train_scaled)

print("✓ Model successfully trained on Week 1 telemetry.")

# ==============================================================================
# STEP 3: BLIND INFERENCE & PREDICTION ON WEEK 2 DATA
# ==============================================================================
# Scale Week 2 data using Week 1 parameters (prevents data leakage)
X_test_scaled = scaler.transform(test_df[feature_cols].fillna(0))
test_df['ml_alert'] = (iso_model.predict(X_test_scaled) == -1).astype(int)

# Apply Physical Domain Rules to Week 2
rule_thermal = (
        (test_df['cabinet_temp_c'] > 48.0) |
        ((test_df['power_kw'] > 20.0) & (test_df['cabinet_temp_c'] > 40.0)) |
        (test_df['thermal_res_ma'] > 0.35) |
        (test_df['dt_15m'] > 5.0)
)
rule_comm = (test_df['conn_drop_1h'] >= 1) | (test_df['error_velocity'] >= 2)

# Combined Ensemble Alert
test_df['raw_alert'] = np.where(rule_thermal | rule_comm | (test_df['ml_alert'] == 1), 1, 0)

# Persistence Filter (Requires 2 consecutive 15-min alert slots to filter blips)
test_df['persistent_alert'] = test_df.groupby('charger_id')['raw_alert'].transform(
    lambda x: (x == 1) & (x.shift(1) == 1)
).astype(int)

# Export blind test predictions with alert flags
test_df.to_csv("telemetry_week2_predictions.csv", index=False)
print("✓ Blind test predictions saved to 'telemetry_week2_predictions.csv'.")

# ==============================================================================
# STEP 4: EVALUATE PERFORMANCE ON WEEK 2 GROUND TRUTH FAULTS (F010 - F019)
# ==============================================================================
week2_faults = faults[faults['start_ts'] >= '2026-11-09'].copy()
results = []
LOOKAHEAD_HOURS = 12

for _, row in week2_faults.iterrows():
    ch, cab, st, ft = row['charger_id'], row['cabinet_id'], row['site_id'], row['start_ts']
    w_start = ft - pd.Timedelta(hours=LOOKAHEAD_HOURS)

    # Filter telemetry window for charger, cabinet, or site fault
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
        'charger_id': ch if pd.notna(ch) else 'NaN (Cabinet)',
        'cabinet_id': cab,
        'detected': detected,
        'alert_count': len(anomalies),
        'lead_time_min': lead_time_min
    })

eval_df = pd.DataFrame(results)

# Display Formatted Results
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("\n=== BLIND TEST EVALUATION METRICS (WEEK 2) ===")
print(eval_df)
print(
    f"\nWeek 2 Blind Test Detection Rate: {eval_df['detected'].mean() * 100:.2f}% ({eval_df['detected'].sum()}/{len(eval_df)} faults caught)")
print(f"Average Warning Lead Time: {eval_df['lead_time_min'].mean() / 60.0:.2f} hours")