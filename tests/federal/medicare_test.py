from contextlib import nullcontext
from decimal import Decimal

from pydantic import ValidationError
import pytest

from python_taxes.federal.calculators import medicare


@pytest.mark.parametrize(
    "medicare_wages, expected", [
        (0, pytest.raises(ValidationError)),
        ('0.00', pytest.raises(ValidationError)),
        (Decimal('0.00'), pytest.raises(ValidationError)),
        (4615.38, nullcontext(Decimal('66.92'))),
        (Decimal('3076.92'), nullcontext(Decimal('44.62'))),
        ('2000', nullcontext(Decimal('29.00'))),
    ]
)


def test_tax_withholding(medicare_wages, expected):
    with expected as result:
        assert medicare.tax_withholding(medicare_wages) == result