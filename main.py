
from datetime import datetime

import pandas as pd
from os import path
from openpyxl import load_workbook

today = datetime.now()

print(f"Hoje é {today.day}/{today.month}/{today.year}")
answer = input("[S / N]   ")

print(answer)

print(10*'- ')
print("Inserir dados: \n\n")

fields = [
    "Descartados:  ",
    "Em investigação:  ",
    "Confirmados:  ",
    "Examinados:  ",
    "Recuperados:  ",
    "Ativos:  ",
    "Hospitalizados:  ",
    "Domicílio:  ",
    "Óbitos:  "
]

columns = [
    "DATA",
    "DESCARTADOS",
    "EM INVESTIGACAO",
    "CONFIRMADOS",
    "EXAMINADOS",
    "RECUPERADOS",
    "ATIVOS",
    "HOSPITAL",
    "DOMICILIO",
    "OBITOS"
]

data = [f"{today.day}/{today.month}/{today.year}"]

for field in fields:
    answer = input(field)
    try:
        value = int(answer)
    except ValueError:
        value = 0
    data.append(value)


df = pd.DataFrame([data], columns=columns)
# df.to_excel("teste.xlsx", index=False)
## https://betterprogramming.pub/using-python-pandas-with-excel-d5082102ca27
infile = path.join("data", "raw", "BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx")
writer = pd.ExcelWriter(infile, engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook(infile)
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(infile, engine="openpyxl")
# write out the new sheet
df.to_excel(writer, index=False,header=False,startrow=len(reader)+1)

writer.close()
