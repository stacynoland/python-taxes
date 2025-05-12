from contextlib import nullcontext
from decimal import Decimal

import pytest
from pydantic import ValidationError

from python_taxes.federal import social_security


@pytest.mark.parametrize(
    "wages, expected",
    [
        # Zero ($0) Tests
        (0, nullcontext(Decimal("0.00"))),
        ("0.00", nullcontext(Decimal("0.00"))),
        (Decimal("0.00"), nullcontext(Decimal("0.00"))),
        # Negative Tests
        (-1.00, pytest.raises(ValidationError)),
        ("-10000", pytest.raises(ValidationError)),
    ],
)
def test_withholding_zero_or_negative(wages, expected):
    with expected as e:
        assert social_security.withholding(wages) == e


# Zero ($0) with YTD Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (0, 100, False, False, nullcontext(Decimal("0.00"))),
        (100, 0, True, True, nullcontext(Decimal("11.00"))),
    ],
)
def test_withholding_zero_with_ytd(wages, wages_ytd, self_emp, rounded, expected):
    with expected as e:
        assert (
            social_security.withholding(
                taxable_wages=wages,
                taxable_wages_ytd=wages_ytd,
                self_employed=self_emp,
                rounded=rounded,
            )
            == e
        )


@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, year, rounded, expected",
    [
        # Not Rounded Tests
        (4615.38, 100, False, None, False, Decimal("286.15")),
        (3076.92, 100, False, None, False, Decimal("190.77")),
        (2000.00, 100, False, None, False, Decimal("124.00")),
        (10000.00, 100, False, None, False, Decimal("620.00")),
        (8475.55, 100, False, None, False, Decimal("525.48")),
        (2000.83, 170000.30, False, None, False, Decimal("0.00")),
        (2000, 168000, False, None, False, Decimal("37.20")),
        (2000, 168000, True, None, False, Decimal("229.03")),
        (170000, 0, True, None, False, Decimal("19467.38")),
        # Rounded Tests
        (4615.38, 100, False, None, True, Decimal("286.00")),
        (3076.92, 100, False, None, True, Decimal("191.00")),
        (2000.00, 100, False, None, True, Decimal("124.00")),
        (10000.00, 100, False, None, True, Decimal("620.00")),
        (8475.55, 100, False, None, True, Decimal("525.00")),
        (2000.83, 170000.30, False, None, True, Decimal("0.00")),
        (2000, 168000, False, None, True, Decimal("37.00")),
        (2000, 168000, True, None, True, Decimal("229.00")),
        (170000, 0, True, None, True, Decimal("19467.00")),
        # Tax Year Tests
        (2000, 168000, False, 1234, False, pytest.raises(ValidationError)),
        (2000, 168000, False, "1234", False, pytest.raises(ValidationError)),
        (2000, 168000, False, "notnum", False, pytest.raises(ValidationError)),
        (2000, 168000, True, 2024, False, nullcontext(Decimal("229.03"))),
        (2000, 168000, True, "2024", False, nullcontext(Decimal("229.03"))),
    ],
)
def test_withholding_2024(wages, wages_ytd, self_emp, year, rounded, expected):
    if not year:
        if wages_ytd == 0:
            assert (
                social_security.withholding(
                    taxable_wages=wages,
                    self_employed=self_emp,
                    tax_year=2024,
                    rounded=rounded,
                )
                == expected
            )
        else:
            assert (
                social_security.withholding(
                    taxable_wages=wages,
                    taxable_wages_ytd=wages_ytd,
                    self_employed=self_emp,
                    tax_year=2024,
                    rounded=rounded,
                )
                == expected
            )
    else:
        with expected as e:
            assert (
                social_security.withholding(
                    taxable_wages=wages,
                    taxable_wages_ytd=wages_ytd,
                    self_employed=self_emp,
                    tax_year=year,
                    rounded=rounded,
                )
                == e
            )
