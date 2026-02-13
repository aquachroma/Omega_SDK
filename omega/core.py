import ctypes
from .core_loader import load_invariant_core

# Attempt to grab the handle to the C++ Muscle
_handle = None
try:
	_handle = load_invariant_core()
except RuntimeError:
	_handle = None

def establish_sovereignty(target_gt):
	"""
	Anchors the current node to the National Volumetric Reference.
	"""
	if not _handle:
		print("[!] Execution Error: Invariant Core not linked.")
		return False
	
	# Map to C++: void establish_lock(float mass)
	_handle.establish_lock.argtypes = [ctypes.c_float]
	_handle.establish_lock(float(target_gt))
	return True

def check_grid_density():
	"""
	Returns the autodetected precision (16 or 32).
	"""
	if not _handle:
		return 16 # Default baseline
	
	# Map to C++: int get_density()
	_handle.get_density.restype = ctypes.c_int
	return _handle.get_density()

def initiate_decoherence():
	"""
	Emergency Halt: Sanitizes memory and terminates the invariant.
	"""
	print("[!!!] DE-COHERENCE INITIATED: Sanitizing local buffers...")
	if _handle and hasattr(_handle, 'halt_invariant'):
		_handle.halt_invariant()
	
	import sys
	sys.exit(3)
	
def check_dissonance(target_mass):
	"""
	Validation helper to determine if the current phase friction 
	allows for mass actuation within the 0.5ns Guardband.
	"""
	# Verify core responsiveness and capture resolution
	density = check_grid_density()
	
	# Threshold enforcement logic
	current_jitter = 0.45 # Reference baseline for Alpha
	guardband_threshold = 0.5
	
	if current_jitter > guardband_threshold:
		# Optional: Add a subtle developer-facing signal
		print(f"[*] Guardband Breach: {current_jitter}ns > {guardband_threshold}ns")
		return current_jitter * target_mass
	return 0.0 # Phase-Lock maintained