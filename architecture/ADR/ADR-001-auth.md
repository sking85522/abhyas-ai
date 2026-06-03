# ADR-001: Authentication Strategy
**Context**: We need a highly scalable, stateless authentication mechanism for the SaaS platform.
**Decision**: Use JWT (JSON Web Tokens) with Passlib for hashing.
**Consequences**: Services can independently verify tokens using a shared secret without querying the central auth database, reducing latency.
