from decimal import Decimal, ROUND_HALF_UP
from typing import Annotated, Literal, Optional

from pydantic import StrictBool, Field, validate_call


PERCENT = Decimal('1.45') / 100

SELF_EMP_PERCENT = Decimal('2.9') / 100

ADDITIONAL_PERCENT = Decimal('0.9') / 100

DEFAULT_THRESHOLD = 200000


@validate_call
def tax_withholding(
    medicare_wages: Annotated[Decimal, Field(ge=Decimal('0.01'), decimal_places=2)],
    medicare_wages_ytd: Optional[
        Annotated[Decimal, Field(ge=Decimal('0.01'), decimal_places=2)]] = None,
    self_employed: StrictBool = False,
) -> Decimal:

    if medicare_wages_ytd and medicare_wages_ytd > DEFAULT_THRESHOLD:
        if self_employed:
            tax_rate = SELF_EMP_PERCENT + ADDITIONAL_PERCENT
        else:
            tax_rate = PERCENT + ADDITIONAL_PERCENT
    else:
        if self_employed:
            tax_rate = SELF_EMP_PERCENT
        else:
            tax_rate = PERCENT

    return (medicare_wages * tax_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


@validate_call
def additional_tax(
    medicare_wages: Annotated[Decimal, Field(ge=Decimal('0.01'), decimal_places=2)],
    medicare_wages_ytd: Annotated[Decimal, Field(ge=Decimal('0.01'), decimal_places=2)],
    self_employed: StrictBool = False,
    status: Optional[Literal['single', 'married', 'separate' 'hoh']] = 'single',
) -> Decimal:

    if medicare_wages_ytd:
        if status == 'married':
            threshold = 250000
        elif status == 'separate':
            threshold = 125000
        else:
            threshold = DEFAULT_THRESHOLD
    else:
        threshold = DEFAULT_THRESHOLD
        medicare_wages_ytd = 0

    if self_employed:
        tax_rate = SELF_EMP_PERCENT
    else:
        tax_rate = PERCENT

    if (medicare_wages_ytd + medicare_wages) > threshold:
        over = (medicare_wages_ytd + medicare_wages) - threshold
        if (medicare_wages - over) > 0:
            tax_amount = (medicare_wages - over) * tax_rate
            tax_rate = tax_rate + ADDITIONAL_PERCENT
            tax_amount = tax_amount + (over * tax_rate)
        else:
            tax_rate = tax_rate + ADDITIONAL_PERCENT
            tax_amount = medicare_wages * tax_rate
    else:
        tax_amount = medicare_wages * tax_rate

    return tax_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
