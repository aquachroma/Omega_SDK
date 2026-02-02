import ctypes
from pyomega import Voxel

# Least Resistance: High-level abstraction of the C-Bridge
def establish_sovereignty(target_gt):
    # Calls libomega_core.so:omega_sync_lock under the hood
    if Voxel.lock(mass=target_gt):
        print("Voxel Solidified.")