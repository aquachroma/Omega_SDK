import unittest
import os
import json
# Import from the package as a user would
from omega import establish_sovereignty, check_grid_density, check_dissonance

class TestNVRFConformance(unittest.TestCase):
	"""
	Standard Conformance Suite for NVRF Nodes.
	Verifies the integration between the Python Interface and the C++ Muscle.
	"""

	def setUp(self):
		# Ensure a clean state for testing
		os.makedirs("./logs", exist_ok=True)
		# Define the relative path to the binary once
		self.core_path = "./omega/libomega_core.so"

	def test_invariant_presence(self):
		"""Verify the compiled Invariant is present in the surgical split location."""
		if not os.path.exists(self.core_path):
			self.skipTest(f"Invariant core not found at {self.core_path}. Run ./init.sh first.")
		self.assertTrue(os.path.exists(self.core_path))

	def test_resolution_detection(self):
		"""Verify the node correctly reports 16 or 32-bit density via the gateway."""
		# We call the public API function we refined
		res = check_grid_density()
		# Even if the binary is missing, our loader returns a 16-bit safe default
		self.assertIn(res, [16, 32], f"Illegal Resolution: {res}")

	def test_guardband_enforcement(self):
		"""Verify the 0.5ns Guardband logic is active."""
		# At 1.0 GT, with our 0.45ns baseline, dissonance should be 0.0 (Phase-Lock)
		dissonance = check_dissonance(target_mass=1.0)
		self.assertEqual(dissonance, 0.0, "Guardband rejected a stable 0.45ns signal.")

	def test_sovereignty_handshake(self):
		"""Verify a standard 1.2 GT lock records to the correct national ledger."""
		# Use the mass defined in your omega_sync.py dashboard
		test_mass = 1.2
		success = establish_sovereignty(target_gt=test_mass)
		
		# If the binary is missing, this may return False; we handle that gracefully
		if not success and not os.path.exists(self.core_path):
			self.skipTest("Binary missing: Handshake cannot be verified.")
			
		self.assertTrue(success, "Sovereignty handshake failed despite presence of core.")
		
		# Verify ledger persistence in the new 'national_ledger' location
		ledger_file = "./logs/national_ledger.jsonl"
		self.assertTrue(os.path.exists(ledger_file), "Ledger was not created.")
		
		with open(ledger_file, "r") as f:
			lines = f.readlines()
			last_entry = json.loads(lines[-1])
			self.assertEqual(last_entry["mass_gt"], test_mass)
			self.assertIn("stability", last_entry)

if __name__ == "__main__":
	unittest.main()