from decimal import Decimal
from typing import NamedTuple

from pydantic import Field, PositiveInt

MAX = Decimal("999999999999.99")


class RateRow(NamedTuple):
    """Tax withholding rate schedule."""

    min: Decimal = Field(ge=Decimal("0.00"), le=MAX, decimal_places=2)
    max: Decimal = Field(ge=Decimal("0.00"), le=MAX, decimal_places=2)
    withhold_amount: Decimal = Field(ge=Decimal("0.00"), le=MAX, decimal_places=2)
    percent: PositiveInt = Field(le=100)
