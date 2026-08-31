import csv
import random
import string
import sys

ALLOWED_EMPLOYMENT_TYPES = ["salaried", "self_employed", "unemployed"]
ALLOWED_COUNTRIES = ["IN", "US", "UK", "DE", "SG"]

CSV_HEADERS = [
    "record_id",
    "age",
    "annual_income",
    "credit_score",
    "country",
    "kyc_verified",
    "requested_amount",
    "employment_type",
]

def generate_record_id(existing_ids, index):
    while True:
        record_id = f"R{index:05d}"
        if record_id not in existing_ids:
            return record_id

def generate_row(existing_ids, index):
    age = random.randint(18, 75)

    annual_income = random.randint(100_000, 2_000_000)

    credit_score = random.randint(300, 900)

    country = random.choice(ALLOWED_COUNTRIES)

    kyc_verified = random.choice([True, False])

    requested_amount = random.randint(50_000, 1_500_000)

    employment_type = random.choice(ALLOWED_EMPLOYMENT_TYPES)

    record_id = generate_record_id(existing_ids, index)
    existing_ids.add(record_id)

    return [
        record_id,
        age,
        annual_income,
        credit_score,
        country,
        str(kyc_verified).lower(),
        requested_amount,
        employment_type,
    ]

def validate_row(row):
    record_id, age, income, credit_score, country, kyc, amount, employment = row

    if not record_id or not isinstance(record_id, str):
        raise ValueError("Invalid record_id")

    if not (18 <= int(age) <= 100):
        raise ValueError("Invalid age")

    if int(income) <= 0:
        raise ValueError("Invalid annual_income")

    if not (300 <= int(credit_score) <= 900):
        raise ValueError("Invalid credit_score")

    if not country or not isinstance(country, str):
        raise ValueError("Invalid country")

    if kyc not in ["true", "false"]:
        raise ValueError("Invalid kyc_verified")

    if int(amount) <= 0:
        raise ValueError("Invalid requested_amount")

    if employment not in ALLOWED_EMPLOYMENT_TYPES:
        raise ValueError("Invalid employment_type")

def main():
    try:
        num_rows = int(input("Enter number of records to generate: ").strip())
        if num_rows <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive integer.")
        sys.exit(1)

    output_file = "input.csv"
    existing_ids = set()

    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(CSV_HEADERS)

        for i in range(1, num_rows + 1):
            row = generate_row(existing_ids, i)
            validate_row(row)
            writer.writerow(row)

    print(f"Successfully generated {num_rows} records in '{output_file}'")

if __name__ == "__main__":
    main()
