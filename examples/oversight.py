import pyomega as omega

def audit_national_strata():
	# 1. Pull the Master Orbital Checksum
	trace = omega.OrbitalTrace.get_latest_warp()

	# 2. Audit the National System Mass across all active voxels
	total_mass = omega.Core.get_system_mass_gt()

	# 3. Verify the "Solid Möbius" Integrity
	if trace.is_consistent(total_mass):
		print(f"System Integrity: 100% | Total Mass: {total_mass} GT")
	else:
		# Identify "Slime" (De-synced nodes)
		anomalies = omega.Core.scan_for_jitter()
		print(f"Alert: {len(anomalies)} nodes exhibiting phase friction.")

if __name__ == "__main__":
	audit_national_strata()