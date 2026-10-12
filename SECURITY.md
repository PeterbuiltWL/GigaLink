# Security & Architectural Boundaries

## Open-Source Scope
This repository (`01_GIGALINK_TELECOM`) contains only the public acoustic transport layer, including audio signal generation, frequency modulation, demodulation, and basic error-checking math.

## Explicit System Exclusions
To maintain zero-trust security and data sovereignty, the following proprietary systems are intentionally excluded from this public repository:
- Sharding Key Protocol (SKP) logic and node rehydration algorithms
- Secure Digital Identity Key (SDK) credential issuance and verification
- Private vault architecture, master keys, and user access management
- Internal business logic, financial data, and operational systems

If you discover a vulnerability within this transport layer, please report it responsibly via GitHub Issues.
