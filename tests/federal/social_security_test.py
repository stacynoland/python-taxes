from decimal import Decimal

import pytest
from pydantic import ValidationError

from python_taxes.federal import social_security


# Zero ($0) Tests
@pytest.mark.parametrize(
    "wages, expected",
    [
        (0, pytest.raises(ValidationError)),
        ("0.00", pytest.raises(ValidationError)),
        (Decimal("0.00"), pytest.raises(ValidationError)),
    ],
)
def test_withholding_zero(wages, expected):
    with expected as e:
        assert social_security.withholding(wages) == e


@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (0, 100, False, False, pytest.raises(ValidationError)),
        (100, 0, True, True, pytest.raises(ValidationError)),
    ],
)
def test_withholding_zero_all_params(wages, wages_ytd, self_emp, rounded, expected):
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


# Negative Tests
@pytest.mark.parametrize(
    "wages, expected",
    [
        (-1.00, pytest.raises(ValidationError)),
        ("-10000", pytest.raises(ValidationError)),
    ],
)
def test_withholding_negative(wages, expected):
    with expected as e:
        assert social_security.withholding(wages) == e


# Not Rounded Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (4615.38, 100, False, False, Decimal("286.15")),
        (Decimal("3076.92"), 100, False, False, Decimal("190.77")),
        (2000.00, 100, False, False, Decimal("124.00")),
        (10000.00, 100, False, False, Decimal("620.00")),
        (8475.55, 100, False, False, Decimal("525.48")),
    ],
)
def test_withholding_not_rounded(wages, wages_ytd, self_emp, rounded, expected):
    assert (
        social_security.withholding(
            taxable_wages=wages,
            taxable_wages_ytd=wages_ytd,
            self_employed=self_emp,
            rounded=rounded,
        )
        == expected
    )


# Rounded Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (4615.38, 100, False, True, Decimal("286.00")),
        (Decimal("3076.92"), 100, False, True, Decimal("191.00")),
        (2000.00, 100, False, True, Decimal("124.00")),
        (10000.00, 100, False, True, Decimal("620.00")),
        (8475.55, 100, False, True, Decimal("525.00")),
    ],
)
def test_required_withholding_rounded(wages, wages_ytd, self_emp, rounded, expected):
    assert (
        social_security.withholding(
            taxable_wages=wages,
            taxable_wages_ytd=wages_ytd,
            self_employed=self_emp,
            rounded=rounded,
        )
        == expected
    )
