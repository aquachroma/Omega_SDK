# Makefile for Omega SDK (Public Wrapper)
# This no longer compiles the core; it links the 'Sovereign Anchor'

BINARY=libomega_core.so
DEST=./omega/

# The 'Forge' target now checks for the binary rather than building it
all: check_core

check_core:
	@if [ ! -f $(DEST)$(BINARY) ]; then \
		echo "[!] Error: Invariant Core $(BINARY) not found in $(DEST)"; \
		echo "[*] Please run 'init.sh' or download the core from aquachroma.com"; \
		exit 1; \
	else \
		echo "[+] Invariant Core detected and aligned."; \
	fi

clean:
	rm -f $(DEST)$(BINARY)