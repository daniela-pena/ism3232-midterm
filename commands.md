# Terminal Record: Cloudstep Software



## 1. Building the project
Commands:
```
cd ~/ism3232
mkdir ism3232-midterm
cd ~/ism3232/ism3232-midterm
python3 -m venv .venv && source .venv/bin/activate
touch business_rules.py main.py commands.md README.md requirements.txt
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
pip install pytest ruff && pip list && pip freeze > requirements.txt
echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
git init
git status
git add .


## 2. The virtual environment
Command:
```
which python3
```

Output:
```
/Users/danielapena/ism3232/ism3232-midterm/.venv/bin/python3
```

# After running 'which python3', the output shows that the virtual environmentis active at the end of the directory because Python is running from the .venv folder (.venv/bin/python3).

## 3. The project structure
Command:
```
tree -L 2
```

Output:
```.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```

# My pycache folder is visible on my computer but not on my Git repository because of the .gitignore command I ran during setup for Git to ignore the .venv and pycache folders.

## 4. Every function and test
Command:
```
rg 'def '
```

Output:
```
tests/test_business_rules.py
4:def test_license_cost_price_by_seats():
7:def test_requires_contract_review_over():
10:def test_requires_contract_review_under():
13:def test_contract_review_boundary_at_limit():
17:def test_discount_at_ten_seats():
21:def test_discount_seat_boundary_under_ten():
24:def test_discount_at_forty_nine_seats():
27:def test_education_discount_at_fifty_seats():
30:def test_non_education_discount_at_fifty_seats():
33:def test_license_total_applies_seat_discount_rate():
36:def test_license_total_applies_education_discount_rate():
39:def test_onboarding_fee_at_limit():
43:def test_onboarding_fee_applied_to_license_limit_total_below_limit():
46:def test_onboarding_fee_not_applied_to_license_limit_total_above_limit():
49:def test_trainer_at_license_total_limit():
53:def test_trainer_assigned_above_license_total_limit():
56:def test_trainer_assigned_at_seat_limit():
59:def test_trainer_not_assigned_below_seat_limit():
62:def test_largest_license_returns_highest_total_company():
69:def test_largest_license_returns_first_company_when_tied():
76:def test_largest_license_of_empty_list_is_zero():
79:def test_format_license_line_no_trainer_or_review():
82:def test_format_license_line_with_trainer_and_review():

business_rules.py
12:def calculate_license_cost(seat_price: float, seats: int) -> float:
16:def get_seat_discount(seats: int, education: bool = False) -> float:
27:def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
36:def needs_contract_review(total: float) -> bool:
40:def gets_trainer(seats: int, total: float) -> bool:
44:def total_licensed(orders: list) -> float:
51:def largest_license(orders: list) -> str:
62:def format_license_line(company: str, total: float, contract_review: bool, trainer: bool) -> str:
```

# business_rules.py defines 8 functions and tests/test_business_rules.py defines 23 tests.

## 5. Which files print
Command:
```
rg -l 'print'
```

Output:
```
main.py
```

# main.py printed and not business_rules.py because business_rules.py holds the logic and keeps/returns values rather than printing them (unlike main.py where it does print the reports).

## 6. The commit history
Command:
```
git log --oneline
```
Output:
```
01b295f (HEAD -> main, origin/main) 9th commit: wrote pytests and tested they all passed
7d05f92 8th commit: main.py print
8b80840 7th commit: 8/8 functions
fcb56e0 6th commit: 5/8 functions
0ca098d 5th commit: 2/8 functions' git status ''
0c5afb1 4th commit: added tests folder
301e8fc 3rd commit: commands & readme
a187001 2nd commit: rules & main
afe08f7 initial commit: week 9 midterm
```

# As of right now, there are 9 commits (and more to come for after committing this file).
