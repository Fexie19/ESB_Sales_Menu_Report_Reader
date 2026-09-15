import pandas as pd
import os, json
from Models.cup_es import cup_es
from Models.cup_frost import cup_frost
from Models.cup_hot import cup_hot
from Models.botol import botol
from Models.dimsum import dimsum    
from Models.kaleng310 import kaleng310
from Models.roti import roti

def read_file():
    skripdir = os.path.dirname(os.path.abspath(__file__))
    file= os.path.join(skripdir, '1-15.xlsx')
    if not os.path.exists(file):
        print(f"Error: File {file} tidak ditemukan.")
        return None
    
    df = None
    for h in [10, 11, 12, 13, 14, 15]:
        try:    
            temp_df = pd.read_excel(file, header=h)
            if 'Menu Name' in temp_df.columns:
                df = temp_df
                break
        except Exception:
            continue
    return (df)



def main(df):
    if df is not None:
        df['Menu Name'] = df['Menu Name'].fillna('')

        print(f"""
Hasil Kalkulasi :
\n
CUP ES | CUP FROST | BOTOL 1LT | KALENG | CUP HOT
\n {cup_es(df)} \n\n {cup_frost(df)} \n\n {cup_hot(df)} \n\n {botol(df)} \n\n {kaleng310(df)} \n\n {dimsum(df)} \n\n {roti(df)}
""")
        
    else:
        print('gagal menjalankan eksekusi')

main(read_file())
