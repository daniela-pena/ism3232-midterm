from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
)


def test_license_cost_price_by_seats():
    assert round(calculate_license_cost(100.00, 2), 2) == 200.00


def test_requires_contract_review_over():
    assert needs_contract_review(5001) is True


def test_requires_contract_review_under():
    assert needs_contract_review(4999) is False


def test_contract_review_boundary_at_limit():
    # Exactly at 5000 should NOT require review (> not >=)
    assert needs_contract_review(5000) is False


def test_discount_at_ten_seats():
    # Exactly 10 seats qualifies for the 7% discount rate
    assert get_seat_discount(10) == 0.07


def test_discount_seat_boundary_under_ten():
    assert get_seat_discount(9) == 0.00


def test_discount_at_forty_nine_seats():
    assert get_seat_discount(49) == 0.07


def test_education_discount_at_fifty_seats():
    assert get_seat_discount(50, True) == 0.16


def test_non_education_discount_at_fifty_seats():
    assert get_seat_discount(50, False) == 0.07


def test_license_total_applies_seat_discount_rate():
    assert round(calculate_license_total(100.00, 10), 2) == 930.00


def test_license_total_applies_education_discount_rate():
    assert round(calculate_license_total(10.00, 50, True), 2) == 420.00


def test_onboarding_fee_at_limit():
    # Exactly $400 still qualifies for a $60 onboarding fee
    assert round(calculate_license_total(400.00, 1), 2) == 460.00


def test_onboarding_fee_applied_to_license_limit_total_below_limit():
    assert round(calculate_license_total(399.00, 1), 2) == 459.00


def test_onboarding_fee_not_applied_to_license_limit_total_above_limit():
    assert round(calculate_license_total(401.00, 1), 2) == 401.00


def test_trainer_at_license_total_limit():
    # Exactly $3000 license total does not qualify
    assert gets_trainer(24, 3000.00) is False


def test_trainer_assigned_above_license_total_limit():
    assert gets_trainer(24, 3001.00) is True


def test_trainer_assigned_at_seat_limit():
    assert gets_trainer(25, 100.00) is True


def test_trainer_not_assigned_below_seat_limit():
    assert gets_trainer(24, 100.00) is False


def test_largest_license_returns_highest_total_company():
    orders = [
        {"company": "Pine Books", "seat_price": 100.00, "seats": 1, "education": False},
        {
            "company": "Summit College",
            "seat_price": 600.00,
            "seats": 1,
            "education": False,
        },
    ]
    assert largest_license(orders) == "Summit College"


def test_largest_license_returns_first_company_when_tied():
    orders = [
        {"company": "Pine Books", "seat_price": 500.00, "seats": 1, "education": False},
        {
            "company": "Quarry School",
            "seat_price": 500.00,
            "seats": 1,
            "education": False,
        },
    ]
    assert largest_license(orders) == "Pine Books"


def test_largest_license_of_empty_list_is_zero():
    assert largest_license([]) == ""


def test_format_license_line_no_trainer_or_review():
    assert (
        format_license_line("Pine Books", 260.00, False, False)
        == "Pine Books: $260.00 | contract review: no | trainer: no"
    )


def test_format_license_line_with_trainer_and_review():
    assert (
        format_license_line("Summit College", 6300.00, True, True)
        == "Summit College: $6300.00 | contract review: yes | trainer: yes"
    )
