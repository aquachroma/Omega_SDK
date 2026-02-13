# omega/core_loader.py
import os
import ctypes
import sys

def load_invariant_core():
	"""
	The 'Sovereign Loader'. Attempts to find the Engine Block.
	"""
	# 1. Check for installed package (The 'Private Wheel' approach)
	try:
		import omega_core_native
		return omega_core_native.get_core()
	except ImportError:
		pass

	# 2. Check for Environment Variable (The 'Developer Override')
	env_path = os.getenv("OMEGA_CORE_PATH")
	if env_path and os.path.exists(env_path):
		return ctypes.CDLL(env_path)

	# 3. Fallback: The 'Caliper Error'
	print("-" * 50)
	print("CORE INVARIANT NOT FOUND")
	print("Mission: Aqua Chroma Environmental Rectification")
	print("Status: Restricted / Unauthorized")
	print("-" * 50)
	raise RuntimeError(
		"Mechanical Invariant (libomega_core) is missing.\n"
		"Please visit aquachroma.com to authenticate and obtain the core binary."
	)
