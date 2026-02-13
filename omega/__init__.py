"""
Aqua Chroma SDK: Public API Surface
Providing a stable interface for National Volumetric Reference synchronization.
"""

from .core_loader import load_invariant_core

# Initialize the core handle for the package
try:
	_core_handle = load_invariant_core()
except RuntimeError:
	_core_handle = None

# Import the logic-layer functions from core.py
from .core import (
	establish_sovereignty, 
	check_grid_density, 
	initiate_decoherence,
	check_dissonance  # <--- Now exported from the SDK core
)

__all__ = [
	"establish_sovereignty", 
	"check_grid_density",
	"initiate_decoherence",
	"check_dissonance"
]

__version__ = "0.1.0-alpha"