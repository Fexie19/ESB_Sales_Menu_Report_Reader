import pandas as pd
import json
from controllers import loads_menu

data = loads_menu()

DSM = data["DSM"]

def dimsum(df):
    menu = DSM
    total = 0
    for i in menu:
        df_menu = df[df['Menu Name'] == i ]
        total_qty = df_menu['Qty'].sum()
    
        if "Dimsum" == i:
            total_qty = total_qty*4

        if "Dimsum Mentai" == i:
            total_qty = total_qty*4

        total = total + total_qty
        print(f"{i} = {total_qty}")

    print(f"\nTotal Pcs Dimsum yang terjual: {total}")