from decimal import Decimal

from pydantic import ValidationError
import pytest

from python_taxes.federal.calculators import social_security


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
