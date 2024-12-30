from decimal import Decimal

from percentage import MAX, TaxBracket


standard = {
    2024: [
        TaxBracket(min=Decimal('0.00'), max=Decimal('16299.99'), withhold_amount=Decimal('0.00'), percentage=0),
        TaxBracket(min=Decimal('16300.00'), max=Decimal('39499.99'), withhold_amount=Decimal('0.00'), percentage=10),
        TaxBracket(min=Decimal('39500.00'), max=Decimal('110599.99'), withhold_amount=Decimal('2320.00'), percentage=12),
        TaxBracket(min=Decimal('110600.00'), max=Decimal('217349.99'), withhold_amount=Decimal('10852.00'), percentage=22),
        TaxBracket(min=Decimal('217350.00'), max=Decimal('400199.99'), withhold_amount=Decimal('34337.00'), percentage=24),
        TaxBracket(min=Decimal('400200.00'), max=Decimal('503749.99'), withhold_amount=Decimal('78221.00'), percentage=32),
        TaxBracket(min=Decimal('503750.00'), max=Decimal('747499.99'), withhold_amount=Decimal('111357.00'), percentage=35),
        TaxBracket(min=Decimal('747500.00'), max=MAX, withhold_amount=Decimal('196669.50'), percentage=37),
    ],
}

multiple_jobs = {
    2024: [
        TaxBracket(min=Decimal('0.00'), max=Decimal('14599.99'), withhold_amount=Decimal('0.00'), percentage=0),
        TaxBracket(min=Decimal('14600.00'), max=Decimal('26199.99'), withhold_amount=Decimal('0.00'), percentage=10),
        TaxBracket(min=Decimal('26200.00'), max=Decimal('61749.99'), withhold_amount=Decimal('1160.00'), percentage=12),
        TaxBracket(min=Decimal('61750.00'), max=Decimal('115124.99'), withhold_amount=Decimal('5426.00'), percentage=22),
        TaxBracket(min=Decimal('115125.00'), max=Decimal('206549.99'), withhold_amount=Decimal('17168.50'), percentage=24),
        TaxBracket(min=Decimal('206550.00'), max=Decimal('258324.99'), withhold_amount=Decimal('39110.50'), percentage=32),
        TaxBracket(min=Decimal('258325.00'), max=Decimal('380199.99'), withhold_amount=Decimal('55678.50'), percentage=35),
        TaxBracket(min=Decimal('380200.00'), max=MAX, withhold_amount=Decimal('98334.75'), percentage=37),
    ],
}
