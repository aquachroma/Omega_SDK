import platform
import urllib.request
import json
import os

def install_engine():
	if not os.path.exists("node_id.json"):
		print("[!] No Identity Anchor found.")
		return

	with open("node_id.json", "r") as f:
		identity = json.load(f)
	
	# Detect Architecture and OS
	sys_type = platform.system().lower() # 'linux', 'darwin', or 'windows'
	
	node_hash = identity.get("node_hash")
	# Add 'os' parameter to the request
	url = f"https://aquachroma.com/api/get_core.php?hash={node_hash}&os={sys_type}"
	
	if sys_type == "windows":
		extension = "dll"
		target_path = "omega/omega_core.dll" # Windows usually drops the 'lib' prefix
	else:
		extension = "dylib" if sys_type == "darwin" else "so"
		target_path = f"omega/libomega_core.{extension}"

	print(f"[*] Requesting {sys_type.upper()} Muscle for Node...")
	try:
		urllib.request.urlretrieve(url, target_path)
		print(f"[+] Engine successfully placed: {target_path}")
	except Exception as e:
		print(f"[!] Delivery Failed: {e}")