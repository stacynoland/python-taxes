import subprocess

import pytest


@pytest.mark.parametrize(
    "wages, expected",
    [
        (100, 1.45),
    ],
)
def test_med_cli(wages, expected):
    process = subprocess.run(
        ["poetry", "run", "pytax", "med", f"{wages}"], capture_output=True, text=True
    )
    assert process.returncode == 0
    assert f"{expected}" in process.stdout


@pytest.mark.parametrize(
    "wages, expected",
    [
        (100, 6.20),
    ],
)
def test_ss_cli(wages, expected):
    process = subprocess.run(
        ["poetry", "run", "pytax", "ss", f"{wages}"], capture_output=True, text=True
    )
    assert process.returncode == 0
    assert f"{expected}" in process.stdout


@pytest.mark.parametrize(
    "wages, expected",
    [
        (100, 0),
        (3846.15, 532.35),
    ],
)
def test_income_cli(wages, expected):
    process = subprocess.run(
        ["poetry", "run", "pytax", "income", f"{wages}"], capture_output=True, text=True
    )
    assert process.returncode == 0
    assert f"{expected}" in process.stdout
