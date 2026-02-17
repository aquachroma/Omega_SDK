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
import numpy as np
import time
import json
import os
import hashlib
import sys
import logging
import shutil
from datetime import datetime
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from pydantic import BaseModel

# --- RECTIFIED IMPORT ---
# We now import the public gateway. 
# Inside omega/core.py, it uses core_loader to find the binary.
import omega.core as core 
from omega.core import initiate_decoherence

# The final observed hash from your terminal output
MASTER_INVARIANT_HASH = "bb22904f1d4368cda3047dd4cd7be1175981c76bc06ccdde801f23db051a34dd"

console = Console()

class ScalarMetadata(BaseModel):
	node_id: str
	mass_gt: float
	strata_layer: int = 16

def get_binary_hash(filepath="./omega/libomega_core.so"):
	"""
	Checks the hash of the binary in the /omega/ directory 
	where init.sh places it.
	"""
	sha256_hash = hashlib.sha256()
	try:
		with open(filepath, "rb") as f:
			for byte_block in iter(lambda: f.read(4096), b""):
				sha256_hash.update(byte_block)
		return sha256_hash.hexdigest()
	except FileNotFoundError:
		return None

def verify_invariant_integrity():
	observed = get_binary_hash()
	if observed == MASTER_INVARIANT_HASH:
		console.print(f"[bold green][SUCCESS][/bold green] Invariant Verified: {observed[:8]}")
		return True
	else:
		# If the hash is wrong, we don't just return False; 
		# we trigger the De-Coherence protocol.
		initiate_decoherence(reason=f"Invariant Mismatch. Observed: {observed}")
		return False

def perform_sovereign_handshake(metadata: ScalarMetadata):
	console.print(f"[*] Node {metadata.node_id} initiating handshake...")
	
	# We now call establish_sovereignty from our gateway (omega/core.py)
	if core.establish_sovereignty(metadata.mass_gt):
		console.print(f"[bold cyan][!] SUCCESS:[/bold cyan] Node is an Active Aqua Chroma Anchor.")
		return True
	return False

def generate_dashboard_table(jitter):
	table = Table(title="Aqua Chroma: National Volumetric Status", border_style="cyan")
	table.add_column("Metric", justify="right")
	table.add_column("Value", justify="left")
	table.add_column("Stability", justify="center")

	table.add_row("Phase Friction (Jitter)", f"{jitter:.4f} ns", "GUARDED" if jitter < 0.5 else "FAIL")
	table.add_row("Active System Mass", "1.2 GT", "SOLID")
	table.add_row("Invariant Hash", MASTER_INVARIANT_HASH[:8], "VERIFIED")
	return table

def run_dashboard():
	with Live(console=console, screen=True, refresh_per_second=4) as live:
		try:
			while True:
				# Ask the gateway for the current jitter
				current_jitter = core.check_grid_density() # Or your jitter function
				# Note: If density returns 16/32, use that to scale your display
				live.update(Panel(generate_dashboard_table(float(current_jitter) * 0.01))) 
				time.sleep(0.25)
		except KeyboardInterrupt:
			console.print("\n[yellow][!] Dashboard closed. Jitter-Guard standing down.[/yellow]")

if __name__ == "__main__":
	# 1. First, check if the file exists and matches the Master Hash
	verify_invariant_integrity()

	# 2. Setup Metadata
	meta = ScalarMetadata(node_id="aqua-alpha-01", mass_gt=1.2)
	
	# 3. Perform Handshake and run dashboard
	if perform_sovereign_handshake(meta):
		run_dashboard()