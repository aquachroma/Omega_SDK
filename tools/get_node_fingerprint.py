import hashlib
import platform
import subprocess
import json
import urllib.request
import time
import os

def generate_fingerprint():
    # Use .format() for Ubuntu 16.04 compatibility
    sys_info = "{}-{}-{}".format(platform.system(), platform.node(), platform.machine())
    try:
        if platform.system() == "Darwin":
            cmd = "ioreg -rd1 -c IOPlatformExpertDevice | grep IOPlatformUUID"
        else:
            cmd = "cat /etc/machine-id"
        hw_id = subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        hw_id = "UNANCHORED-NODE"
    
    combined = "{}-{}".format(sys_info, hw_id)
    return hashlib.sha256(combined.encode()).hexdigest()

def register_node(handle):
    fingerprint = generate_fingerprint()
    url = "https://aquachroma.com/api/register.php"
    
    payload = {
        "handle": handle,
        "fingerprint": fingerprint,
        "timestamp": time.time()
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    print("[*] Connecting to Aqua Chroma Registry for {}...".format(handle))
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode())
            with open("node_id.json", "w") as f:
                json.dump(res_data, f, indent=4)
            return True
    except Exception as e:
        # Avoid f-strings even in error handling
        short_fp = fingerprint[:8]
        fallback_id = {"node_hash": "OFFLINE-{}".format(short_fp), "status": "UNANCHORED"}
        with open("node_id.json", "w") as f:
            json.dump(fallback_id, f, indent=4)
        return False

if __name__ == "__main__":
    print(generate_fingerprint())
