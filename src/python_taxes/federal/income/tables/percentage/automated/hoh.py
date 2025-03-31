from decimal import Decimal

from .. import MAX, RateSchedule


standard = {
    2023: [
        RateSchedule(min=Decimal("0.00"), max=Decimal("12199.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateSchedule(min=Decimal("12200.00"), max=Decimal("27899.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateSchedule(min=Decimal("27900.00"), max=Decimal("72049.99"), withhold_amount=Decimal("1570.00"), percent=12),
        RateSchedule(min=Decimal("72050.00"), max=Decimal("107549.99"), withhold_amount=Decimal("6868.00"), percent=22),
        RateSchedule(min=Decimal("107550.00"), max=Decimal("194299.99"), withhold_amount=Decimal("14678.00"), percent=24),
        RateSchedule(min=Decimal("194300.00"), max=Decimal("243449.99"), withhold_amount=Decimal("35498.00"), percent=32),
        RateSchedule(min=Decimal("243450.00"), max=Decimal("590299.99"), withhold_amount=Decimal("51226.00"), percent=35),
        RateSchedule(min=Decimal("590300.00"), max=MAX, withhold_amount=Decimal("172623.50"), percent=37),
    ],
    2024: [
        RateSchedule(min=Decimal("0.00"), max=Decimal("13299.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateSchedule(min=Decimal("13300.00"), max=Decimal("29849.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateSchedule(min=Decimal("29850.00"), max=Decimal("76399.99"), withhold_amount=Decimal("1655.00"), percent=12),
        RateSchedule(min=Decimal("76400.00"), max=Decimal("113799.99"), withhold_amount=Decimal("7241.00"), percent=22),
        RateSchedule(min=Decimal("113800.00"), max=Decimal("205249.99"), withhold_amount=Decimal("15469.00"), percent=24),
        RateSchedule(min=Decimal("205250.00"), max=Decimal("256999.99"), withhold_amount=Decimal("37417.00"), percent=32),
        RateSchedule(min=Decimal("257000.00"), max=Decimal("622649.99"), withhold_amount=Decimal("53977.00"), percent=35),
        RateSchedule(min=Decimal("622650.00"), max=MAX, withhold_amount=Decimal("181954.50"), percent=37),
    ],
    2025: [
        RateSchedule(min=Decimal("0.00"), max=Decimal("13899.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateSchedule(min=Decimal("13900.00"), max=Decimal("30899.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateSchedule(min=Decimal("30900.00"), max=Decimal("78749.99"), withhold_amount=Decimal("1700.00"), percent=12),
        RateSchedule(min=Decimal("78750.00"), max=Decimal("117249.99"), withhold_amount=Decimal("7442.00"), percent=22),
        RateSchedule(min=Decimal("117250.00"), max=Decimal("211199.99"), withhold_amount=Decimal("15912.00"), percent=24),
        RateSchedule(min=Decimal("211200.00"), max=Decimal("264399.99"), withhold_amount=Decimal("38460.00"), percent=32),
        RateSchedule(min=Decimal("264400.00"), max=Decimal("640249.99"), withhold_amount=Decimal("55484.00"), percent=35),
        RateSchedule(min=Decimal("640250.00"), max=MAX, withhold_amount=Decimal("187031.50"), percent=37),
    ]
}

multiple_jobs = {
    2023: [
        RateSchedule(min=Decimal("0.00"), max=Decimal("10399.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateSchedule(min=Decimal("10400.00"), max=Decimal("18249.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateSchedule(min=Decimal("18250.00"), max=Decimal("40324.99"), withhold_amount=Decimal("785.00"), percent=12),
        RateSchedule(min=Decimal("40325.00"), max=Decimal("58074.99"), withhold_amount=Decimal("3434.00"), percent=22),
        RateSchedule(min=Decimal("58075.00"), max=Decimal("101449.99"), withhold_amount=Decimal("7339.00"), percent=24),
        RateSchedule(min=Decimal("101450.00"), max=Decimal("126024.99"), withhold_amount=Decimal("17749.00"), percent=32),
        RateSchedule(min=Decimal("126025.00"), max=Decimal("299449.99"), withhold_amount=Decimal("25613.00"), percent=35),
        RateSchedule(min=Decimal("299450.00"), max=MAX, withhold_amount=Decimal("86311.75"), percent=37),
    ],
    2024: [
        RateSchedule(min=Decimal("0.00"), max=Decimal("10949.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateSchedule(min=Decimal("10950.00"), max=Decimal("19224.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateSchedule(min=Decimal("19225.00"), max=Decimal("42499.99"), withhold_amount=Decimal("827.50"), percent=12),
        RateSchedule(min=Decimal("42500.00"), max=Decimal("61199.99"), withhold_amount=Decimal("3620.50"), percent=22),
        RateSchedule(min=Decimal("61200.00"), max=Decimal("106924.99"), withhold_amount=Decimal("7734.50"), percent=24),
        RateSchedule(min=Decimal("106925.00"), max=Decimal("132799.99"), withhold_amount=Decimal("18708.50"), percent=32),
        RateSchedule(min=Decimal("132800.00"), max=Decimal("315624.99"), withhold_amount=Decimal("26988.50"), percent=35),
        RateSchedule(min=Decimal("315625.00"), max=MAX, withhold_amount=Decimal("90977.25"), percent=37),
    ],
    2025: [
        RateSchedule(min=Decimal("0.00"), max=Decimal("11249.99"), withhold_amount=Decimal("0.00"), percent=0),
        RateSchedule(min=Decimal("11250.00"), max=Decimal("19749.99"), withhold_amount=Decimal("0.00"), percent=10),
        RateSchedule(min=Decimal("19750.00"), max=Decimal("43674.99"), withhold_amount=Decimal("850.00"), percent=12),
        RateSchedule(min=Decimal("43675.00"), max=Decimal("62924.99"), withhold_amount=Decimal("3721.00"), percent=22),
        RateSchedule(min=Decimal("62925.00"), max=Decimal("109899.99"), withhold_amount=Decimal("7956.00"), percent=24),
        RateSchedule(min=Decimal("109900.00"), max=Decimal("136499.99"), withhold_amount=Decimal("19230.00"), percent=32),
        RateSchedule(min=Decimal("136500.00"), max=Decimal("324424.99"), withhold_amount=Decimal("27742.00"), percent=35),
        RateSchedule(min=Decimal("324425.00"), max=MAX, withhold_amount=Decimal("93515.75"), percentage=37),
    ]
}
