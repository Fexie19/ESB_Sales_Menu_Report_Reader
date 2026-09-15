import pandas as pd
import os, json
from controllers import loads_menu

data = loads_menu()
CE = data["CE"]

print(CE)


def cup_es(df):
    menu = CE
    total = 0
    for i in menu:
        df_menu = df[df['Menu Name'] == i ]
        total_qty = df_menu['Qty'].sum()
    

        if "BUNDLING PROMO GOFOOD 3 ES KOPI CALF PREMIUM" == i:
            total_qty = total_qty*3
            
        if "Bundling 3 Es Kopi Calf Premium" == i:
            total_qty = total_qty*3

        if "Bundling Es Kopi Calf Premium  + Classic Milk Tea" == i:
            total_qty = total_qty*2

        if "Bundling Chocolate + Es Kopi Calf Premium" == i:
            total_qty = total_qty*2

        total = total + total_qty
        print(f"{i} = {total_qty}")

    print(f"\nTotal Cup Es yang terjual: {total}")