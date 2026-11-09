
import csv
from pathlib import Path

# Locate the tariff CSV file
csv_path = (
    Path(__file__).parent
    / "data"
    / "electricity"
    / "tariff_rates.csv"
)

# Read the CSV file
with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

# Select domestic tariff records
domestic_rows = [
    row for row in rows
    if row["tariff_category"].strip().upper() == "LT-IA"
]

print("Tamil Nadu Domestic Electricity Tariff")
print("Effective from: 01-07-2025\n")

for row in domestic_rows:
    print("Consumption:", row["slab_or_time_slot"])
    print("Energy charge: Rs.", row["energy_charge_rs_per_unit"], "per unit")
    print("-----------------------------")

print("Total domestic slabs:", len(domestic_rows))
