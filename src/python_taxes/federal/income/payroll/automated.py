from decimal import Decimal
from typing import Annotated, Literal, Optional, Union

from pydantic import Field, StrictBool, validate_call

from python_taxes.federal import rounding
from ..tables.percentage.automated import single, married, hoh


PAY_FREQUENCY = {
    'Semiannual': 2,
    'Quarterly': 4,
    'Monthly': 12,
    'Semimonthly': 24,
    'Biweekly': 26,
    'Weekly': 52,
    'Daily': 260,
}

CURRENT_TAX_YEAR = 2024


@validate_call
def employer_withholding(
    taxable_wages: Annotated[Decimal, Field(ge=Decimal("0.01"), decimal_places=2)],
    pay_frequency: Literal['Semiannual', 'Quarterly', 'Monthly', 'Semimonthly',
                           'Biweekly', 'Weekly', 'Daily'] = 'Biweekly',
    filing_status: Literal['single', 'married', 'separate', 'hoh'] = 'single',
    multiple_jobs: Optional[StrictBool] = False,
    tax_credits: Optional[Decimal] = Decimal("0.00"),
    other_income: Optional[Decimal] = Decimal("0.00"),
    deductions: Optional[Decimal] = Decimal("0.00"),
    extra_withholding: Optional[Decimal] = Decimal("0.00"),
    tax_year: Optional[Union[int, str]] = CURRENT_TAX_YEAR,
    rounded: Optional[StrictBool] = False,
) -> Decimal:
    """Calculate income tax withholding.

    Formula used if Form W-4 is 2020 or later.
    If W-4 is 2019 or earlier, use employer_withholding_pre_2020 instead.

    Parameters:
    taxable_wages -- Wages earned this year
    pay_frequency -- Number of pay periods per year
    filing_status -- Filing status (default 'single')
    multiple_jobs -- Indicates if box in Step 2 on W-4 is checked
    tax_credits -- Dependant claims and other credits from Step 3 on W-4
    other_income -- Income not from jobs - Step 4 on W-4
    deductions -- If claiming deductions other than standard - Step 4 on W-4
    extra_withholding -- Extra amount to withhold each pay period - Step 4 on W-4
    tax_year -- Year for which you are filing (default CURRENT_TAX_YEAR)
    rounded -- Round to nearest whole dollar amount (default False)
    """

    # Steps 1a-1i
    match filing_status:
        case 'single' | 'separate' if multiple_jobs:
            withholding_schedule = single.multiple_jobs
        case 'single' | 'separate':
            withholding_schedule = single.standard_schedule
            deductions = deductions + Decimal("8600.00")
        case 'married' if multiple_jobs:
            withholding_schedule = married.multiple_jobs
        case 'married':
            withholding_schedule = married.standard_schedule
            deductions = deductions + Decimal("12900.00")
        case 'hoh' if multiple_jobs:
            withholding_schedule = hoh.multiple_jobs
        case 'hoh':
            withholding_schedule = hoh.standard_schedule
            deductions = deductions + Decimal("8600.00")

    pay_freq = PAY_FREQUENCY[pay_frequency]

    adjusted_wage = ((taxable_wages * pay_freq) + other_income) - deductions

    # Step 2
    for row in withholding_schedule[tax_year]:
        if adjusted_wage >= row.min and adjusted_wage < row.max:
            withholding_rate = row
            break

    tax_withholding = (
        (adjusted_wage - withholding_rate.min)
        * withholding_rate.percent
        + withholding_rate.withhold_amount
    )

    withheld_this_period = tax_withholding / pay_freq

    # Step 3
    if tax_credits:
        withheld_this_period = withheld_this_period - (tax_credits / pay_freq)

    # Step 4
    if extra_withholding:
        withheld_this_period = withheld_this_period + extra_withholding

    return Decimal(withheld_this_period).quantize(rounding[rounded])


@validate_call
def employer_withholding_pre_2020(
    taxable_wages: Annotated[Decimal, Field(ge=Decimal("0.01"), decimal_places=2)],
    pay_frequency: Literal['Semiannual', 'Quarterly', 'Monthly', 'Semimonthly',
                           'Biweekly', 'Weekly', 'Daily'] = 'Biweekly',
    marital_status: Literal['single', 'married', 'separate'] = 'single',
    allowances_claimed: int = 0,
    extra_withholding: Optional[Decimal] = Decimal("0.00"),
    tax_year: Optional[Union[int, str]] = CURRENT_TAX_YEAR,
    rounded: Optional[StrictBool] = False,
) -> Decimal:
    """Calculate income tax withholding if Form W-4 is 2019 or earlier.

    Parameters:
    taxable_wages -- Wages earned this year
    pay_frequency -- Number of pay periods per year
    marital_status -- Marital status (default 'single')
    allowances_claimed -- Number of allowances claimed in Step 5 on W-4
    extra_withholding -- Extra amount to withhold each pay period - Step 6 on W-4
    tax_year -- Year for which you are filing (default CURRENT_TAX_YEAR)
    rounded -- Round to nearest whole dollar amount (default False)
    """

    # Steps 1a-1c and 1j-1l
    match marital_status:
        case 'single' | 'separate':
            withholding_schedule = single.standard_schedule
        case 'married':
            withholding_schedule = married.standard_schedule

    pay_freq = PAY_FREQUENCY[pay_frequency]

    allowances = allowances_claimed * Decimal("4300.00")

    adjusted_wage = (taxable_wages * pay_freq) - allowances

    # Step 2
    for rate_row in withholding_schedule[tax_year]:
        if adjusted_wage >= rate_row.min and adjusted_wage < rate_row.max:
            withholding_rate = rate_row
            break

    tax_withholding = (
        (adjusted_wage - withholding_rate.min)
        * withholding_rate.percent
        + withholding_rate.withhold_amount
    )

    withheld_this_period = tax_withholding / pay_freq

    # Step 3 skipped if W4 is from 2019 or earlier
    # Step 4
    if extra_withholding:
        withheld_this_period = withheld_this_period + extra_withholding

    return Decimal(withheld_this_period).quantize(rounding[rounded])
