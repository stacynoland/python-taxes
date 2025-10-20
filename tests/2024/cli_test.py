import pytest
from typer.testing import CliRunner

from python_taxes.cli import app

runner = CliRunner()


@pytest.mark.parametrize(
    "wages, exit_code, expected",
    [
        (100, 0, 1.45),
        ("bad", 2, "Error"),
    ],
)
def test_med_cli(wages, exit_code, expected):
    result = runner.invoke(app, ["med", str(wages)], catch_exceptions=False)
    assert result.exit_code == exit_code
    assert f"{expected}" in result.output


@pytest.mark.parametrize(
    "wages, exit_code, expected",
    [
        (100, 0, 6.20),
        ("1000 00", 2, "Error"),
    ],
)
def test_ss_cli(wages, exit_code, expected):
    result = runner.invoke(app, ["ss", str(wages)])
    assert result.exit_code == exit_code
    assert f"{expected}" in result.output


@pytest.mark.parametrize(
    "wages, exit_code, expected",
    [
        (100, 0, 0),
        (3846.15, 0, 532.35),
        (b"bad", 2, "Error"),
    ],
)
def test_income_cli(wages, exit_code, expected):
    result = runner.invoke(app, ["income", str(wages), "--year", "2024"])
    assert result.exit_code == exit_code
    assert f"{expected}" in result.output
