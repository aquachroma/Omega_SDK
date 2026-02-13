import hashlib
import platform
import subprocess
import json
import urllib.request
import time

def generate_fingerprint():
    sys_info = f"{platform.system()}-{platform.node()}-{platform.machine()}"
    try:
        if platform.system() == "Darwin":
            cmd = "ioreg -rd1 -c IOPlatformExpertDevice | grep IOPlatformUUID"
        else:
            cmd = "cat /etc/machine-id"
        hw_id = subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        hw_id = "UNANCHORED-NODE"
    return hashlib.sha256(f"{sys_info}-{hw_id}".encode()).hexdigest()

def register_node(handle):
    """
    Connects to the Aqua Chroma Registry to anchor this node.
    """
    fingerprint = generate_fingerprint()
    url = "https://aquachroma.com/api/register.php"
    
    payload = {
        "handle": handle,
        "fingerprint": fingerprint,
        "timestamp": time.time()
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    print(f"[*] Connecting to Aqua Chroma Registry for {handle}...")
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode())
            # Save the node_id.json locally
            with open("node_id.json", "w") as f:
                json.dump(res_data, f, indent=4)
            return True
    except Exception as e:
        # Fallback for offline/unauthorized nodes
        fallback_id = {"node_hash": f"OFFLINE-{fingerprint[:8]}", "status": "UNANCHORED"}
        with open("node_id.json", "w") as f:
            json.dump(fallback_id, f, indent=4)
        return False

if __name__ == "__main__":
    # If run directly, just show the fingerprint
    print(generate_fingerprint())