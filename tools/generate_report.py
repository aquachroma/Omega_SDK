import os
import json
from datetime import datetime
# Import the aggregator logic from the sibling file
from tools.aggregate_strata import aggregate_national_ledger

def generate_strata_report(target_gt="1,000.00", orbital_status="LOCKED"):
	"""
	Final Synthesis: Injects live telemetry into the 
	National Strata Report template using dynamic variable injection.
	"""
	# Inside generate_strata_report()
	metrics = aggregate_national_ledger()
	
	if not metrics:
		print("[!] Aborting: No telemetry data available to solidify.")
		return

	# 2. Determine System Coherence State
	# If jitter exceeds the 0.5ns guardband, the state is DEGRADED
	is_stable = metrics['avg_jitter'] < 0.5
	system_state = "SOLIDIFIED" if is_stable else "DEGRADED / PHASE FRICTION"

	# 3. Map Live Data to Template Tags
	replacements = {
		"{{TOTAL_GT}}": f"{metrics['total_mass']:.2f}",
		"{{TARGET_GT}}": target_gt,
		"{{COHERENCE_SCORE}}": f"{metrics['avg_stability'] * 100:.2f}%",
		"{{AVG_JITTER}}": f"{metrics['avg_jitter']:.4f} ns",
		"{{SYSTEM_STATE}}": "SOLIDIFIED" if metrics['avg_jitter'] < 0.5 else "DEGRADED",
		"{{TIMESTAMP}}": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	}

	# 4. Read the Template
	template_path = "docs/summary_template.md"
	if not os.path.exists(template_path):
		print(f"[!] Template missing at {template_path}. Using fallback layout.")
		template_content = "# National Strata Report\nStatus: {{SYSTEM_STATE}}\nCoherence: {{COHERENCE_SCORE}}"
	else:
		with open(template_path, "r") as f:
			template_content = f.read()

	# 5. Perform the Handshake (Inject data into template)
	final_report = template_content
	for tag, value in replacements.items():
		final_report = final_report.replace(tag, str(value))

	# 6. Secure the Output
	os.makedirs("reports", exist_ok=True)
	report_filename = f"reports/strata_report_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
	
	with open(report_filename, "w") as f:
		f.write(final_report)

	print(f"[+] Synthesis Complete: {report_filename}")
	print(f"[*] Guardband Status: {system_state}")

if __name__ == "__main__":
	# In production, these variables would be passed from the SDK Orchestrator
	generate_strata_report(target_gt="1,000.00", orbital_status="LOCKED")