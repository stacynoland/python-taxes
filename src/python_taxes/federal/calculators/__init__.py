from decimal import Decimal, getcontext, ROUND_HALF_UP


getcontext().rounding = ROUND_HALF_UP

ROUNDED = Decimal('1.')

NOT_ROUNDED = Decimal('0.01')

rounding = {
    True: ROUNDED,
    False: NOT_ROUNDED,
}
