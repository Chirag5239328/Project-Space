import sys
import os
import csv

from core.schema.schema_inferer import SchemaInferer
from core.validation.dynamic_validator import DynamicValidator
from core.rules.json_rule_loader import JSONRuleLoader
from core.rules.rule_adapter import RuleAdapter
from core.engine.evaluator import RuleEvaluator
from audit.db import init_db
from audit.logger import AuditLogger
from io_utils.output_writer import OutputWriter
from io_utils.summary import SummaryReport


class RunnerError(Exception):
    pass


def load_csv_rows(path: str):

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def run_engine(input_csv: str, rules_file: str, output_dir: str):

    if not os.path.exists(input_csv):
        raise RunnerError("Input CSV not found")

    if not os.path.exists(rules_file):
        raise RunnerError("Rules file not found")

    os.makedirs(output_dir, exist_ok=True)

    print("Step 1: Loading CSV")
    raw_rows = load_csv_rows(input_csv)

    if not raw_rows:
        raise RunnerError("CSV has no data")

    print("Step 2: Inferring schema")
    inferer = SchemaInferer()
    schema = inferer.infer(input_csv)

    print("Step 3: Building validator")
    validator = DynamicValidator(schema)

    print("Step 4: Validating rows")
    validated = []

    for row in raw_rows:
        rec = validator.validate(row)
        validated.append(rec)

    print("Step 5: Loading rules")
    loader = JSONRuleLoader(schema)
    json_rules = loader.load(rules_file)

    print("Step 6: Adapting rules")
    adapter = RuleAdapter()
    ruleset = adapter.adapt(json_rules)

    print("Step 7: Initializing audit DB")
    db_path = os.path.join(output_dir, "audit.db")

    if os.path.exists(db_path):
        os.remove(db_path)

    init_db(db_path)

    audit_logger = AuditLogger(db_path)

    print("Step 8: Running engine")
    evaluator = RuleEvaluator(ruleset, audit_logger)

    decisions = []

    for record in validated:
        decision = evaluator.evaluate(record)
        decisions.append(decision)

    print("Step 9: Writing output CSV")
    out_csv = os.path.join(output_dir, "output.csv")

    writer = OutputWriter(out_csv)
    writer.write(raw_rows, decisions)

    print("Step 10: Writing summary")
    summary_path = os.path.join(output_dir, "summary.csv")

    report = SummaryReport(summary_path)
    data = report.generate(decisions)
    report.write_csv(data)

    print("\nRun completed successfully.")
    print(f"Output directory: {output_dir}")


def main():

    if len(sys.argv) != 4:
        print(
            "Usage: python run_engine.py <input.csv> <rules.json> <output_dir>"
        )
        sys.exit(1)

    try:
        run_engine(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()