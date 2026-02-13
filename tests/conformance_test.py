"""
Aqua Chroma SDK: Conformance Suite (v0.1.0-alpha)
Identifies the gap between 'Skeleton' intent and 'Muscle' execution.
"""

import unittest
import os
import json
from omega.core import establish_sovereignty, check_grid_density

class TestNVRFConformance(unittest.TestCase):

	def test_01_library_presence(self):
		"""Verify the Invariant Muscle is synthesized."""
		self.assertTrue(os.path.exists("./libomega_core.so"), 
						"libomega_core.so missing. Run ./init.sh first.")

	def test_02_resolution_handshake(self):
		"""Verify the Python layer can read the compiled-in Resolution."""
		# This checks if our -DSTRATA_RESOLUTION flag worked
		try:
			from omega.core import _lib
			res = _lib.get_node_resolution()
			self.assertIn(res, [16, 32], f"Invalid Resolution detected: {res}")
			print(f"  [CONF] Detected {res}-bit hardware profile.")
		except Exception as e:
			self.fail(f"Could not query node resolution: {e}")

	def test_03_deterministic_lock_sim(self):
		"""Verify a standard 1.0 GT Voxel Lock produces a valid ledger entry."""
		# Ensure log dir exists
		os.makedirs("./logs", exist_ok=True)
		
		# Attempt lock
		success = establish_sovereignty(target_gt=1.0)
		self.assertTrue(success, "Voxel solidification failed during conformance check.")
		
		# Verify the Ledger entry
		with open("./logs/ledger_main.jsonl", "r") as f:
			last_entry = json.loads(f.readlines()[-1])
			self.assertEqual(last_entry["mass_gt"], 1.0)
			self.assertIn("jitter_ns", last_entry)
			print(f"  [CONF] Ledger integrity verified. Jitter: {last_entry['jitter_ns']}ns")

if __name__ == "__main__":
	print("--- [AQUA CHROMA] Starting Conformance Harness ---")
	unittest.main()
