from datetime import datetime

import pandas as pd
from rich.traceback import install

from src.questioner import ask4YesOrNo, ask4date, ask4int, ask4option, greeting

install()

fields = [
    "Data",
    "Descartados",
    "Em investigação",
    "Confirmados",
    "Examinados",
    "Recuperados",
    "Ativos",
    "Hospitalizados",
    "Domicílio",
    "Óbitos"
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

msg = '''
# Boletins Diário Santo Antônio da Platina - PR

Utilitário para coletar os dados dos boletins diários sobre os casos de *COVID-19* no Município de Santo Antônio da Platina - PR

'''

greeting(msg)

width = max(len(f) for f in fields) + 2

data = list()

go_on = True

while go_on:
    line = list()
    for i, field in enumerate(fields):
        if i == 0:
            ans = ask4date(f"{field}:", justify='left', width=width, default=datetime.now())
        else:
            ans = ask4int(f"{field}:", justify='left', width=width, default=0)
        line.append(ans)
    go_on = ask4YesOrNo("Deseja continuar?")
    data.append(line)

print(data)
