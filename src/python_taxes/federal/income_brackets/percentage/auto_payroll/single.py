from decimal import Decimal

from percentage import MAX, TaxBracket


standard = {
    2024: [
        TaxBracket(min=Decimal('0.00'), max=Decimal('5999.99'), withhold_amount=Decimal('0.00'), percentage=0),
        TaxBracket(min=Decimal('6000.00'), max=Decimal('17599.99'), withhold_amount=Decimal('0.00'), percentage=10),
        TaxBracket(min=Decimal('17600.00'), max=Decimal('53149.99'), withhold_amount=Decimal('1160.00'), percentage=12),
        TaxBracket(min=Decimal('53150.00'), max=Decimal('106524.99'), withhold_amount=Decimal('5426.00'), percentage=22),
        TaxBracket(min=Decimal('106525.00'), max=Decimal('197949.99'), withhold_amount=Decimal('17168.50'), percentage=24),
        TaxBracket(min=Decimal('197950.00'), max=Decimal('249724.99'), withhold_amount=Decimal('39110.50'), percentage=32),
        TaxBracket(min=Decimal('249725.00'), max=Decimal('615349.99'), withhold_amount=Decimal('55678.50'), percentage=35),
        TaxBracket(min=Decimal('615350.00'), max=MAX, withhold_amount=Decimal('183647.25'), percentage=37),
    ],
}

multiple_jobs = {
    2024: [
        TaxBracket(min=Decimal('0.00'), max=Decimal('5999.99'), withhold_amount=Decimal('0.00'), percentage=0),
        TaxBracket(min=Decimal('6000.00'), max=Decimal('17599.99'), withhold_amount=Decimal('0.00'), percentage=10),
        TaxBracket(min=Decimal('17600.00'), max=Decimal('53149.99'), withhold_amount=Decimal('1160.00'), percentage=12),
        TaxBracket(min=Decimal('53150.00'), max=Decimal('106524.99'), withhold_amount=Decimal('5426.00'), percentage=22),
        TaxBracket(min=Decimal('106525.00'), max=Decimal('197949.99'), withhold_amount=Decimal('17168.50'), percentage=24),
        TaxBracket(min=Decimal('197950.00'), max=Decimal('249724.99'), withhold_amount=Decimal('39110.50'), percentage=32),
        TaxBracket(min=Decimal('249725.00'), max=Decimal('615349.99'), withhold_amount=Decimal('55678.50'), percentage=35),
        TaxBracket(min=Decimal('615350.00'), max=MAX, withhold_amount=Decimal('183647.25'), percentage=37),
    ],
}
