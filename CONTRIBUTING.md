# Aqua Chroma Contributor Guide

Thank you for your interest in the National Volumetric Reference Framework (NVRF).
This repository implements tooling that supports a stable, deterministic
reference layer. Contributions are welcome where they strengthen reliability,
clarity, and interoperability.

---

## 1. Repository Model

This project follows an open-interface / protected-core structure:

• SDK Layer (Public Contributions Welcome)
  Python wrappers, CLI tools, synchronization utilities,
  logging systems, tests, and documentation.

• Core Invariant (Maintained Internally)
  The tetrahedral invariant logic located in `/omega`
  and distributed via `libomega_core.so` is maintained
  exclusively by Aqua Chroma to preserve determinism,
  auditability, and physical parity.

External pull requests modifying the invariant layer
cannot be accepted. Improvements may be proposed via
issues or design discussions.

---

## 2. Contribution Workflow

1. Fork the repository and create a feature branch
2. Ensure deterministic execution — no hidden latency,
   race conditions, or non-repeatable timing behavior
3. Add tests when applicable
4. Submit a pull request with a clear explanation of:
   • the problem solved
   • the performance impact
   • compatibility considerations

We prioritize predictable behavior over cleverness.

---

## 3. Contributor License Agreement (CLA)

By submitting a contribution, you agree that:

• You grant Aqua Chroma a perpetual, worldwide,
  non-exclusive, royalty-free license to use,
  modify, distribute, and sublicense your contribution

• Your contribution is original work and you have
  the legal authority to submit it

This ensures the SDK can evolve without ownership
ambiguity or future licensing conflicts.

---

## 4. Coding Standards

• Type Safety  
  Python contributions must use PEP 484 type hints

• Logging  
  Telemetry must use the established `.jsonl` format

• Performance Discipline  
  Avoid heavy dependencies or constructs that
  introduce jitter or unpredictable latency

Determinism is a design constraint, not an optimization.

---
