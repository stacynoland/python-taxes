import sys
from decimal import Decimal
from typing import Union

from pydantic import StrictBool
from typing_extensions import Annotated

from python_taxes import CURRENT_TAX_YEAR
from python_taxes.federal.income import employer_withholding as income_withholding
from python_taxes.federal.medicare import required_withholding as med_withholding
from python_taxes.federal.social_security import withholding as ss_withholding

try:
    import typer
except ImportError:
    print("Error: typer not found. Command-line (cli) not available.")
    sys.exit(1)

app = typer.Typer()


def parse_decimal(value: Union[str, int, float]) -> Decimal:
    try:
        return Decimal(value)
    except TypeError as e:
        print(f"TypeError: {e}")
        raise typer.BadParameter(f"Cannot convert value to Decimal: {value}")


@app.callback()
def callback():
    """
    Calculate federal income related taxes with python-taxes CLI app: pytax
    """


@app.command()
def med(
    wages: Annotated[
        Decimal, typer.Argument(parser=parse_decimal, help="Taxable wages this period")
    ],
    ytd: Annotated[
        Decimal,
        typer.Option(
            parser=parse_decimal, help="Total taxable wages paid year-to-date"
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
        typer.Argument(parser=parse_decimal, help="Taxable wages this period"),
    ],
    ytd: Annotated[
        Decimal,
        typer.Option(
            parser=parse_decimal, help="Total taxable wages paid year-to-date"
        ),
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
        typer.Argument(parser=parse_decimal, help="Taxable wages this period"),
    ],
    freq: Annotated[str, typer.Option(help="Pay frequency")] = "biweekly",
    status: Annotated[str, typer.Option(help="Filing status")] = "single",
    mjobs: Annotated[
        StrictBool,
        typer.Option(help="Select True if box in Step 2 on W-4 checked"),
    ] = False,
    credits: Annotated[
        Decimal,
        typer.Option(
            parser=parse_decimal, help="Amount to claim for dependents and credits"
        ),
    ] = Decimal("0.00"),
    other: Annotated[
        Decimal,
        typer.Option(parser=parse_decimal, help="Income not from jobs"),
    ] = Decimal("0.00"),
    deduct: Annotated[
        Decimal,
        typer.Option(parser=parse_decimal, help="Deductions other than standard"),
    ] = Decimal("0.00"),
    extra: Annotated[
        Decimal,
        typer.Option(parser=parse_decimal, help="Extra to withhold each period"),
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
    app()
