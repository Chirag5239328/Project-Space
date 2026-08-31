# Config-Driven Decision Engine

## Overview

This project is a backend decision engine that evaluates structured records using externally defined rules and produces deterministic decisions with full auditability.

It is designed to simulate how enterprise systems in finance, compliance, HR, and operations enforce policies without hardcoding logic.

The system separates:

- Data
- Policy
- Execution
- Audit
- Reporting

So rules can be changed without changing code.

---

## Key Features

- CSV input validation using Pydantic
- YAML-based rule configuration
- Deterministic rule evaluation
- Priority-based rule resolution
- SQLite audit logging
- Enriched output CSV
- Summary report generation
- Automated test suite

No machine learning is used.
All decisions are rule-based and explainable.

---

## Architecture

Logical pipeline:

```text
Input CSV
   ↓
Schema Validator
   ↓
Rule Loader
   ↓
Rule Engine
   ↓
Audit Logger (SQLite)
   ↓
Output Generator
   ↓
Summary Report
```

---

## Project Structure

```text
config-driven-decision-engine/
│
├── main.py
├── csv_validator.py
├── rules_loader.py
├── rule_schema.py
├── record_schema.py
│
├── engine/
│   └── evaluator.py
│
├── audit/
│   ├── db.py
│   └── logger.py
│
├── ioutput/
│   ├── output_writer.py
│   └── summary.py
│
├── data/
│   ├── input.csv
│   ├── output.csv
│   ├── summary.csv
│   └── audit.db
│
├── tests/
│
├── pytest.ini
└── README.md
```

---

## Input Format

### Input CSV

Each row represents one decision unit.

### Required columns

```text
record_id
age
annual_income
credit_score
country
kyc_verified
requested_amount
employment_type
```

---

## Rule Configuration

Rules are defined in YAML.

### Format

```yaml
rules:
  - rule_id: R001_LOW_CREDIT
    priority: 1
    decision: reject
    stop_on_match: true
    reason: Low credit score
    conditions:
      all:
        - field: credit_score
          operator: "<"
          value: 600
```

### Supported Operators

| Operator | Meaning |
|----------|---------|
| == | Equals |
| != | Not equals |
| < | Less than |
| <= | Less than or equal |
| > | Greater than |
| >= | Greater than or equal |
| between | Range check |
| in | Membership |

### Logical Groups

- all → AND
- any → OR

### Default Rule

A default rule must exist:

```yaml
conditions:
  all: []
```

---

## Decisions

Each record receives exactly one outcome:

- accept
- reject
- review

Rules are evaluated by ascending priority.
First matching rule wins.

---

## Audit Logging

All rule evaluations are stored in SQLite:

### File

```text
data/audit.db
```

### Table

```text
audit_log
```

### Fields

```text
record_id
rule_id
priority
matched
decision
timestamp
```

This enables compliance and traceability.

---

## Output Files

### 1. Decision Output

```text
data/output.csv
```

Contains original fields plus:

- decision
- rule_id
- reason

### 2. Summary Report

```text
data/summary.csv
```

Contains:

- total_records
- accept
- reject
- review
- percentages

---

## Installation

### Requirements

Python 3.9+

pip

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Or manually:

```bash
pip install pandas pydantic pyyaml pytest
```

---

## Running the System

From project root:

```bash
python main.py
```

This will:

- Validate input
- Load rules
- Run engine
- Write audit logs
- Generate output CSV
- Generate summary

---

## Running Tests

Run all automated tests:

```bash
pytest
```

All tests must pass before changes are merged.

---

## Error Handling

- Invalid CSV → validation error
- Invalid rules → configuration error
- Evaluation failure → engine error
- Output issues → IO error

The system fails fast on invalid inputs.

---

## Extending the System

### Adding New Rules

Edit:

```text
rules.yaml
```

No code changes required.

### Changing Input Schema

Modify:

```text
record_schema.py
csv_validator.py
```

The engine does not require modification.

### Adding New Operators

Edit:

```text
engine/operators.py
```

Add function and mapping.

---

## API Integration (Optional)

The engine can be wrapped using FastAPI to support:

- File uploads
- Remote execution
- UI integration

---

## Design Principles

- Configuration over code
- Determinism
- Explainability
- Auditability
- Fail-fast validation
- Separation of concerns

---

## Limitations

- Fixed schema (v1)
- Single-file input
- Local execution only
- No UI (by design)

---

## Future Enhancements

- Configurable schema
- Web UI rule builder
- REST API
- Rule versioning
- Multi-tenant support
- Simulation mode
