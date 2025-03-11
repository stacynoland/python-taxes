from decimal import Decimal

import pytest
from pydantic import ValidationError

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

class TestZero:
    def test_required(self, wages, expected):
        assert (medicare.required_withholding(wages) == expected)

    def test_additional(self, wages, expected):
        assert (medicare.additional_withholding(wages) == expected)


@pytest.mark.parametrize(
    "wages, wages_ytd, self_emp, expected",
    [
        (0, 0, False, pytest.raises(ValidationError)),
        ("0.01", "0.00", True, pytest.raises(ValidationError)),
    ],
)

class TestZeroAllParams:
    def test_full_required(self, wages, wages_ytd, self_emp, expected):
        assert (
            medicare.required_withholding(self, wages, wages_ytd, self_emp) == expected
        )

    def test_full_additional(self, wages_ytd, self_emp, expected):
        assert (
            medicare.additional_withholding(self, wages_ytd, self_emp) == expected
        )


# Negative Tests
@pytest.mark.parametrize(
    "wages, expected",
    [
        (-1.00, pytest.raises(ValidationError)),
        ("-10000", pytest.raises(ValidationError)),
    ],
)

class TestNegative:
    def test_required(self, wages, expected):
        assert (medicare.required_withholding(wages) == expected)

    def test_additional(self, wages, expected):
        assert (medicare.additional_withholding(wages) == expected)
