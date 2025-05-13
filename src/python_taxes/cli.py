import sys
from decimal import Decimal
from enum import Enum
from typing import Annotated

from pydantic import StrictBool, validate_call

from python_taxes import CURRENT_TAX_YEAR, currency_field
from python_taxes.federal.income import employer_withholding as income_withholding
from python_taxes.federal.medicare import required_withholding as med_withholding
from python_taxes.federal.social_security import withholding as ss_withholding

try:
    import typer
except ImportError:  # pragma: no cover
    print("Error: typer not found. Command-line (cli) not available.")
    sys.exit(1)

app = typer.Typer()


class PayFrequency(str, Enum):
    semiannual = "semiannual"
    quarterly = "quarterly"
    monthly = "monthly"
    semimonthly = "semimonthly"
    biweekly = "biweekly"
    weekly = "weekly"
    daily = "daily"


class FilingStatus(str, Enum):
    single = "single"
    married = "married"
    separate = "separate"
    hoh = "hoh"


@validate_call
def currency(value: Annotated[Decimal, currency_field]) -> Decimal:
    return value


@app.callback()
def callback():
    """
    Calculate federal income related taxes with python-taxes CLI app: pytax
    """


@app.command()
def med(
    wages: Annotated[
        Decimal, typer.Argument(parser=currency, help="Taxable wages this period")
    ],
    ytd: Annotated[
        Decimal,
        typer.Option(
            parser=currency,
            help="Total taxable wages paid year-to-date",
        ),
    ] = Decimal("0.00"),
    selfemp: Annotated[
        StrictBool,
        typer.Option(help="Whether to calculate as self-employed"),
    ] = False,
    round: Annotated[
        StrictBool,
        typer.Option(help="Whether to round the final value"),
    ] = False,
):
    value = med_withholding(wages, ytd, selfemp, round)
    print(value)


@app.command()
def ss(
    wages: Annotated[
        Decimal,
        typer.Argument(parser=currency, help="Taxable wages this period"),
    ],
    ytd: Annotated[
        Decimal,
        typer.Option(parser=currency, help="Total taxable wages paid year-to-date"),
    ] = Decimal("0.00"),
    selfemp: Annotated[
        StrictBool,
        typer.Option(help="Whether to calculate as self-employed"),
    ] = False,
    year: Annotated[int, typer.Option(help="Enter the tax year")] = CURRENT_TAX_YEAR,
    round: Annotated[
        StrictBool,
        typer.Option(help="Whether to round the final value"),
    ] = False,
):
    value = ss_withholding(wages, ytd, selfemp, year, round)
    print(value)


@app.command()
def income(
    wages: Annotated[
        Decimal,
        typer.Argument(parser=currency, help="Taxable wages this period"),
    ],
    freq: Annotated[
        PayFrequency, typer.Option(help="Pay frequency", case_sensitive=False)
    ] = PayFrequency.biweekly,
    status: Annotated[
        FilingStatus, typer.Option(help="Filing status", case_sensitive=False)
    ] = FilingStatus.single,
    mjobs: Annotated[
        StrictBool,
        typer.Option(help="Multiple jobs: Select True if box in Step 2 on W-4 checked"),
    ] = False,
    credits: Annotated[
        Decimal,
        typer.Option(
            parser=currency, help="Amount to claim for dependents and credits"
        ),
    ] = Decimal("0.00"),
    other: Annotated[
        Decimal,
        typer.Option(parser=currency, help="Income not from jobs"),
    ] = Decimal("0.00"),
    deduct: Annotated[
        Decimal,
        typer.Option(parser=currency, help="Deductions other than standard"),
    ] = Decimal("0.00"),
    extra: Annotated[
        Decimal,
        typer.Option(parser=currency, help="Extra to withhold each period"),
    ] = Decimal("0.00"),
    year: Annotated[int, typer.Option(help="Enter the tax year")] = CURRENT_TAX_YEAR,
    round: Annotated[
        StrictBool,
        typer.Option(help="Whether to round the final value"),
    ] = False,
):
    value = income_withholding(
        wages, freq, status, mjobs, credits, other, deduct, extra, year, round
    )
    print(value)


if __name__ == "__main__":
    app()  # pragma: no cover
