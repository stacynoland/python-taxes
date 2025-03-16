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
    medicare_wages: Annotated[Decimal, Field(ge=Decimal("0.01"), decimal_places=2)],
    medicare_wages_ytd: Optional[
        Annotated[Decimal, Field(ge=Decimal("0.01"), decimal_places=2)]] = None,
    self_employed: StrictBool = False,
    round: StrictBool = False,
) -> Decimal:
    """Required amount to withhold regardless of filing status

    Parameters:
    medicare_wages -- Earned this period
    medicare_wages_ytd -- Earned this year
    self_employed -- Person/employee is self-employed (default False)
    round -- Round response to nearest whole dollar amount (default False)
    """

    if not medicare_wages_ytd:
        medicare_wages_ytd = 0

    if self_employed:
        tax_rate = SELF_EMPLOYED_PERCENT
    else:
        tax_rate = STANDARD_PERCENT

    if (medicare_wages > DEFAULT_THRESHOLD
            or (medicare_wages_ytd + medicare_wages) > DEFAULT_THRESHOLD):
        tax_rate = tax_rate + ADDITIONAL_PERCENT

    return (medicare_wages * tax_rate).quantize(rounding[round])


@validate_call
def additional_withholding(
    medicare_wages_ytd: Annotated[Decimal, Field(ge=Decimal("0.01"), decimal_places=2)],
    self_employed: StrictBool = False,
    status: Optional[Literal['single', 'married', 'separate' 'hoh']] = 'single',
    round: StrictBool = False,
) -> Decimal:
    """Additional withholding based on status

    Parameters:
    medicare_wages_ytd -- Earned this year
    self_employed -- Person/employee is self-employed (default False)
    status -- Filing status of person (default 'single')
    round -- Round response to nearest whole dollar amount (default False)
    """

    if self_employed:
        tax_rate = SELF_EMPLOYED_PERCENT
    else:
        tax_rate = STANDARD_PERCENT

    threshold = status_threshold[status]

    if medicare_wages_ytd > threshold:
        wages_over_threshold = medicare_wages_ytd - threshold
        med_taxes = (medicare_wages_ytd - wages_over_threshold) * tax_rate
        tax_rate = tax_rate + ADDITIONAL_PERCENT
        med_taxes = med_taxes + (wages_over_threshold * tax_rate)
    else:
        med_taxes = medicare_wages_ytd * tax_rate

    return med_taxes.quantize(rounding[round])
