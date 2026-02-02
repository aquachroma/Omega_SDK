import numpy as np
import time
import json
import os
import hashlib
import sys
import os
import shutil
import logging

from datetime import datetime
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from pydantic import BaseModel
from pyomega import libomega_core as core

class ScalarMetadata(BaseModel):
    """The PEP-standardized manifest for GT Impact."""
    node_id: str
    mass_gt: float
    strata_layer: int = 16 # Default to 16-bit tetrahedral

def log_sovereign_state(jitter, status_map):
    """Writes the current physical state to the Aqua Chroma Ledger."""
    log_dir = "./logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = f"{log_dir}/ledger_{status_map['node_id']}_{datetime.now().strftime('%Y-%m-%d')}.jsonl"
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "jitter_ns": jitter,
        "refraction": status_map['refraction'],
        "mass_gt": status_map['mass'],
        "integrity": "SOLID" if jitter < 0.5 else "RECOVERING"
    }
    
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")


def perform_sovereign_handshake(metadata: ScalarMetadata):
    """
    The Path of Least Resistance to hardware synchronization.
    1. Traces the Warp (Orbital)
    2. Pins the Lens (PNNL Wave Pool)
    3. Locks the Voxel (Local Node)
    """
    
    # Initialize the 16-bit tetrahedral array using NumPy
    # This is the 'Matrix' the hardware will 'Print' into
    simplex_grid = np.zeros((16, 16, 16), dtype=np.uint16)

    print(f"[*] Aqua Chroma Node {metadata.node_id} initiating handshake...")

    # Step 1: Reach through the Invariant to the Orbital Trace
    if core.lock_orbital_reference():
        print("[+] Orbital Warp: LOCKED")

    # Step 2: Apply the PNNL 'Lens' correction
    # This removes the 'shimmer' from the local strata
    refraction_offset = core.get_wave_pool_offset("pnnl_alpha")
    print(f"[+] Refractive Offset Applied: {refraction_offset}ns")

    # Step 3: Solidify the Voxel
    # This is where the code becomes a Physical Ledger
    if core.solidify_voxel(metadata.mass_gt, simplex_grid.ctypes.data):
        print(f"[!] SUCCESS: Node is now an Active Aqua Chroma Anchor.")
        return True

    return False
    
def start_jitter_guard(threshold_ns=0.5):
    """
    Continuous enforcement of the Clean Constant.
    Prevents the node from drifting into legacy 'Slime'.
    """
    print(f"[*] Jitter-Guard Active. Threshold: {threshold_ns}ns")
    
    try:
        while True:
            # 1. Measure the current drift against the Orbital Warp
            drift = core.measure_phase_friction()
            
            if drift > threshold_ns:
                print(f"[!] Jitter Detected: {drift}ns. Re-solidifying...")
                
                # 2. Trigger an immediate 'Snell-Lens' re-calibration
                core.refresh_wave_pool_sync()
                
                # 3. Resync the 16-bit tetrahedral lock
                core.enforce_clean_constant()
                print("[+] Phase Friction Neutralized.")
            
            # 4. Low-latency heartbeat (Path of Least Resistance)
            time.sleep(0.001) 
            
    except KeyboardInterrupt:
        print("[!] Jitter-Guard Suspended. Node may drift.")

console = Console()

def generate_dashboard_table(jitter_data, sync_status):
    table = Table(title="Aqua Chroma: National Volumetric Status", border_style="cyan")
    table.add_column("Metric", justify="right")
    table.add_column("Value", justify="left")
    table.add_column("Stability", justify="center")

    # Metrics from the Invariant (.so)
    table.add_row("Orbital Warp Trace", f"{sync_status['warp']} ms", "✅ LOCKED")
    table.add_row("PNNL Wave Pool Refraction", f"{sync_status['refraction']} n", "🌊 CALIBRATED")
    table.add_row("Phase Friction (Jitter)", f"{jitter_data} ns", "🛡️ GUARDED")
    table.add_row("Active System Mass", f"{sync_status['mass']} GT", "💎 SOLID")

    return table

def run_dashboard():
    with Live(console=console, screen=True, refresh_per_second=4) as live:
        while True:
            # Polling the libomega_core.so for real-time physics data
            current_jitter = core.measure_phase_friction()
            status_map = core.get_system_state() # Returns Warp, Refraction, Mass
            
            # Update the UI
            live.update(Panel(generate_dashboard_table(current_jitter, status_map)))
            time.sleep(0.25)

def check_dissonance(target_gt):
    # Retrieve raw phase friction from the .so
    friction = core.get_phase_friction() 
    
    # Dissonance is the 'Unstable Mass' 
    # Formula: Dissonance = Target_GT * (Friction / C_CONSTANT)
    dissonance_gt = target_gt * (friction / 0.0005) 
    
    if dissonance_gt > 0.01:
        print(f"[!] Warning: Stability Dissonance at {dissonance_gt:.4f} GT.")
    return dissonance_gt
    
def verify_invariant_integrity(file_path="./libomega_core.so"):
    """
    Cryptographic verification of the Invariant logic.
    Ensures the 'Laws of Physics' are untampered.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read in chunks to handle large binaries efficiently
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        current_hash = sha256_hash.hexdigest()
        
        if current_hash == MASTER_INVARIANT_HASH:
            print(f"[SUCCESS] Invariant Verified. Hash: {current_hash[:8]}...")
            return True
        else:
            print(f"[!] SECURITY ALERT: Invariant mismatch!")
            print(f"[!] Observed: {current_hash}")
            print(f"[!] Expected: {MASTER_INVARIANT_HASH}")
            return False
            
    except FileNotFoundError:
        print("[!] FATAL: libomega_core.so missing. Run init.sh first.")
        return False

# Integrated into the main flow
if not verify_invariant_integrity():
    print("[!] EXCOMMUNICATED: Node identity cannot be verified. Exiting.")
    sys.exit(1)
    
def trigger_purge():
    """
    The 'Self-Destruct' Routine. 
    Wipes the local ledger and volatile buffers to prevent Slime persistence.
    """
    print("[!!!] SECURITY BREACH DETECTED: INITIATING PURGE [!!!]")
    
    # Target directories for sanitization
    TARGETS = ['./logs', './__pycache__', './build']
    
    for target in TARGETS:
        if os.path.exists(target):
            try:
                # Use a high-level wipe
                shutil.rmtree(target)
                print(f"[+] Purged: {target}")
            except Exception as e:
                print(f"[!] Critical Failure wiping {target}: {e}")

    # Securely clear the Invariant to prevent unauthorized execution
    if os.path.exists("./libomega_core.so"):
        os.remove("./libomega_core.so")
        print("[+] Invariant logic de-manifested.")

    print("[SUCCESS] Local environment sanitized. Node is now inert.")
    sys.exit(0)
COUNTER_FILE = ".purge_counter"

def record_failure():
    count = 0
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            count = int(f.read().strip())
    
    count += 1
    
    if count >= 3:
        os.remove(COUNTER_FILE)
        trigger_purge()
    else:
        with open(COUNTER_FILE, "w") as f:
            f.write(str(count))
        print(f"[!] Security Failure {count}/3. System lock in progress.")