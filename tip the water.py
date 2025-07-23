def total_calc(bil_amount,tip_perc):
    total=bil_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"Please say ${total}")

total_calc(270,30)