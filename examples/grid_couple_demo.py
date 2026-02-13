"""
Example: Grid-Coupling a Local Node.
Demonstrates the transition from an autonomous (indeterminte) state 
to a coupled (deterministic) state within the National Strata.
"""
from omega_sync import ScalarMetadata, perform_sovereign_handshake

def initialize_grid_coupling():
	# Define the target mass for the deterministic lock
	meta = ScalarMetadata(node_id="seattle-hub-01", mass_gt=1.2)
	
	print("--- Initiating Grid-Coupled Deterministic Lock ---")
	
	# The Handshake establishes the reference parity
	if perform_sovereign_handshake(meta):
		print("[STATUS] Local Node: COUPLED")
		print("[STATUS] State: DETERMINISTIC")
	else:
		print("[ERROR] Indeterminacy threshold exceeded during coupling.")

if __name__ == "__main__":
	initialize_grid_coupling()