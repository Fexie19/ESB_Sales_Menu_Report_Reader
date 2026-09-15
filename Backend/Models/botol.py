import pandas as pd
import json
from controllers import loads_menu

data = loads_menu()

B1LT = data["B1LT"]

def botol(df):
    menu = B1LT
    total = 0
    for i in menu:
        df_menu = df[df['Menu Name'] == i ]
        total_qty = df_menu['Qty'].sum()

        if "BUNDLING PROMO GOFOOD 2 LITER PREMIUM" == i:
            total_qty = total_qty*2
        
        if "BUNDLING PROMO GOFOOD 3 ES KOPI CALF PREMIUM" == i:
            total_qty = total_qty*3

        total = total + total_qty
        print(f"{i} = {total_qty}")

    print(f"\nTotal Botol 1lT yang terjual: {total}")