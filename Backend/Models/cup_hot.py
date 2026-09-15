import pandas as pd
import json
from controllers import loads_menu

data = loads_menu()

CH = data["CH"]

def cup_hot(df):
    menu = CH
    total = 0
    for i in menu:
        df_menu = df[df['Menu Name'] == i ]
        total_qty = df_menu['Qty'].sum()
    
        total = total + total_qty
        print(f"{i} = {total_qty}")

    print(f"\nTotal Cup Hot yang terjual: {total}")