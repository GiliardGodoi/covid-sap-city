
from datetime import datetime

import pandas as pd
from os import path
from openpyxl import load_workbook

today = datetime.now()
date = datetime(today.year, today.month, today.day)


print(f"Hoje é {today.day}/{today.month}/{today.year}")
answer = input("[S / N]   ")
# if answer.upper() == 'S':
    # date = datetime(today.year, today.month, today.day)

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

data = [date]

for field in fields:
    answer = input(field)
    try:
        value = int(answer)
    except ValueError:
        value = 0
    data.append(value)

print(data)

df = pd.DataFrame([data], columns=columns)

# df.to_excel("teste.xlsx", index=False)
## https://betterprogramming.pub/using-python-pandas-with-excel-d5082102ca27
in_excel = path.join("data", "raw", "BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx")

writer = pd.ExcelWriter(in_excel, engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook(in_excel)

# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets if ws.title != "Sheet1")

reader = pd.read_excel(in_excel, engine="openpyxl")
reader.dropna(how='all')

df.to_excel(writer,
            sheet_name="Planilha1",
            index=False,
            header=False,
            startrow=len(reader))

writer.close()