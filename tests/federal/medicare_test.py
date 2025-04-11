from decimal import Decimal

import pytest
from pydantic import ValidationError

from python_taxes.federal import medicare


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
class TestForZeroOrNegative:
    def test_required_withholding(self, wages, expected):
        with expected as e:
            assert medicare.required_withholding(wages) == e

    def test_additional_withholding(self, wages, expected):
        with expected as e:
            assert medicare.additional_withholding(wages) == e


# Required Withholding Zero ($0) with Arguments Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (0, 0, False, True, pytest.raises(ValidationError)),
        ("0.01", "0.00", True, False, pytest.raises(ValidationError)),
    ],
)
def test_required_withholding_zero_with_args(
    wages, wages_ytd, self_emp, rounded, expected
):
    with expected as e:
        assert (
            medicare.required_withholding(
                taxable_wages=wages,
                taxable_wages_ytd=wages_ytd,
                self_employed=self_emp,
                rounded=rounded,
            )
            == e
        )


# Additional Withholding Zero ($0) with Arguments Tests
@pytest.mark.parametrize(
    "wages_ytd, self_emp, status, rounded, expected",
    [
        (0, False, "single", False, pytest.raises(ValidationError)),
        ("0.00", True, "married", True, pytest.raises(ValidationError)),
    ],
)
def test_additional_withholding_zero_with_args(
    wages_ytd, self_emp, status, rounded, expected
):
    with expected as e:
        assert (
            medicare.additional_withholding(
                taxable_wages_ytd=wages_ytd,
                filing_status=status,
                self_employed=self_emp,
                rounded=rounded,
            )
            == e
        )


@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        # Not Rounded Tests
        (10000.00, 200000.00, False, False, Decimal("235.00")),
        (8475.55, 200000, False, False, Decimal("199.18")),
        (4615.38, 0, False, False, Decimal("66.92")),
        (3076.92, 0, False, False, Decimal("44.62")),
        (2000.00, 0, False, False, Decimal("29.00")),
        (4615.38, 0, True, False, Decimal("123.61")),
        (3076.92, 0, True, False, Decimal("82.40")),
        (2000.00, 0, True, False, Decimal("53.56")),
        # Rounded Tests
        (10000.00, 200000.00, False, True, Decimal("235.00")),
        (8475.55, 200000, False, True, Decimal("199.00")),
        (4615.38, 0, False, True, Decimal("67.00")),
        (3076.92, 0, False, True, Decimal("45.00")),
        (2000.00, 0, False, True, Decimal("29.00")),
        (4615.38, 0, True, True, Decimal("124.00")),
        (3076.92, 0, True, True, Decimal("82.00")),
        (2000.00, 0, True, True, Decimal("54.00")),
    ],
)
def test_required_withholding(wages, wages_ytd, self_emp, rounded, expected):
    if wages_ytd == 0:
        assert (
            medicare.required_withholding(
                taxable_wages=wages,
                self_employed=self_emp,
                rounded=rounded,
            )
            == expected
        )
    else:
        assert (
            medicare.required_withholding(
                taxable_wages=wages,
                taxable_wages_ytd=wages_ytd,
                self_employed=self_emp,
                rounded=rounded,
            )
            == expected
        )


@pytest.mark.parametrize(
    "wages_ytd, status, self_emp, rounded, expected",
    [
        # Not Rounded Tests
        (200000.00, "single", False, False, Decimal("2900.00")),
        (200000.00, "married", False, False, Decimal("2900.00")),
        (125000.00, "separate", False, False, Decimal("1812.50")),
        (200000.00, "hoh", False, False, Decimal("2900.00")),
        (275500.00, "single", False, False, Decimal("4674.25")),
        (300563.00, "married", False, False, Decimal("4813.23")),
        (255674.00, "separate", False, False, Decimal("4883.34")),
        (255674.00, "hoh", False, False, Decimal("4208.34")),
        (275500.00, "single", True, False, Decimal("7868.12")),
        (300563.00, "married", True, False, Decimal("8297.66")),
        (255674.00, "separate", True, False, Decimal("7847.37")),
        (255674.00, "hoh", True, False, Decimal("7172.37")),
        # Rounded Tests
        (200000.00, "single", False, True, Decimal("2900.00")),
        (200000.00, "married", False, True, Decimal("2900.00")),
        (125000.00, "separate", False, True, Decimal("1813.00")),
        (200000.00, "hoh", False, True, Decimal("2900.00")),
        (275500.00, "single", False, True, Decimal("4674.00")),
        (300563.00, "married", False, True, Decimal("4813.00")),
        (255674.00, "separate", False, True, Decimal("4883.00")),
        (255674.00, "hoh", False, True, Decimal("4208.00")),
        (275500.00, "single", True, True, Decimal("7868.00")),
        (300563.00, "married", True, True, Decimal("8298.00")),
        (255674.00, "separate", True, True, Decimal("7847.00")),
        (255674.00, "hoh", True, True, Decimal("7172.00")),
    ],
)
def test_additional_withholding(wages_ytd, status, self_emp, rounded, expected):
    assert (
        medicare.additional_withholding(wages_ytd, status, self_emp, rounded)
        == expected
    )
