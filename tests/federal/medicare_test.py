from decimal import Decimal

from pydantic import ValidationError
import pytest

from python_taxes.federal.calculators import medicare


# Zero ($0) Tests
@pytest.mark.parametrize(
    "wages, expected",
    [
        (0, pytest.raises(ValidationError)),
        ("0.00", pytest.raises(ValidationError)),
        (Decimal("0.00"), pytest.raises(ValidationError)),
    ],
)
class TestForZero:
    def test_required_withholding_zero(self, wages, expected):
        with expected as e:
            assert (medicare.withholding(wages) == e)

    def test_additional_withholding_zero(self, wages, expected):
        with expected as e:
            assert (medicare.additional_withholding(wages) == e)


@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (0, 0, False, True, pytest.raises(ValidationError)),
        ("0.01", "0.00", True, False, pytest.raises(ValidationError)),
    ],
)
def test_required_withholding_zero_all_params(
    wages, wages_ytd, self_emp, rounded, expected):
        with expected as e:
            assert (
                medicare.withholding(wages, wages_ytd, self_emp, rounded) == e
            )


@pytest.mark.parametrize(
    "wages_ytd, self_emp, status, rounded, expected",
    [
        (0, False, "single", False, pytest.raises(ValidationError)),
        ("0.00", True, "married", True, pytest.raises(ValidationError)),
    ],
)
def test_additional_withholding_zero_all_params(
    wages_ytd, self_emp, status, rounded, expected):
        with expected as e:
            assert (
                medicare.additional_withholding(wages_ytd, self_emp, status, rounded) == e
            )


# Negative Tests
@pytest.mark.parametrize(
    "wages, expected",
    [
        (-1.00, pytest.raises(ValidationError)),
        ("-10000", pytest.raises(ValidationError)),
    ],
)
class TestForNegatives:
    def test_required_withholding_negative(self, wages, expected):
        with expected as e:
            assert (medicare.withholding(wages) == e)

    def test_additional_withholding_negative(self, wages, expected):
        with expected as e:
            assert (medicare.additional_withholding(wages) == e)


# Not Rounded Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (4615.38, None, False, False, Decimal("66.92")),
        (Decimal("3076.92"), None, False, False, Decimal("44.62")),
        (2000.00, None, False, False, Decimal("29.00")),
        (10000.00, 200000.00, False, False, Decimal("235.00")),
        (8475.55, 200000, False, False, Decimal("199.18")),
    ],
)
def test_required_withholding_not_rounded(
    wages, wages_ytd, self_emp, rounded, expected):
        assert (
            medicare.withholding(wages, wages_ytd, self_emp, rounded) == expected
        )

# Rounded Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (4615.38, None, False, True, Decimal("67.00")),
        (Decimal("3076.92"), None, False, True, Decimal("45.00")),
        (2000.00, None, False, True, Decimal("29.00")),
        (10000.00, 200000.00, False, True, Decimal("235.00")),
        (8475.55, 200000, False, True, Decimal("199.00")),
    ],
)
def test_required_withholding_rounded(
    wages, wages_ytd, self_emp, rounded, expected):
        assert (
            medicare.withholding(wages, wages_ytd, self_emp, rounded) == expected
        )
