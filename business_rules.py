# business_rules.py
# Author: Daniela Pena

general_discount_seat_min = 10

onboarding_fee = 60.00
onboarding_fee_limit = 400.00
contract_review_limit = 5000.00
trainer_seat_min = 25
trainer_license_limit = 3000.00

def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Return license cost before any discount."""
    return seat_price * seats

def get_seat_discount(seats: int, education: bool = False) -> float:
    """Returns the discount rate as a decimal based on seats and customer type."""
    if seats < general_discount_seat_min:
        return 0.00
    elif seats < 50:
        return 0.07
    elif education:
        return 0.16
    else:
        return 0.07

def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
    """Returns the license total for one order."""
    license_cost = calculate_license_cost(seat_price, seats)
    discount_rate = get_seat_discount(seats, education)
    discounted_cost = license_cost * (1 - discount_rate)
    if discounted_cost <= onboarding_fee_limit:
        discounted_cost += onboarding_fee
    return discounted_cost

def needs_contract_review(total: float) -> bool:
    """Return True when license total needs a contract review."""
    return total > contract_review_limit

def gets_trainer(seats: int, total: float) -> bool:
    """Return True when the order gets a dedicated trainer."""
    return seats >= trainer_seat_min or total > trainer_license_limit

def total_licensed(orders: list) -> float:
    """Returns sum of the license totals for every order."""
    total = 0.00
    for order in orders:
        total += calculate_license_total(order["seat_price"], order["seats"], order["education"])
    return total

def largest_license(orders: list) -> str:
    """Returns the company with the largest license total. If two are tied, it will return the first one on the list."""
    largest_company_name = ''
    largest_total = -0.01
    for order in orders:
        order_total = calculate_license_total(order["seat_price"], order["seats"], order["education"])
        if order_total > largest_total:
            largest_total = order_total
            largest_company_name = order["company"]
    return largest_company_name

def format_license_line(company: str, total: float, contract_review: bool, trainer: bool) -> str:
    """Returns one line of the report. Each True/False is shown as yes or no, and the amount always has two decimal places."""
    contract_review_text = 'yes' if contract_review else 'no'
    trainer_review_text = 'yes' if trainer else 'no'
    return (f'{company}: ${total:.2f} | contract review: {contract_review_text} | trainer: {trainer_review_text}')