# GitHub Copilot Instructions for NeuroLift Technologies

These instructions guide GitHub Copilot when working on any repository in the NeuroLift Technologies organization.

## Project Context

NeuroLift Technologies builds AI-powered tools and platforms focused on cognitive enhancement and developer productivity. Our projects include:
- Python-based machine learning libraries
- Web applications (TypeScript/React frontend, Python/Node.js backend)
- Developer tooling and CLI utilities

## Coding Standards

- **Python**: Follow PEP 8; use type hints; prefer `dataclasses` or `pydantic` models for structured data.
- **TypeScript/JavaScript**: Use strict TypeScript types; prefer functional patterns; use `const` over `let` where possible.
- **Tests**: Write tests for all new functionality. Use `pytest` for Python and `vitest` or `jest` for TypeScript.
- **Documentation**: Write clear docstrings (Google-style for Python, JSDoc for TypeScript/JavaScript).
- **Security**: Never hardcode secrets. Use environment variables for credentials and sensitive configuration.

## Conventions

- Keep functions small and focused on a single responsibility.
- Prefer explicit error handling over silent failures.
- Use descriptive variable and function names; avoid single-letter names outside of loop indices.
- Commit messages should use the imperative mood (e.g., "Add user authentication" not "Added user authentication").

## Pull Requests

- Reference the related issue number in the PR description.
- Keep PRs small and focused — one feature or fix per PR.
- Always fill in the PR template fully.
