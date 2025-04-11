from decimal import ROUND_HALF_UP, Decimal, getcontext

getcontext().rounding = ROUND_HALF_UP

ROUNDED = Decimal("1.")

NOT_ROUNDED = Decimal("0.01")

rounding = {
    True: ROUNDED,
    False: NOT_ROUNDED,
}


# AfterValidator for tax_year
def is_valid_tax_year(value: int) -> int:
    if value in [2023, 2024, 2025]:
        return value
    raise ValueError("Invalid tax year. Valid tax years are 2023, 2024, and 2025.")
