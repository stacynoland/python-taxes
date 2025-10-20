from contextlib import nullcontext
from decimal import Decimal

import pytest
from pydantic import ValidationError

from python_taxes.federal import income


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
class TestZeroOrNegative:
    def test_employer_withholding(self, wages, expected):
        with expected as e:
            assert income.employer_withholding(wages) == e

    def test_employer_withholding_pre2020(self, wages, expected):
        with expected as e:
            assert income.employer_withholding_pre_2020(wages) == e


# Tests for income.employer_withholding
@pytest.mark.parametrize(
    "wages, rounded, expected",
    [
        # Not Rounded Tests
        (100, False, Decimal("0.00")),
        (3846.15, False, Decimal("532.35")),
        (3384.62, False, Decimal("430.81")),
        (5769.23, False, Decimal("982.25")),
        (4615.38, False, Decimal("705.33")),
        (2000.00, False, Decimal("163.69")),
        (11538.46, False, Decimal("2702.49")),
        (23076.92, False, Decimal("6740.95")),
        # Rounded Tests
        (100, True, Decimal("0.00")),
        (3846.15, True, Decimal("532.00")),
        (3384.62, True, Decimal("431.00")),
        (5769.23, True, Decimal("982.00")),
        (4615.38, True, Decimal("705.00")),
        (2000.00, True, Decimal("164.00")),
        (11538.46, True, Decimal("2702.00")),
        (23076.92, True, Decimal("6741.00")),
    ],
)
def test_rounding_employer_withholding(wages, rounded, expected):
    assert (
        income.employer_withholding(
            taxable_wages=wages,
            rounded=rounded,
            tax_year=2024,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, pay_freq, expected",
    [
        # Daily Pay Frequency Tests
        (3846.15, "daily", Decimal("1241.48")),
        (3384.62, "daily", Decimal("1070.72")),
        # Weekly Pay Frequency Tests
        (5769.23, "weekly", Decimal("1351.24")),
        (4615.38, "weekly", Decimal("957.97")),
        # Semimonthly Pay Frequency Tests
        (2000.00, "semimonthly", Decimal("157.33")),
        (11538.46, "semimonthly", Decimal("2591.16")),
        # Monthly Pay Frequency Tests
        (23076.92, "monthly", Decimal("5182.32")),
        (3846.15, "monthly", Decimal("296.20")),
        # Quarterly Pay Frequency Tests
        (5769.23, "quarterly", Decimal("211.92")),
        (4615.38, "quarterly", Decimal("96.54")),
        # Semiannual Pay Frequency Tests
        (11538.46, "semiannual", Decimal("423.85")),
        (23076.92, "semiannual", Decimal("1777.23")),
    ],
)
def test_pay_frequency_employer_withholding(wages, pay_freq, expected):
    assert (
        income.employer_withholding(
            taxable_wages=wages,
            pay_frequency=pay_freq,
            tax_year=2024,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, filing_status, multiple_jobs, expected",
    [
        # Single/Separate + Multiple Jobs Tests
        (3846.15, "single", True, Decimal("721.89")),
        (3384.62, "separate", True, Decimal("611.12")),
        # Married  Tests
        (5769.23, "married", False, Decimal("641.62")),
        (4615.38, "married", False, Decimal("401.23")),
        # Married + Multiple Jobs Tests
        (2000.00, "married", True, Decimal("163.69")),
        (11538.46, "married", True, Decimal("2702.49")),
        # Hoh Tests
        (23076.92, "hoh", False, Decimal("6577.58")),
        (3846.15, "hoh", False, Decimal("405.42")),
        # Hoh + Multiple Jobs Tests
        (5769.23, "hoh", True, Decimal("1269.56")),
        (4615.38, "hoh", True, Decimal("880.48")),
    ],
)
def test_status_jobs_employer_withholding(
    wages, filing_status, multiple_jobs, expected
):
    if multiple_jobs:
        assert (
            income.employer_withholding(
                taxable_wages=wages,
                filing_status=filing_status,
                multiple_jobs=multiple_jobs,
                tax_year=2024,
            )
            == expected
        )
    else:
        assert (
            income.employer_withholding(
                taxable_wages=wages,
                filing_status=filing_status,
                tax_year=2024,
            )
            == expected
        )


@pytest.mark.parametrize(
    "wages, tax_credit, expected",
    [
        # Tax Credit Tests
        (3846.15, 5000, Decimal("340.04")),
        (2000.00, 5325, Decimal("0.00")),
        (11538.46, 10000, Decimal("2317.87")),
        (23076.92, 10000, Decimal("6356.34")),
    ],
)
def test_tax_credit_employer_withholding(wages, tax_credit, expected):
    assert (
        income.employer_withholding(
            taxable_wages=wages,
            tax_credits=tax_credit,
            tax_year=2024,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, other_income, expected",
    [
        # Other Income Tests
        (3846.15, 10000, Decimal("616.96")),
        (2000.00, 10000, Decimal("210.81")),
        (11538.46, 20000, Decimal("2971.72")),
        (23076.92, 20000, Decimal("7010.18")),
    ],
)
def test_other_income_employer_withholding(wages, other_income, expected):
    assert (
        income.employer_withholding(
            taxable_wages=wages,
            other_income=other_income,
            tax_year=2024,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, deductions, expected",
    [
        # Deductions Tests
        (3846.15, 5000, Decimal("490.04")),
        (2000.00, 5000, Decimal("140.62")),
        (11538.46, 10000, Decimal("2567.87")),
        (23076.92, 10000, Decimal("6606.34")),
    ],
)
def test_deductions_employer_withholding(wages, deductions, expected):
    assert (
        income.employer_withholding(
            taxable_wages=wages,
            deductions=deductions,
            tax_year=2024,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, extra_withhold, expected",
    [
        # Extra Withholding Tests
        (3846.15, 300, Decimal("832.35")),
        (2000.00, 300, Decimal("463.69")),
        (11538.46, 5000, Decimal("7702.49")),
        (23076.92, 5000, Decimal("11740.95")),
    ],
)
def test_extra_employer_withholding(wages, extra_withhold, expected):
    assert (
        income.employer_withholding(
            taxable_wages=wages,
            extra_withholding=extra_withhold,
            tax_year=2024,
        )
        == expected
    )


# Tests for income.employer_withholding_pre_2020
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
def test_rounding_employer_withholding_pre2020(wages, rounded, expected):
    assert (
        income.employer_withholding_pre_2020(
            taxable_wages=wages,
            rounded=rounded,
            tax_year=2024,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, status, expected",
    [
        # Marital Status Tests
        (3846.15, "separate", Decimal("605.11")),
        (2000.00, "married", Decimal("146.92")),
        (11538.46, "married", Decimal("2083.58")),
        (23076.92, "married", Decimal("5578.63")),
    ],
)
def test_status_employer_withholding_pre2020(wages, status, expected):
    assert (
        income.employer_withholding_pre_2020(
            taxable_wages=wages,
            marital_status=status,
            tax_year=2024,
        )
        == expected
    )


@pytest.mark.parametrize(
    "wages, extra_withhold, expected",
    [
        # Extra Withholding Tests
        (3846.15, 300, Decimal("905.11")),
        (2000.00, 300, Decimal("503.38")),
        (11538.46, 5000, Decimal("7818.26")),
        (23076.92, 5000, Decimal("11856.72")),
    ],
)
def test__employer_withholding_pre2020(wages, extra_withhold, expected):
    assert (
        income.employer_withholding_pre_2020(
            taxable_wages=wages,
            extra_withholding=extra_withhold,
            tax_year=2024,
        )
        == expected
    )
