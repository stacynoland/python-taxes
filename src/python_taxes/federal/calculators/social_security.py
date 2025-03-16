from decimal import Decimal
from typing import Annotated, Literal, Optional

from pydantic import Field, StrictBool, validate_call

from . import rounding

STANDARD_TAX = Decimal('6.200') / 100

SELF_EMPLOYED_TAX = Decimal('12.400') / 100


@validate_call
def withholding(
    taxable_wages: Annotated[Decimal, Field(ge=0.01, decimal_places=2)],
    self_employed: StrictBool = False,
    rounded: StrictBool = False,
) -> Decimal:
    """Social security tax withholding.

    Parameters:
    taxable_wages -- Total wages to be taxed
    self_employed -- Person/employee is self-employed (default False)
    round -- Round response to nearest whole dollar amount (default False)
    """

    if self_employed:
        tax_rate = SELF_EMPLOYED_TAX
    else:
        tax_rate = STANDARD_TAX

    return (taxable_wages * tax_rate).quantize(rounding[rounded])
