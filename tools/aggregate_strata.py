import json
import os
import statistics

def aggregate_national_ledger():
	"""
	Zero-dependency replacement for Pandas.
	Calculates the full metric set for the National Strata Report.
	"""
	ledger_path = "logs/national_ledger.jsonl"
	if not os.path.exists(ledger_path):
		return None

	# Storage for raw telemetry
	jitters = []
	stabilities = []
	masses = []

	with open(ledger_path, "r") as f:
		for line in f:
			try:
				data = json.loads(line)
				jitters.append(data.get("jitter", 0.0))
				stabilities.append(data.get("stability", 1.0)) # 1.0 = 100%
				masses.append(data.get("mass_gt", 0.0))
			except (json.JSONDecodeError, KeyError):
				continue

	if not jitters:
		return {
			"avg_jitter": 0.0, 
			"avg_stability": 0.0, 
			"total_mass": 0.0,
			"node_count": 0
		}

	return {
		"avg_jitter": statistics.mean(jitters),
		"avg_stability": statistics.mean(stabilities),
		"total_mass": sum(masses),
		"node_count": len(jitters)
	}