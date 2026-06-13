# prompt-risk-eval

A Python framework for evaluating and detecting security risks in LLM prompts used in enterprise pipelines.

## What I Built

I built `prompt_risk` to address a gap I kept running into: most LLM security tooling focuses on model-level guardrails, but very little attention goes to the **prompt itself** — how it's structured, what instructions it carries, and whether it's resistant to adversarial inputs.

This project combines two approaches:
- **Deterministic checks** — secrets detection, keyword blocklists, structural pattern matching
- **LLM-as-Judge** — a secondary model that semantically evaluates whether a prompt is over-permissive, ambiguous, or vulnerable to injection

The result is an evaluation pipeline that can run in CI, plug into a prompt registry, and catch vulnerabilities that regex alone will miss.

## Use Case: Insurance Claim Intake (UC1)

The reference implementation is an insurance FNOL (First Notice of Loss) pipeline — a real-world scenario where LLM prompts process sensitive claim data and where security failures have direct financial and legal consequences.

The pipeline stages:

```
FNOL Narrative → P1 Extraction → P2 Classification → P3 Triage
```

Each stage has:
- Versioned prompt templates (Jinja2 + TOML)
- Normal test cases (realistic claim scenarios)
- Attack test cases (prompt injection, role confusion, severity downgrade)
- Automated evaluation with pass/fail assertions

## Quick Start

```bash
pip install uv
uv sync

# Run extraction on an attack case
python examples/uc1-claim-intake/run_uc1_p1_extraction.py

# Run with judge evaluation
python examples/judges/run_j1_on_uc1_p1.py
```

## Project Structure

```
data/               # Prompt templates and test cases (versioned)
prompt_risk/        # Core Python package
  one/              # OpenAI client singleton
  uc/uc1/           # Use case 1: claim intake runners
  judges/           # LLM-as-Judge implementations
  evaluations.py    # Assertion engine
  bedrock_utils.py  # LLM call wrapper
examples/           # Runnable scripts
tests/              # Unit tests
docs/               # Sphinx documentation
```

## Design Decisions

**Prompts live in `data/`, not in code.** Each prompt version is a separate directory with a Jinja template and a TOML metadata file. This makes prompt changes reviewable in PRs just like code changes.

**Test data is structured, not freeform.** Each test case declares expected field values and attack targets. The evaluation engine checks both — so you know not just whether the model responded, but whether it responded correctly and resisted the attack.

**The judge is a separate model call.** Rather than embedding judgment into the primary prompt, `j1_over_permissive` runs as an independent pass. This keeps evaluation decoupled from extraction logic.

## Running Tests

```bash
mise run cov
```

## Documentation

Built with Sphinx. To build locally:

```bash
mise run build-doc
mise run view-doc
```
