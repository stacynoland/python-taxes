from decimal import Decimal

from pydantic import ValidationError
import pytest

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
        assert (social_security.withholding(wages) == e)


@pytest.mark.parametrize(
    "wages, self_emp, rounded, expected",
    [
        (0, False, False, pytest.raises(ValidationError)),
        ("0.00", True, True, pytest.raises(ValidationError)),
    ],
)
def test_withholding_zero_all_params(
    wages, self_emp, rounded, expected):
        with expected as e:
            assert (social_security.withholding(wages, self_emp, rounded) == e)


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
        assert (social_security.withholding(wages) == e)


# Not Rounded Tests
@pytest.mark.parametrize(
    "wages, self_emp, rounded, expected",
    [
        (4615.38, False, False, Decimal("286.15")),
        (Decimal("3076.92"), False, False, Decimal("190.77")),
        (2000.00, False, False, Decimal("124.00")),
        (10000.00, False, False, Decimal("620.00")),
        (8475.55, False, False, Decimal("525.48")),
    ],
)
def test_withholding_not_rounded(wages, self_emp, rounded, expected):
        assert (
            social_security.withholding(wages, self_emp, rounded) == expected
        )


# Rounded Tests
@pytest.mark.parametrize(
    "wages, self_emp, rounded, expected",
    [
        (4615.38, False, True, Decimal("286.00")),
        (Decimal("3076.92"), False, True, Decimal("191.00")),
        (2000.00, False, True, Decimal("124.00")),
        (10000.00, False, True, Decimal("620.00")),
        (8475.55, False, True, Decimal("525.00")),
    ],
)
def test_required_withholding_rounded(wages, self_emp, rounded, expected):
        assert (
            social_security.withholding(wages, self_emp, rounded) == expected
        )
