def calculate_total_bill(amount: float, tip_percent: int) -> float:
    f_amount = float(amount)
    f_tip_percent = float(tip_percent)
    total = f_amount + (f_amount * (f_tip_percent / 100))
    return round(total, 2)
