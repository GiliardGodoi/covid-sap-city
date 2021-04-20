import typer
from os import path
from rich.console import Console


from src.charts import (timeseries_compare_confirmed_understudy,
                        timeseries_active_understudy,
                        timeseries_active_cases,
                        timeseries_hospital_cases,
                        timeseries_confirmed_recoveries,
                        barplot_deaths_per_month,
                        barplot_week_evolution,
                        )
from src.storage import read_excel

app = typer.Typer()
console = Console()

data_source = path.join('data', 'raw', 'BOLETIM_DIARIO_CORONAVIRUS_SAP.xlsx')
charts_folder = path.join('data', 'charts')

@app.command()
def feed(many : bool = typer.Option(False,
                                    is_flag=True,
                                    help="Use essa flag para inserir dados para várias datas.")):
    pass

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