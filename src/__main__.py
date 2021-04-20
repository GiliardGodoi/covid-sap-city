import typer
from os import path
from rich.console import Console
from datetime import datetime

import pandas as pd
from rich.traceback import install

from src.questioner import ask4YesOrNo, ask4date, ask4int, ask4option, greeting


from src.charts import (timeseries_compare_confirmed_understudy,
                        timeseries_active_understudy,
                        timeseries_active_cases,
                        timeseries_hospital_cases,
                        timeseries_confirmed_recoveries,
                        barplot_deaths_per_month,
                        barplot_week_evolution,
                        )
from src.storage import read_excel

install()

app = typer.Typer()
console = Console()

data_source = path.join('data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx')
charts_folder = path.join('data', 'charts')

@app.command()
def feed(many : bool = typer.Option(False,
                                    is_flag=True,
                                    help="Use essa flag para inserir dados para várias datas.")):


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

@app.command()
def charts(source : str = typer.Argument(data_source, help='Arquivo que contem os dados'),
            dest : str = typer.Argument(charts_folder, help='Pasta onde as imagens serão salvas'),
            ):
    # print(source, dest)
    with console.status("[bold green] Lendo arquivo..."):
        frame = read_excel(source)
        frame['NOVOS_CASOS'] = frame['CONFIRMADOS'].diff(periods=1)
        frame['RECUPERADOS_DIA'] = frame['RECUPERADOS'].diff(periods=1)
        frame['DESCARTADOS_DIA'] = frame['DESCARTADOS'].diff(periods=1)

    with console.status("Plotando gráficos...", spinner='clock'):
        timeseries_compare_confirmed_understudy(frame, charts_folder)
        timeseries_active_understudy(frame, charts_folder)
        timeseries_active_cases(frame, charts_folder)
        timeseries_hospital_cases(frame, charts_folder)
        timeseries_confirmed_recoveries(frame, charts_folder)
        barplot_deaths_per_month(frame, charts_folder)
        barplot_week_evolution(frame, charts_folder)



if __name__ == "__main__":
    app()