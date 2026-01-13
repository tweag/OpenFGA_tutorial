# GitHub Copilot Custom Instructions

## Python Development Guidelines

When working with Python files in this repository, follow these principles inspired by the Zen of Python:

### Code Style and Readability

- **Beautiful is better than ugly**: Write clean, aesthetically pleasing code with consistent formatting
- **Explicit is better than implicit**: Use clear variable names, explicit type hints, and avoid magic behavior
- **Readability counts**: Prioritize code clarity over cleverness; code is read more often than written

### Code Structure

- **Simple is better than complex**: Favor straightforward solutions over unnecessarily complicated ones
- **Complex is better than complicated**: When complexity is needed, ensure it's well-structured and understandable
- **Flat is better than nested**: Avoid deep nesting; use early returns and guard clauses
- **Sparse is better than dense**: Use whitespace appropriately to improve readability

### Design Principles

- **There should be one-- and preferably only one --obvious way to do it**: Follow established patterns in the codebase
- **Namespaces are one honking great idea**: Use clear module organization and avoid polluting the global namespace
- **Special cases aren't special enough to break the rules**: Maintain consistency across the codebase

### Error Handling

- **Errors should never pass silently**: Always handle exceptions appropriately
- **Unless explicitly silenced**: When ignoring errors, document why with clear comments
- **In the face of ambiguity, refuse the temptation to guess**: Validate assumptions and fail fast when uncertain

### Implementation

- **If the implementation is hard to explain, it's a bad idea**: Prefer solutions that are easy to understand and document
- **If the implementation is easy to explain, it may be a good idea**: Simple, explainable solutions are often the best
- **Now is better than never**: Don't over-engineer; deliver working solutions iteratively
- **Although never is often better than *right* now**: Balance speed with quality; avoid hasty implementations

### Specific Practices for This Repository

- Use type hints (from `typing` module) for function parameters and return values
- Follow PEP 8 style guidelines for Python code
- Write docstrings for all public functions, classes, and modules
- Use Pydantic models for data validation where appropriate
- Handle async operations properly with `async`/`await` keywords
- Keep functions focused and single-purpose
- Use context managers (`with` statements) for resource management
- Prefer list comprehensions over `map`/`filter` when they improve readability
