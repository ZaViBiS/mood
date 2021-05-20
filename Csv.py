import pandas as pd
import matplotlib.pyplot as plt
from functions import jsonReader


def jsonToCsv(name):
    data = jsonReader()[name]

    frame = pd.DataFrame(data, columns = ['Time', 'Hello'])

    frame.to_csv('my_csv_export.csv', index=False) # экспортируем в файл


def BuildingAGraphFromCsv():
    data = pd.read_csv("my_csv_export.csv")

    fig = plt.figure()
    plt.plot(data['Time'], data['Hello'])
    fig.autofmt_xdate()
    plt.savefig('line_plot.png') 
