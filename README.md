![Python Taxes Image](https://github.com/user-attachments/assets/6c62946b-e749-46bb-a84e-6321397f1753)
[![Tests](https://github.com/stacynoland/python-taxes/actions/workflows/tests.yml/badge.svg)](https://github.com/stacynoland/python-taxes/actions/workflows/tests.yml)
![Coverage](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fstacynoland.com%2Fpython-taxes%2Fcoverage.json&query=%24.totals.percent_covered_display&suffix=%25&label=coverage&color=3fb831)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-taxes?logo=python&logoColor=yellow)
[![PyPI - Version](https://img.shields.io/pypi/v/python-taxes)](https://pypi.org/project/python-taxes/)
![PyPI - Status](https://img.shields.io/pypi/status/python-taxes)
[![Black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)

> Disclaimer: This library is not intended to be used for tax advice. Please consult a tax professional for any tax-related questions or concerns.

Python-Taxes is a library designed to make calculating US Federal taxes easy.

The library supports Social Security, Medicare, and Federal Income taxes for tax years 2023 to 2025. Please note, 2025 is only added for future tax season.

`CURRENT_TAX_YEAR` is set to 2024.

## Installation

To install the library, you can use pip or another dependency manager like Poetry.

`pip install python-taxes`

or

`poetry add python-taxes`

## Usage

### Social Security Tax

To calculate Social Security tax, use the `social_security` module:

```python
from python_taxes.federal import social_security

social_security.withholding(5000)  # Returns the amount withheld for Social Security tax

social_security.withholding(
                taxable_wages=3000,
                taxable_wages_ytd=100000,
                self_employed=False,
                tax_year=2024,
                rounded=True,
            )
```
---
### Medicare Tax

To calculate Medicare tax, use the `medicare` module. There are two functions available:

`medicare.required_withholding` - Returns the required amount to withhold for Medicare tax regardless of filing status.
`medicare.additional_withholding` - Returns the amount that should be withheld based on filing status, including Additional Medicare tax.

```python
from python_taxes.federal import medicare

medicare.required_withholding(5000)  # Returns the amount withheld for Medicare tax

medicare.required_withholding(
                taxable_wages=5000,
                taxable_wages_ytd=100000,
                self_employed=True,
                rounded=True,
            )

medicare.additional_withholding(100000, "married")  # Returns the amount withheld for Medicare Tax and Additional Medicare tax, if applicable, based on filing status.

medicare.additional_withholding(
                taxable_wages_ytd=100000,
                filing_status="married",
                self_employed=False,
                rounded=True,
            )
```
---
### Federal Income Tax

To calculate Federal Income tax, use the `income` package. Currently, the only payroll withholding supported is for automated systems. Specifically, the percentage tables in IRS Publication 15-T section 1 (Percentage Method Tables for Automated Payroll Systems).

```python
from python_taxes.federal import income

income.employer_withholding(10000)  # Returns the amount withheld for Federal Income tax

income.employer_withholding(
                taxable_wages=10000,
                pay_frequency="monthly",
                filing_status="married",
                multiple_jobs=False,
                tax_credits=0,
                other_income=0,
                deductions=0,
                extra_withholding=0,
                tax_year=2024,
                rounded=True,
            )

income.employer_withholding_pre_2020(10000)  # Returns the amount withheld for Federal Income tax - using this method is required if Form W-4 is from 2019 or earlier.

income.employer_withholding_pre_2020(
                taxable_wages=10000,
                pay_frequency="monthly",
                marital_status="married",
                allowances_claimed=0,
                extra_withholding=0,
                tax_year=2024,
                rounded=False,
            )
```
