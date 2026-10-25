# ISM 3232 Midterm: Cloudstep Software

- **Name:** Daniela Pena
- **Version:** Python 3.14.7
- **Date:** 10.25.2026

## What This Program Does

# This program helps to calculate the license cost totals for Cloudstep Software's app. It applies specific discounts and onboarding fees when applicable depending on if it meets certain business rules. Similarly, it helps determine which customers qualify for a trainer (assigned to them), if contract reviews are needed (past a certain threshold), and grants the user a report with a summary of the results.

## Business Rules

# There are six business rules for Cloudstep Software: 
1. The license cost is calculated by multiplying the price per seat and the number of seats.
2. There are discounts available to customers depending on the following criteria: fewer than 10 seats (no discount applicable), 10 through 49 seats (7% discount applicable), and 50 seats or more (16% applicable depending on customer type).
3. Only education customers are able to get a 16% discount (with 50+ seats), otherwise, any other order with 50+ seats gets the same 7% discount as customers with 10+ seats.
4. Customers who have a discounted cost of $400 or less will receive an onboarding fee od $60.
5. Customers with license totals of over $5,000 will need their contract reviewed.
6. Any customer order with more than 25 seats or over $3,000 in their license total will be assigned a dedicated trainer.

## How to Run
```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test
```
ruff format .
ruff check .
pytest -v
```
# There are a total of 23 tests written.

## Files in this Repository

- `business_rules.py`: the eight functions and any constants
- `main.py`: the sample orders and the report/summary
- `tests/test_business_rules.py`: the pytest tests
- `tests/__init__.py`: an empty file that lets the tests import the functions needed
- `commands.md`: the terminal commands that built and checked the project, with their output(s)
- `README.md`: this file containing the program information/project overview
- `requirements.txt`: the packages to install
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository

## AI Use Statement

# I (Daniela Pena) did not use AI on this exam!!!! 
