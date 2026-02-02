#include <omega.hpp>

void activate_loom() {
    auto loom = omega::AesaLoom::connect();
    // Direct interaction with the Invariant's beamsteering logic
    loom.enforce_isolation(-60.0 /* dB */);
}