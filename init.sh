#!/bin/bash
# Omega SDK Initialization Forge

echo "=================================================="
echo "    OMEGA SDK: SOVEREIGN NODE INITIALIZATION     "
echo "=================================================="

# 1. Identity Capture
echo "--------------------------------------------------"
echo " [IDENTITY ANCHOR] "
echo " Providing a Registry Handle allows the National Strata"
echo " to attribute your node's stability metrics and grant"
echo " priority access to the 16-bit Invariant Core."
echo "--------------------------------------------------"
read -p "[?] Enter your Sovereign Identity (Handle): " USER_HANDLE

# 2. Sovereign Registration
echo "[*] Generating Hardware Anchor..."
python3 -c "from tools.get_node_fingerprint import register_node; register_node('$USER_HANDLE')"

if [ -f "node_id.json" ]; then
    NODE_HASH=$(python3 -c "import json; print(json.load(open('node_id.json'))['node_hash'])")
    echo "[+] Node Registered Successfully."
    echo "[*] Assigned Node Hash: $NODE_HASH"
else
    echo "[!] Warning: Registry connection failed. Operating in Shadow Mode."
fi

# 3. Environment Prep
mkdir -p logs
touch logs/national_ledger.jsonl

echo "=================================================="
echo "    HANDSHAKE COMPLETE: NODE READY FOR CORE      "
echo "=================================================="