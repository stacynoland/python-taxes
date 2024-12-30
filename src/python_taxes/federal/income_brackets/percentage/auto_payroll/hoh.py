from decimal import Decimal

from percentage import MAX, TaxBracket


standard = {
    2024: [
        TaxBracket(min=Decimal('0.00'), max=Decimal('13299.99'), withhold_amount=Decimal('0.00'), percentage=0),
        TaxBracket(min=Decimal('13300.00'), max=Decimal('29849.99'), withhold_amount=Decimal('0.00'), percentage=10),
        TaxBracket(min=Decimal('29850.00'), max=Decimal('76399.99'), withhold_amount=Decimal('1655.00'), percentage=12),
        TaxBracket(min=Decimal('76400.00'), max=Decimal('113799.99'), withhold_amount=Decimal('7241.00'), percentage=22),
        TaxBracket(min=Decimal('113800.00'), max=Decimal('205249.99'), withhold_amount=Decimal('15469.00'), percentage=24),
        TaxBracket(min=Decimal('205250.00'), max=Decimal('256999.99'), withhold_amount=Decimal('37417.00'), percentage=32),
        TaxBracket(min=Decimal('257000.00'), max=Decimal('622649.99'), withhold_amount=Decimal('53977.00'), percentage=35),
        TaxBracket(min=Decimal('622650.00'), max=MAX, withhold_amount=Decimal('181954.50'), percentage=35),
    ],
}

multiple_jobs = {
    2024: [
        TaxBracket(min=Decimal('0.00'), max=Decimal('10949.99'), withhold_amount=Decimal('0.00'), percentage=0),
        TaxBracket(min=Decimal('10950.00'), max=Decimal('19224.99'), withhold_amount=Decimal('0.00'), percentage=10),
        TaxBracket(min=Decimal('19225.00'), max=Decimal('42499.99'), withhold_amount=Decimal('827.50'), percentage=12),
        TaxBracket(min=Decimal('42500.00'), max=Decimal('61199.99'), withhold_amount=Decimal('3620.50'), percentage=22),
        TaxBracket(min=Decimal('61200.00'), max=Decimal('106924.99'), withhold_amount=Decimal('7734.50'), percentage=24),
        TaxBracket(min=Decimal('106925.00'), max=Decimal('132799.99'), withhold_amount=Decimal('18708.50'), percentage=32),
        TaxBracket(min=Decimal('132800.00'), max=Decimal('315624.99'), withhold_amount=Decimal('26988.50'), percentage=35),
        TaxBracket(min=Decimal('315625.00'), max=MAX, withhold_amount=Decimal('90977.25'), percentage=35),
    ],
}
