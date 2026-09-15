import pandas as pd
import json
from controllers import loads_menu

data = loads_menu()

RT = data["RT"]

def roti(df):
    menu = RT
    total = 0
    for i in menu:
        df_menu = df[df['Menu Name'] == i ]
        total_qty = df_menu['Qty'].sum()

        total = total + total_qty
        print(f"{i} = {total_qty}")

    print(f"\nTotal Pcs Roti yang terjual: {total}")