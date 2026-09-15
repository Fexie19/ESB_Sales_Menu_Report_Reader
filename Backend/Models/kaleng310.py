import pandas as pd
import json
from controllers import loads_menu

data = loads_menu()

K310 = data["K310"]

def kaleng310(df):
    menu = K310
    total = 0
    for i in menu:
        df_menu = df[df['Menu Name'] == i ]
        total_qty = df_menu['Qty'].sum()

        total = total + total_qty
        print(f"{i} = {total_qty}")

    print(f"\nTotal Kaleng 310ml yang terjual: {total}")