from decimal import Decimal

from pydantic import Field

CURRENT_TAX_YEAR = 2024

currency_field = Field(ge=Decimal("0.00"), decimal_places=2)
