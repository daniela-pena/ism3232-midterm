# main.py

from business_rules import (
    calculate_license_total,
    format_license_line,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)

orders = [
    {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
    {"company": "Quarry School", "seat_price": 35.00, "seats": 12, "education": True},
    {"company": "Redwood Cargo", "seat_price": 45.00, "seats": 60, "education": False},
    {"company": "Summit College", "seat_price": 50.00, "seats": 150, "education": True},
    {"company": "Tidal Health", "seat_price": 55.00, "seats": 100, "education": False},
    {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},
    {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},
    {"company": "Willow Law", "seat_price": 400.00, "seats": 9, "education": False},
]

print("Cloudstep Software - Order Report")

for order in orders:
    total = calculate_license_total(
        order["seat_price"], order["seats"], order["education"]
    )
    contract_review_text = needs_contract_review(total)
    trainer = gets_trainer(order["seats"], total)

    print(format_license_line(order["company"], total, contract_review_text, trainer))

order_count = len(orders)
total_license_combined = total_licensed(orders)
avg_license_total = total_license_combined / order_count
largest_company = largest_license(orders)

contract_reviews_needed = 0
for order in orders:
    total = calculate_license_total(
        order["seat_price"], order["seats"], order["education"]
    )
    if needs_contract_review(total):
        contract_reviews_needed += 1

trainers_assigned = 0
for order in orders:
    total = calculate_license_total(
        order["seat_price"], order["seats"], order["education"]
    )
    if gets_trainer(order["seats"], total):
        trainers_assigned += 1

print(f"Orders: {order_count}")
print(f"Total licensed: ${total_license_combined:.2f}")
print(f"Average license total: ${avg_license_total:.2f}")
print(f"Largest license total: {largest_company}")
print(f"Contract reviews needed: {contract_reviews_needed}")
print(f"Trainers assigned: {trainers_assigned}")
