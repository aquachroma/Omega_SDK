:: """
:: AQUA CHROMA OMEGA SDK - NATIONAL VOLUMETRIC REFERENCE INTERFACE
:: Copyright (c) 2026 Aqua Chroma. 
:: 
:: TECHNICAL NOTICE: This SDK is a deterministic interface layer. 
:: Modification of the orchestration logic or guardband enforcement routines 
:: may result in a loss of synchronization with the National Strata. 
:: 
:: Interoperability with the high-precision Invariant Core is contingent 
:: upon maintaining the integrity of this routing layer and successful 
:: node-hash validation via the Aqua Chroma Registry.
:: """

@echo off
SETLOCAL
echo ==================================================
echo     OMEGA SDK: SOVEREIGN NODE INITIALIZATION
echo ==================================================

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Please install Python and add it to your PATH.
    pause
    exit /b
)

echo [*] Initializing Identity Anchor...
python tools/get_node_fingerprint.py

if exist node_id.json (
    echo [*] Requesting Engine from National Strata...
    python -c "from tools.fetch_engine import install_engine; install_engine()"
)

echo ==================================================
echo     HANDSHAKE COMPLETE: NODE READY FOR CORE
echo ==================================================
pause
