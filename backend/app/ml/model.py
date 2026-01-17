# Baseline ML model runner
def run_baseline_model(df, target, task):# Baseline ML model runner
    if not target or target not in df.columns:
        return {"enabled": False}
    return {"enabled": True, "task": task}
