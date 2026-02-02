use omega_core::Invariant;

pub fn trace_warp() -> Result<(), OmegaError> {
    let mut lock = Invariant::new()?;
    // Safe wrapper around the raw .so pointer
    lock.sync_with_neutrino()?;
    Ok(())
}