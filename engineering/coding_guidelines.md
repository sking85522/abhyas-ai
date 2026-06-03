# Coding Guidelines

1. **Service Isolation**: Absolutely no cross-imports between services.
2. **Configuration**: Use `pydantic-settings` for all configurations. Never hardcode secrets.
3. **Typing**: Enforce strict type hints on all function signatures.
4. **Code Format**: Use `black` and `isort` for Python formatting.
