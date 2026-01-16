def run_stats_analysis(df):
    return {"describe": df.describe(include="all").to_dict()}
