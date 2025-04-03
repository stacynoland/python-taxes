from decimal import Decimal

from .. import MAX, RateRow


standard_schedule = {
    2023: [
        RateRow(min=Decimal("0.00"), max=Decimal("14799.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("14800.00"), max=Decimal("36799.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("36800.00"), max=Decimal("104249.99"), withhold_amount=Decimal("2200.00"), percent=12),
        RateRow(min=Decimal("104250.00"), max=Decimal("205549.99"), withhold_amount=Decimal("10294.00"), percent=22),
        RateRow(min=Decimal("205550.00"), max=Decimal("378999.99"), withhold_amount=Decimal("32580.00"), percent=24),
        RateRow(min=Decimal("379000.00"), max=Decimal("477299.99"), withhold_amount=Decimal("74208.00"), percent=32),
        RateRow(min=Decimal("477300.00"), max=Decimal("708549.99"), withhold_amount=Decimal("105664.00"), percent=35),
        RateRow(min=Decimal("708550.00"), max=MAX, withhold_amount=Decimal("186601.50"), percent=37),
    ],
    2024: [
        RateRow(min=Decimal("0.00"), max=Decimal("16299.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("16300.00"), max=Decimal("39499.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("39500.00"), max=Decimal("110599.99"), withhold_amount=Decimal("2320.00"), percent=12),
        RateRow(min=Decimal("110600.00"), max=Decimal("217349.99"), withhold_amount=Decimal("10852.00"), percent=22),
        RateRow(min=Decimal("217350.00"), max=Decimal("400199.99"), withhold_amount=Decimal("34337.00"), percent=24),
        RateRow(min=Decimal("400200.00"), max=Decimal("503749.99"), withhold_amount=Decimal("78221.00"), percent=32),
        RateRow(min=Decimal("503750.00"), max=Decimal("747499.99"), withhold_amount=Decimal("111357.00"), percent=35),
        RateRow(min=Decimal("747500.00"), max=MAX, withhold_amount=Decimal("196669.50"), percent=37),
    ],
    2025: [
        RateRow(min=Decimal("0.00"), max=Decimal("17099.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("17100.00"), max=Decimal("40949.9"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("40950.00"), max=Decimal("114049.9"), withhold_amount=Decimal("2385.00"), percent=12),
        RateRow(min=Decimal("114050.00"), max=Decimal("223799.9"), withhold_amount=Decimal("11157.00"), percent=22),
        RateRow(min=Decimal("223800.00"), max=Decimal("411699.9"), withhold_amount=Decimal("35302.00"), percent=24),
        RateRow(min=Decimal("411700.00"), max=Decimal("518149.9"), withhold_amount=Decimal("80398.00"), percent=32),
        RateRow(min=Decimal("518150.00"), max=Decimal('768699.99'), withhold_amount=Decimal("114462.00"), percent=35),
        RateRow(min=Decimal("768700.00"), max=MAX, withhold_amount=Decimal("202154.50"), percent=37),
    ],
}

multiple_jobs = {
    2023: [
        RateRow(min=Decimal("0.00"), max=Decimal("13849.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("13850.00"), max=Decimal("24849.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("24850.00"), max=Decimal("58574.99"), withhold_amount=Decimal("1100.00"), percent=12),
        RateRow(min=Decimal("58575.00"), max=Decimal("109224.99"), withhold_amount=Decimal("5147.00"), percent=22),
        RateRow(min=Decimal("109225.00"), max=Decimal("195949.99"), withhold_amount=Decimal("16290.00"), percent=24),
        RateRow(min=Decimal("195950.00"), max=Decimal("245099.99"), withhold_amount=Decimal("37104.00"), percent=32),
        RateRow(min=Decimal("245100.00"), max=Decimal("360724.99"), withhold_amount=Decimal("52832.00"), percent=35),
        RateRow(min=Decimal("360725.00"), max=MAX, withhold_amount=Decimal("93300.75"), percent=37),
    ],
    2024: [
        RateRow(min=Decimal("0.00"), max=Decimal("14599.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("14600.00"), max=Decimal("26199.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("26200.00"), max=Decimal("61749.99"), withhold_amount=Decimal("1160.00"), percent=12),
        RateRow(min=Decimal("61750.00"), max=Decimal("115124.99"), withhold_amount=Decimal("5426.00"), percent=22),
        RateRow(min=Decimal("115125.00"), max=Decimal("206549.99"), withhold_amount=Decimal("17168.50"), percent=24),
        RateRow(min=Decimal("206550.00"), max=Decimal("258324.99"), withhold_amount=Decimal("39110.50"), percent=32),
        RateRow(min=Decimal("258325.00"), max=Decimal("380199.99"), withhold_amount=Decimal("55678.50"), percent=35),
        RateRow(min=Decimal("380200.00"), max=MAX, withhold_amount=Decimal("98334.75"), percent=37),
    ],
    2025: [
        RateRow(min=Decimal("0.00"), max=Decimal("14999.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateRow(min=Decimal("15000.00"), max=Decimal("26924.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateRow(min=Decimal("26925.00"), max=Decimal("63474.99"), withhold_amount=Decimal("1192.50"), percent=12),
        RateRow(min=Decimal("63475.00"), max=Decimal("118349.99"), withhold_amount=Decimal("5578.50"), percent=22),
        RateRow(min=Decimal("118350.00"), max=Decimal("212299.99"), withhold_amount=Decimal("17651.00"), percent=24),
        RateRow(min=Decimal("212300.00"), max=Decimal("265524.99"), withhold_amount=Decimal("40199.00"), percent=32),
        RateRow(min=Decimal("265525.00"), max=Decimal("390799.99"), withhold_amount=Decimal("57231.00"), percent=35),
        RateRow(min=Decimal("390800.00"), max=MAX, withhold_amount=Decimal("101077.25"), percent=37),
    ],
}
