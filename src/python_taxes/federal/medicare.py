from decimal import Decimal
from typing import Annotated, Literal

from pydantic import StrictBool, validate_call

from python_taxes import currency_field
from python_taxes.federal import rounding

STANDARD_PERCENT = Decimal("1.45") / 100

SELF_EMPLOYED_PERCENT = Decimal("2.9") / 100

ADDITIONAL_PERCENT = Decimal("0.9") / 100

DEFAULT_THRESHOLD = Decimal("200000")

status_threshold = {
    "single": DEFAULT_THRESHOLD,
    "married": Decimal("250000"),
    "separate": Decimal("125000"),
    "hoh": DEFAULT_THRESHOLD,
}


@validate_call
def required_withholding(
    taxable_wages: Annotated[Decimal, currency_field],
    taxable_wages_ytd: Annotated[Decimal, currency_field] = Decimal("0.00"),
    self_employed: StrictBool = False,
    rounded: StrictBool = False,
) -> Decimal:
    """Calculate required amount to withhold regardless of filing status.

    Parameters:
    taxable_wages -- Wages earned this period
    taxable_wages_ytd -- Wages earned this year
    self_employed -- True if self-employed (default False)
    rounded -- Round to nearest whole dollar amount (default False)
    """

    if self_employed:
        tax_rate = SELF_EMPLOYED_PERCENT
        taxable_wages = taxable_wages * (Decimal("92.35") / 100)
        taxable_wages_ytd = taxable_wages_ytd * (Decimal("92.35") / 100)
    else:
        tax_rate = STANDARD_PERCENT

    if (
        taxable_wages > DEFAULT_THRESHOLD
        or (taxable_wages_ytd + taxable_wages) > DEFAULT_THRESHOLD
    ):
        tax_rate = tax_rate + ADDITIONAL_PERCENT

    return (taxable_wages * tax_rate).quantize(rounding[rounded])


@validate_call
def additional_withholding(
    taxable_wages_ytd: Annotated[Decimal, currency_field],
    filing_status: Annotated[
        str, Literal["single", "married", "separate", "hoh"]
    ] = "single",
    self_employed: StrictBool = False,
    rounded: StrictBool = False,
) -> Decimal:
    """Calculate withholding based on status.

    Parameters:
    taxable_wages_ytd -- Wages earned this year
    filing_status -- Filing status (default 'single')
    self_employed -- True if self-employed (default False)
    rounded -- Round to nearest whole dollar amount (default False)
    """

    if self_employed:
        tax_rate = SELF_EMPLOYED_PERCENT
        taxable_wages_ytd = taxable_wages_ytd * (Decimal("92.35") / 100)
    else:
        tax_rate = STANDARD_PERCENT

    threshold = status_threshold[filing_status]

    if taxable_wages_ytd > threshold:
        wages_over_threshold = taxable_wages_ytd - threshold
        med_taxes = (taxable_wages_ytd - wages_over_threshold) * tax_rate
        tax_rate = tax_rate + ADDITIONAL_PERCENT
        med_taxes = med_taxes + (wages_over_threshold * tax_rate)
    else:
        med_taxes = taxable_wages_ytd * tax_rate

    return med_taxes.quantize(rounding[rounded])
