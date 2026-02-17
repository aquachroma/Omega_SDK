import unittest
import ctypes
import os

class TestOmegaCore(unittest.TestCase):
    def setUp(self):
        lib_path = os.path.abspath("omega/libomega_core.dylib")
        self.core = ctypes.CDLL(lib_path)
        self.core.get_voxel_integrity.restype = ctypes.c_float

    def test_initialization(self):
        # This will trigger the [CORE] print statements
        self.core.initialize_strata()
        
    def test_integrity_threshold(self):
        integrity = self.core.get_voxel_integrity()
        self.assertGreater(integrity, 0.95, "Voxel Integrity below Sovereign threshold!")

if __name__ == "__main__":
    unittest.main()
