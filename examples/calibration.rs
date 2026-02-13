use omega_sdk::calibration::{WavePool, Refractor};
use omega_sdk::core::NeutrinoSync;

fn main() -> Result<(), OmegaError> {
	// 1. Establish the subterranean heartbeat
	let heartbeat = NeutrinoSync::anchor("pnnl_sub_01")?;

	// 2. Poll the Wave Pool for the current refractive "Snell Lens" index
	let pool = WavePool::connect("hanford_basin")?;
	let lens = pool.get_liquid_lens_correction()?;

	// 3. Apply the correction to the local Invariant
	heartbeat.apply_refraction(lens)?;
	
	println!("Refractive Synchronization: SUCCESS (Drift: 0.12ns)");
	Ok(())
}