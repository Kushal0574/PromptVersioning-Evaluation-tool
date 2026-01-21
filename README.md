# PromptOps — Prompt Versioning & Evaluation Tool

PromptOps is a CLI-first tool for **versioning, evaluating, and regression-testing prompts
backed by SQLite. It mirrors real-world LLM experimentation workflows.

## Features
- Prompt versioning with metadata
- SQLite-backed persistence
- Evaluation pipelines
- Scoring + regression detection
- Clean modular architecture


## Architecture
- `cli.py` — CLI entry point
- `db.py` — SQLite persistence
- `models.py` — Core domain models
- `versioning.py` — Prompt lifecycle logic
- `evaluation.py` — Evaluation engine
- `scoring.py` — Scoring + regression checks
- `config.py` — Config management
- `utils.py` — Shared helpers

## Why this matters
This tool demonstrates how real AI teams manage prompt evolution,
reproducibility, and quality drift — not just prompt experimentation.

## Example
```bash
python cli.py add --name "summarizer" --content "Summarize text clearly"
python cli.py eval --name "summarizer"
```
