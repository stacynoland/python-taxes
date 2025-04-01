from decimal import Decimal

from .. import MAX, RateRow


standard_schedule = {
    2023: [
        RateRow(min=Decimal("0.00"), max=Decimal("5249.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("5250.00"), max=Decimal("16249.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("16250.00"), max=Decimal("49974.99"), withhold_amount=Decimal("1100.00"), percent=12),
        RateRow(min=Decimal("49975.00"), max=Decimal("100624.99"), withhold_amount=Decimal("5147.00"), percent=22),
        RateRow(min=Decimal("100625.00"), max=Decimal("187349.99"), withhold_amount=Decimal("16290.00"), percent=24),
        RateRow(min=Decimal("187350.00"), max=Decimal("236499.99"), withhold_amount=Decimal("37104.00"), percent=32),
        RateRow(min=Decimal("236500.00"), max=Decimal("583374.99"), withhold_amount=Decimal("52832.00"), percent=35),
        RateRow(min=Decimal("583375.00"), max=MAX, withhold_amount=Decimal("174238.25"), percent=37),
    ],
    2024: [
        RateRow(min=Decimal("0.00"), max=Decimal("5999.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("6000.00"), max=Decimal("17599.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("17600.00"), max=Decimal("53149.99"), withhold_amount=Decimal("1160.00"), percent=12),
        RateRow(min=Decimal("53150.00"), max=Decimal("106524.99"), withhold_amount=Decimal("5426.00"), percent=22),
        RateRow(min=Decimal("106525.00"), max=Decimal("197949.99"), withhold_amount=Decimal("17168.50"), percent=24),
        RateRow(min=Decimal("197950.00"), max=Decimal("249724.99"), withhold_amount=Decimal("39110.50"), percent=32),
        RateRow(min=Decimal("249725.00"), max=Decimal("615349.99"), withhold_amount=Decimal("55678.50"), percent=35),
        RateRow(min=Decimal("615350.00"), max=MAX, withhold_amount=Decimal("183647.25"), percent=37),
    ],
    2025: [
        RateRow(min=Decimal("0.00"), max=Decimal("6399.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("6400.00"), max=Decimal("18324.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("18325.00"), max=Decimal("54874.99"), withhold_amount=Decimal("1192.50"), percent=12),
        RateRow(min=Decimal("54875.00"), max=Decimal("109749.99"), withhold_amount=Decimal("5578.50"), percent=22),
        RateRow(min=Decimal("109750.00"), max=Decimal("203699.99"), withhold_amount=Decimal("17651.00"), percent=24),
        RateRow(min=Decimal("203700.00"), max=Decimal("256924.99"), withhold_amount=Decimal("40199.00"), percent=32),
        RateRow(min=Decimal("256925.00"), max=Decimal("632749.99"), withhold_amount=Decimal("57231.00"), percent=35),
        RateRow(min=Decimal("632750.00"), max=MAX, withhold_amount=Decimal("188769.75"), percent=37),
    ]
}

multiple_jobs = {
    2023: [
        RateRow(min=Decimal("0.00"), max=Decimal("6924.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("6925.00"), max=Decimal("12424.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("12425.00"), max=Decimal("29287.99"), withhold_amount=Decimal("550.00"), percent=12),
        RateRow(min=Decimal("29288.00"), max=Decimal("54612.99"), withhold_amount=Decimal("2573.50"), percent=22),
        RateRow(min=Decimal("54613.00"), max=Decimal("97974.99"), withhold_amount=Decimal("8145.00"), percent=24),
        RateRow(min=Decimal("97975.00"), max=Decimal("122549.99"), withhold_amount=Decimal("18552.00"), percent=32),
        RateRow(min=Decimal("122550.00"), max=Decimal("295987.99"), withhold_amount=Decimal("26416.00"), percent=35),
        RateRow(min=Decimal("295988.00"), max=MAX, withhold_amount=Decimal("87119.13"), percent=37),
    ],
    2024: [
        RateRow(min=Decimal("0.00"), max=Decimal("7299.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("7300.00"), max=Decimal("13099.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("13100.00"), max=Decimal("30874.99"), withhold_amount=Decimal("580.00"), percent=12),
        RateRow(min=Decimal("30875.00"), max=Decimal("57562.99"), withhold_amount=Decimal("2713.00"), percent=22),
        RateRow(min=Decimal("57563.00"), max=Decimal("103274.99"), withhold_amount=Decimal("8584.25"), percent=24),
        RateRow(min=Decimal("103275.00"), max=Decimal("129162.99"), withhold_amount=Decimal("19555.25"), percent=32),
        RateRow(min=Decimal("129163.00"), max=Decimal("311974.99"), withhold_amount=Decimal("27839.25"), percent=35),
        RateRow(min=Decimal("311975.00"), max=MAX, withhold_amount=Decimal("91823.63"), percentage=37),
    ],
    2025: [
        RateRow(min=Decimal("0.00"), max=Decimal("7499.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("7500.00"), max=Decimal("13462.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("13463.00"), max=Decimal("31737.99"), withhold_amount=Decimal("596.25"), percent=12),
        RateRow(min=Decimal("31738.00"), max=Decimal("59174.99"), withhold_amount=Decimal("2789.25"), percent=22),
        RateRow(min=Decimal("59175.00"), max=Decimal("106149.99"), withhold_amount=Decimal("8825.50"), percent=24),
        RateRow(min=Decimal("106150.00"), max=Decimal("132762.99"), withhold_amount=Decimal("20099.50"), percent=32),
        RateRow(min=Decimal("132763.00"), max=Decimal("320674.99"), withhold_amount=Decimal("28615.50"), percent=35),
        RateRow(min=Decimal("320675.00"), max=MAX, withhold_amount=Decimal("94384.88"), percentage=37),
    ]
}
