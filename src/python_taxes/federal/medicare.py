from decimal import Decimal
from typing import Annotated, Literal, Optional

from pydantic import Field, StrictBool, validate_call

from . import rounding


STANDARD_PERCENT = Decimal("1.45") / 100

SELF_EMPLOYED_PERCENT = Decimal("2.9") / 100

ADDITIONAL_PERCENT = Decimal("0.9") / 100

DEFAULT_THRESHOLD = Decimal("200000")

status_threshold = {
    'single': DEFAULT_THRESHOLD,
    'married': Decimal("250000"),
    'separate': Decimal("125000"),
    'hoh': DEFAULT_THRESHOLD,
}


@validate_call
def required_withholding(
    taxable_wages: Annotated[Decimal, Field(ge=Decimal("0.01"), decimal_places=2)],
    taxable_wages_ytd: Optional[Annotated[
        Decimal, Field(ge=Decimal("0.01"), decimal_places=2)]] = Decimal("0.00"),
    self_employed: Optional[StrictBool] = False,
    rounded: Optional[StrictBool] = False,
) -> Decimal:
    """
    Required amount to withhold regardless of filing status

    Parameters:
    taxable_wages -- Wages earned this period
    taxable_wages_ytd -- Wages earned this year
    self_employed -- True if self-employed (default False)
    round -- Round to nearest whole dollar amount (default False)
    """

    if not taxable_wages_ytd:
        taxable_wages_ytd = 0

    if self_employed:
        tax_rate = SELF_EMPLOYED_PERCENT
    else:
        tax_rate = STANDARD_PERCENT

    if (taxable_wages > DEFAULT_THRESHOLD
            or (taxable_wages_ytd + taxable_wages) > DEFAULT_THRESHOLD):
        tax_rate = tax_rate + ADDITIONAL_PERCENT

    return (taxable_wages * tax_rate).quantize(rounding[rounded])


@validate_call
def additional_withholding(
    taxable_wages_ytd: Annotated[Decimal, Field(ge=Decimal("0.01"), decimal_places=2)],
    status: Optional[Literal['single', 'married', 'separate', 'hoh']] = 'single',
    self_employed: Optional[StrictBool] = False,
    rounded: Optional[StrictBool] = False,
) -> Decimal:
    """
    Additional withholding based on status

    Parameters:
    taxable_wages_ytd -- Wages earned this year
    status -- Filing status (default 'single')
    self_employed -- True if self-employed (default False)
    round -- Round to nearest whole dollar amount (default False)
    """

    if self_employed:
        tax_rate = SELF_EMPLOYED_PERCENT
    else:
        tax_rate = STANDARD_PERCENT

    threshold = status_threshold[status]

    if taxable_wages_ytd > threshold:
        wages_over_threshold = taxable_wages_ytd - threshold
        med_taxes = (taxable_wages_ytd - wages_over_threshold) * tax_rate
        tax_rate = tax_rate + ADDITIONAL_PERCENT
        med_taxes = med_taxes + (wages_over_threshold * tax_rate)
    else:
        med_taxes = taxable_wages_ytd * tax_rate

    return med_taxes.quantize(rounding[rounded])
