from decimal import Decimal

import pytest
from pydantic import ValidationError

from python_taxes.federal import medicare


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
            assert medicare.required_withholding(wages) == e

    def test_additional_withholding_zero(self, wages, expected):
        with expected as e:
            assert medicare.additional_withholding(wages) == e


@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (0, 0, False, True, pytest.raises(ValidationError)),
        ("0.01", "0.00", True, False, pytest.raises(ValidationError)),
    ],
)
def test_required_withholding_zero_all_params(
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


@pytest.mark.parametrize(
    "wages_ytd, self_emp, status, rounded, expected",
    [
        (0, False, "single", False, pytest.raises(ValidationError)),
        ("0.00", True, "married", True, pytest.raises(ValidationError)),
    ],
)
def test_additional_withholding_zero_all_params(
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
            assert medicare.required_withholding(wages) == e

    def test_additional_withholding_negative(self, wages, expected):
        with expected as e:
            assert medicare.additional_withholding(wages) == e


# Not Rounded Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (10000.00, 200000.00, False, False, Decimal("235.00")),
        (8475.55, 200000, False, False, Decimal("199.18")),
    ],
)
def test_required_withholding_not_rounded_with_ytd(
    wages, wages_ytd, self_emp, rounded, expected
):
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
    "wages, self_emp, rounded, expected",
    [
        (4615.38, False, False, Decimal("66.92")),
        (Decimal("3076.92"), False, False, Decimal("44.62")),
        (2000.00, False, False, Decimal("29.00")),
    ],
)
def test_required_withholding_not_rounded_no_ytd(wages, self_emp, rounded, expected):
    assert (
        medicare.required_withholding(
            taxable_wages=wages,
            self_employed=self_emp,
            rounded=rounded,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages_ytd, status, self_emp, rounded, expected",
    [
        (200000.00, "single", False, False, Decimal("2900.00")),
        (200000.00, "married", False, False, Decimal("2900.00")),
        (125000.00, "separate", False, False, Decimal("1812.50")),
        (200000.00, "hoh", False, False, Decimal("2900.00")),
        (275500.00, "single", False, False, Decimal("4674.25")),
        (300563.00, "married", False, False, Decimal("4813.23")),
        (255674.00, "separate", False, False, Decimal("4883.34")),
        (255674.00, "hoh", False, False, Decimal("4208.34")),
        (275500.00, "single", True, False, Decimal("8669.00")),
        (300563.00, "married", True, False, Decimal("9171.39")),
        (255674.00, "separate", True, False, Decimal("8590.61")),
        (255674.00, "hoh", True, False, Decimal("7915.61")),
    ],
)
def test_additional_withholding_not_rounded(
    wages_ytd, status, self_emp, rounded, expected
):
    assert (
        medicare.additional_withholding(wages_ytd, status, self_emp, rounded)
        == expected
    )


# Rounded Tests
@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, rounded, expected",
    [
        (10000.00, 200000.00, False, True, Decimal("235.00")),
        (8475.55, 200000, False, True, Decimal("199.00")),
    ],
)
def test_required_withholding_rounded_with_ytd(
    wages, wages_ytd, self_emp, rounded, expected
):
    assert (
        medicare.required_withholding(wages, wages_ytd, self_emp, rounded) == expected
    )


@pytest.mark.parametrize(
    "wages, self_emp, rounded, expected",
    [
        (4615.38, False, False, Decimal("66.92")),
        (Decimal("3076.92"), False, False, Decimal("44.62")),
        (2000.00, False, False, Decimal("29.00")),
    ],
)
def test_required_withholding_rounded_no_ytd(wages, self_emp, rounded, expected):
    assert (
        medicare.required_withholding(
            taxable_wages=wages, self_employed=self_emp, rounded=rounded
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages_ytd, status, self_emp, rounded, expected",
    [
        (200000.00, "single", False, True, Decimal("2900.00")),
        (200000.00, "married", False, True, Decimal("2900.00")),
        (125000.00, "separate", False, True, Decimal("1813.00")),
        (200000.00, "hoh", False, True, Decimal("2900.00")),
        (275500.00, "single", False, True, Decimal("4674.00")),
        (300563.00, "married", False, True, Decimal("4813.00")),
        (255674.00, "separate", False, True, Decimal("4883.00")),
        (255674.00, "hoh", False, True, Decimal("4208.00")),
        (275500.00, "single", True, True, Decimal("8669.00")),
        (300563.00, "married", True, True, Decimal("9171.00")),
        (255674.00, "separate", True, True, Decimal("8591.00")),
        (255674.00, "hoh", True, True, Decimal("7916.00")),
    ],
)
def test_additional_withholding_rounded(wages_ytd, status, self_emp, rounded, expected):
    assert (
        medicare.additional_withholding(wages_ytd, status, self_emp, rounded)
        == expected
    )
