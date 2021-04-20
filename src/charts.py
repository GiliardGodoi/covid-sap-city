

from os import path

import matplotlib.ticker as plticker
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns

plt.rcParams["figure.figsize"] = (10, 5)
params = {
    'axes.facecolor' : 'white',
    'axes.titlesize' : 'larger',
    'axes.titleweight' : 'bold',
    'axes.edgecolor': 'gray',
    "axes.grid" : True,
    "grid.linewidth": 0.9,
    'grid.linestyle': '--',
    'axes.grid.which' : 'major'
    }

sns.set_style("whitegrid", params)

def timeseries_compare_confirmed_understudy(frame, dest=None):
    '''
    Title: SAP - COVID-19 - Evolução dos casos

    Columns:
        EM INVESTIGAÇÃO
        CONFIRMADOS

    Note:

    '''
    plt.figure()
    ax = sns.lineplot(data=frame[['EM INVESTIGACAO', 'CONFIRMADOS']],
                palette="tab10"
                )

    _ = ax.set_title("SAP - COVID-19 - Evolução dos casos")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.xaxis.grid(False)
    sns.despine(left=True)

    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '01-evolucao-casos.png'))


def timeseries_active_understudy(frame, dest=None):
    '''
    Title: Santo Antônio da Platina - COVID-19

    Columns:
        ATIVOS
        EM INVESTIGAÇÃO

    Notes:
    '''
    plt.figure()
    ax = sns.lineplot(data=frame[['ATIVOS','EM INVESTIGACAO']],
                palette="tab10"
                )
    _ = ax.set_title("Santo Antônio da Platina - COVID-19")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    # ax.set_ylim([-10, 300])
    ax.xaxis.grid()
    sns.despine(left=True)

    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '02-relacao-ativos-investigacao.png'))


def timeseries_active_cases(frame, dest=None):
    '''
    Title: SAP COVID-19 - Evolução dos casos ativos

    Columns:
        ATIVOS

    Notes:
    '''
    plt.figure()
    ax = sns.lineplot(data=frame[['ATIVOS']], legend=False)
    _ = ax.set_title("SAP COVID-19 - Evolução dos casos ativos")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.xaxis.grid()
    sns.despine(left=True)

    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '03-evolucao-casos-ativos.png'))


def timeseries_hospital_cases(frame, dest=None):
    '''
    Title: SAP COVID-19 - Evolução dos casos hospitalizados

    Columns:
        ATIVOS

    Notes:
    '''
    plt.figure()
    ax = sns.lineplot(data=frame[['HOSPITAL']],
                palette="tab10",
                legend=False
                )
    _ = ax.set_title("SAP COVID-19 - Evolução dos casos hospitalizados")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    # ax.set_ylim([-10, 250])
    ax.xaxis.grid()
    sns.despine(left=True)
    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '04-evolucao-hospitalizados.png'))


def timeseries_confirmed_recoveries(frame, dest=None):
    '''
    Title: Santo Antônio da Platina - COVID-19

    Columns:
        CONFIRMADOS
        RECUPERADOS

    Notes:
    '''
    plt.figure()
    ax = sns.lineplot(data=frame[['CONFIRMADOS','RECUPERADOS']],
                palette="tab10"
                )
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    _ = ax.set_title("Santo Antônio da Platina - COVID-19")
    ax.xaxis.grid()
    sns.despine(left=True)

    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '05-relacao-confirmados-recuperados.png'))


def moving_means(frame, days=7, dest=None):
    '''
    Title: SAP - Covid19 - Média móvel

    Columns:
        ATIVOS

    Notes:
    '''
    plt.figure()
    ax = frame['ATIVOS'].plot()
    ax = frame['ATIVOS'].rolling(days).mean().plot()
    _ = ax.set_title(f"SAP - Covid-19 - Média Móvel {days} dias")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.xaxis.grid()
    sns.despine(left=True)

    if dest is not None and path.exists(dest):
        plt.savefig(path.join(days, '06-media-movel.png'))


def timeseries_deaths_evolution(frame, dest=None):
    '''
    Title: Evolução do número de óbitos

    Columns:
        OBITOS

    Notes:
    '''
    fig = sns.relplot(kind="line", data=frame['OBITOS'], height=5, aspect=2)
    ax = fig.facet_axis(0,0)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.set(yticks=range(4,20))
    sns.despine(left=True)
    _ = fig.set(title="Evolução do número de óbitos")
    plt.tight_layout()
    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '07-evolucao-obitos.png'))


def barplot_deaths_per_month(frame, dest=None):
    '''
    Title: SAP COVID-19 - Total de mortes por mês

    Columns:
        OBITOS

    Notes:
    '''
    plt.figure()
    deaths = frame['OBITOS'].diff(periods=1)

    groupdeaths = deaths.groupby([(deaths.index.year),(deaths.index.month)]).sum()

    def formatter(label):
        yearDict = {
            2020 : '20',
            2021 : '21',
            2020 : '22'
        }
        monthDict = {
            1:'Jan',
            2:'Fev',
            3:'Mar',
            4:'Abr',
            5:'Maio',
            6:'Jun',
            7:'Jul',
            8:'Ago',
            9:'Set',
            10:'Out',
            11:'Nov',
            12:'Dez'}

        return f"{monthDict[label[1]]} {yearDict[label[0]]}"

    # formatter((2020, 7))

    labels = [formatter(label) for label in groupdeaths.index]

    # labels

    ax = groupdeaths.plot(kind='bar', color='steelblue')

    ax.set(title='SAP COVID-19 - Total de mortes por mês')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticklabels(labels)
    ax.set_xlabel("Meses")
    ax.tick_params(axis="x", rotation=0)
    sns.despine(left=True)

    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '08-evolucao-obitos-por-mes.png'))


def barplot_week_evolution(frame, dest=None):
    '''
    Title: Total de novos casos e recuperação por semana

    Columns:
        NOVOS_CASOS
        RECUPERADOS_DIA

    '''
    df = frame.resample('W-MON').sum()
    loc = plticker.MultipleLocator(base=3.0)

    labels = [date.strftime("%d/%m") for date in df.index]

    plt.figure(figsize=(15, 7))
    ax = plt.subplot()
    plt.bar(labels, df['NOVOS_CASOS'], color='steelblue', label='Novos casos')
    plt.bar(labels, df['RECUPERADOS_DIA'], color='orange', alpha=0.8, label='Recuperados na semana')
    ax.yaxis.grid(True)
    ax.xaxis.set_major_locator(loc)
    ax.set(title="Total de novos casos e recuperação por semana")
    plt.legend()
    plt.xticks(rotation=40)
    plt.tight_layout()

    sns.despine(left=True)

    if dest is not None and path.exists(dest):
        plt.savefig(path.join(dest, '09-compara-novos-casos-recuperados-dia.png'))
