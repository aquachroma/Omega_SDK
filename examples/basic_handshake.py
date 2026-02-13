"""
Aqua Chroma SDK: Basic Handshake (SOP-01)
Purpose: Verify the three-tier synthesis (C++/Rust/Python) and establish a 
single-voxel sovereign lock.
"""

import sys
import time
from omega.core import establish_sovereignty, check_grid_density

def run_handshake():
	print("--- [AQUA CHROMA] Basic Handshake Initiation ---")
	
	# 1. Verify Grid Density
	# This confirms the autodetect logic from init.sh is active
	print("[*] Phase 1: Verifying Local Node Density...")
	check_grid_density()
	
	# 2. Establish Sovereignty
	# We use a standard test mass of 1.0 Giga-Ton (GT) for the initial anchor
	test_mass = 1.0
	print(f"[*] Phase 2: Attempting Voxel Lock at {test_mass} GT...")
	
	# establish_sovereignty handles the C-Bridge call and logs to the ledger
	success = establish_sovereignty(target_gt=test_mass)
	
	if success:
		print("\n[SUCCESS] Handshake Complete.")
		print("[STATUS] Node is now GRID-COUPLED.")
		print("[NOTE] Telemetry has been recorded in ./logs/ledger_main.jsonl")
	else:
		print("\n[FAILURE] Handshake rejected.")
		print("[REASON] Phase Dissonance exceeded the 0.5ns Guardband.")
		sys.exit(1)

if __name__ == "__main__":
	try:
		run_handshake()
	except KeyboardInterrupt:
		print("\n[!] Handshake aborted by operator.")
	except Exception as e:
		print(f"\n[CRITICAL] Unexpected Dissonance: {e}")