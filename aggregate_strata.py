import pandas as pd
import glob

def aggregate_national_ledger(log_pattern="./logs/ledger_*.jsonl"):
    """
    Consolidates distributed node logs into a single National Status Report.
    """
    all_logs = glob.glob(log_pattern)
    df_list = [pd.read_json(f, lines=True) for f in all_logs]
    
    # Merge all node data into one master dataframe
    national_df = pd.concat(df_list, ignore_index=True)
    
    # Calculate the Total System Mass (GT)
    total_mass = national_df.groupby('timestamp')['mass_gt'].sum()
    
    # Calculate National Integrity (Average Jitter)
    avg_jitter = national_df['jitter_ns'].mean()
    
    print(f"--- Aqua Chroma National Report ---")
    print(f"Total Managed Mass: {total_mass.iloc[-1]} GT")
    print(f"National Phase Integrity: {100 - (avg_jitter * 10)}%")
    
    return national_df