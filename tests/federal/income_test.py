from decimal import Decimal

import pytest
from pydantic import ValidationError

from python_taxes.federal import income


@pytest.mark.parametrize(
    "wages, expected",
    [
        # Zero ($0) Tests
        (0, pytest.raises(ValidationError)),
        ("0.00", pytest.raises(ValidationError)),
        (Decimal("0.00"), pytest.raises(ValidationError)),
        # Negative Tests
        (-1.00, pytest.raises(ValidationError)),
        ("-10000", pytest.raises(ValidationError)),
    ],
)
class TestZeroOrNegative:
    def test_employer_withholding(self, wages, expected):
        with expected as e:
            assert income.employer_withholding(wages) == e

    def test_employer_withholding_pre2020(self, wages, expected):
        with expected as e:
            assert income.employer_withholding_pre_2020(wages) == e


# Not Rounded Tests
@pytest.mark.parametrize(
    "wages, rounded, expected",
    [
        # Not Rounded Tests
        (3846.15, False, Decimal("532.35")),
        (3384.62, False, Decimal("430.81")),
        (5769.23, False, Decimal("982.25")),
        (4615.38, False, Decimal("705.33")),
        (2000.00, False, Decimal("163.69")),
        (11538.46, False, Decimal("2702.49")),
        (23076.92, False, Decimal("6740.95")),
        # Rounded Tests
        (3846.15, True, Decimal("532.00")),
        (3384.62, True, Decimal("431.00")),
        (5769.23, True, Decimal("982.00")),
        (4615.38, True, Decimal("705.00")),
        (2000.00, True, Decimal("164.00")),
        (11538.46, True, Decimal("2702.00")),
        (23076.92, True, Decimal("6741.00")),
    ],
)
def test_employer_withholding(wages, rounded, expected):
    assert (
        income.employer_withholding(
            taxable_wages=wages,
            rounded=rounded,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, rounded, expected",
    [
        # Not Rounded Tests
        (3846.15, False, Decimal("605.11")),
        (3384.62, False, Decimal("503.58")),
        (5769.23, False, Decimal("1061.63")),
        (4615.38, False, Decimal("784.71")),
        (2000.00, False, Decimal("203.38")),
        (11538.46, False, Decimal("2818.26")),
        (23076.92, False, Decimal("6856.72")),
        # Rounded Tests
        (3846.15, True, Decimal("605.00")),
        (3384.62, True, Decimal("504.00")),
        (5769.23, True, Decimal("1062.00")),
        (4615.38, True, Decimal("785.00")),
        (2000.00, True, Decimal("203.00")),
        (11538.46, True, Decimal("2818.00")),
        (23076.92, True, Decimal("6857.00")),
    ],
)
def test_employer_withholding_pre2020(wages, rounded, expected):
    assert (
        income.employer_withholding_pre_2020(
            taxable_wages=wages,
            rounded=rounded,
        )
        == expected
    )
