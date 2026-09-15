import pandas as pd
import json
from controllers import loads_menu

data = loads_menu()

CF = data["CF"]

def cup_frost(df):
    menu = CF
    total = 0
    for i in menu:
        df_menu = df[df['Menu Name'] == i ]
        total_qty = df_menu['Qty'].sum()
    
        if "Bundling Fusion Black + Berry Shoot" == i:
                    total_qty = total_qty*2

        total = total + total_qty
        print(f"{i} = {total_qty}")

    print(f"\nTotal Cup frost yang terjual: {total}")