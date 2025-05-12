from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator, StrictBool, validate_call

from python_taxes import CURRENT_TAX_YEAR, currency_field
from python_taxes.federal import is_valid_tax_year, rounding

STANDARD_TAX = Decimal("6.200") / 100

SELF_EMPLOYED_TAX = Decimal("12.400") / 100

wage_limit = {
    2023: Decimal("160200"),
    2024: Decimal("168600"),
    2025: Decimal("176100"),
}


@validate_call
def withholding(
    taxable_wages: Annotated[Decimal, currency_field],
    taxable_wages_ytd: Annotated[Decimal, currency_field] = Decimal("0.00"),
    self_employed: StrictBool = False,
    tax_year: Annotated[int, AfterValidator(is_valid_tax_year)] = CURRENT_TAX_YEAR,
    rounded: StrictBool = False,
) -> Decimal:
    """
    Social security tax withholding.

    Parameters:
    taxable_wages -- Wages earned this period
    taxable_wages_ytd -- Wages earned this year
    self_employed -- True if self-employed (default False)
    tax_year -- Year for which you are filing (default CURRENT_TAX_YEAR)
    rounded -- Round to nearest whole dollar amount (default False)
    """

    if self_employed:
        tax_rate = SELF_EMPLOYED_TAX
        taxable_wages = taxable_wages * (Decimal("92.35") / 100)
        taxable_wages_ytd = taxable_wages_ytd * (Decimal("92.35") / 100)
    else:
        tax_rate = STANDARD_TAX

    limit = wage_limit[tax_year]

    if taxable_wages_ytd > limit:
        return Decimal("0.00")  # Tax is 0 because limit is reached

    if (taxable_wages + taxable_wages_ytd) > limit:
        over = (taxable_wages + taxable_wages_ytd) - limit
        taxable_wages = taxable_wages - over

    return (taxable_wages * tax_rate).quantize(rounding[rounded])
