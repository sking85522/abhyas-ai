# ADR-003: AI Provider Abstraction
**Context**: Preventing vendor lock-in with LLM providers.
**Decision**: Create a `plugins/` abstraction layer for AI models. Direct imports of `google.generativeai` or `openai` in core business logic are prohibited.
