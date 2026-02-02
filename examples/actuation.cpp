#include <omega/actuation.hpp>
#include <omega/geometry.hpp>

int main() {
    // 1. Initialize the 16-bit Tetrahedral Gradient
    auto gradient = omega::VoxelGradient::initialize(RESOLUTION_16BIT);

    // 2. Connect to the AESA Loom for spatial isolation
    auto loom = omega::AesaLoom::connect();
    loom.set_isolation_zone(-60.0 /* decibels */);

    // 3. Actuate the "Print Head" for a 1.2GT Scalar Mass synthesis
    if (gradient.resynthesize_strata(MATERIAL_FGM_04, 1.2 /* Giga-Tons */)) {
        loom.engage_containment();
        std::cout << "Material Resynthesis: STABILIZED" << std::endl;
    }
    return 0;
}