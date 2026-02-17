"""
AQUA CHROMA OMEGA SDK - NATIONAL VOLUMETRIC REFERENCE INTERFACE
Copyright (c) 2026 Aqua Chroma. 

TECHNICAL NOTICE: This SDK is a deterministic interface layer. 
Modification of the orchestration logic or guardband enforcement routines 
may result in a loss of synchronization with the National Strata. 

Interoperability with the high-precision Invariant Core is contingent 
upon maintaining the integrity of this routing layer and successful 
node-hash validation via the Aqua Chroma Registry.
"""
# omega/core_loader.py
import os
import ctypes
import sys

def load_lib():
	sys_name = platform.system()
	if sys_name == "Windows":
		lib_name = "omega_core.dll"
	elif sys_name == "Darwin":
		lib_name = "libomega_core.dylib"
	else:
		lib_name = "libomega_core.so"
		
	lib_path = os.path.join(os.path.dirname(__file__), lib_name)
	
	if os.path.exists(lib_path):
		return ctypes.CDLL(lib_path)
	return None

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
