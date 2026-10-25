# business_rules.py
# Author: Daniela Pena

general_discount_seat_min = 10

onboarding_fee = 60.00
contract_review_limit = 5000.00
trainer_seat_limit = 25
trainer_license_limit = 3000.00

def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Return license cost before any discount."""
    return seat_price * seats

def get_seat_discount(seats: int, education: bool = False) -> float:
    """Returns the discount rate as a decimal based on seats and customer type."""
    if education: 
        return 0.16
    elif seats < general_discount_seat_min:
        return 0.00
    else:
        return 0.07

def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
    """Returns the license total for one order."""
    license_cost = calculate_license_cost(seat_price, seats)
    discount_rate = get_seat_discount(seats, education)
    discounted_cost = license_cost * (1 - discount_rate)
    if discounted_cost <= 400.00:
        discounted_cost += onboarding_fee
    return discounted_cost
