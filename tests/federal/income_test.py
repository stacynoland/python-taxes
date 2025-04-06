from decimal import Decimal

import pytest
from pydantic import ValidationError

from python_taxes.federal import income


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
    def test_employer_withholding_zero(self, wages, expected):
        with expected as e:
            assert income.employer_withholding(wages) == e

    def test_additional_withholding_zero(self, wages, expected):
        with expected as e:
            assert income.employer_withholding_pre_2020(wages) == e


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
            assert income.employer_withholding(wages) == e

    def test_additional_withholding_negative(self, wages, expected):
        with expected as e:
            assert income.employer_withholding_pre_2020(wages) == e
