import pandas as pd
import matplotlib.pyplot as plt
from functions import jsonReader


def jsonToCsv(name, utilizerName):
    pngName = str(name) + '.png'
    
    data = jsonReader()[name]
    data = pd.DataFrame(data, columns = ['Time', 'Appraisal'])

    fig = plt.figure()

    plt.ylim(1,10) # ограничение оси y (1, 10)
    plt.title(utilizerName) # Заголовок
    plt.grid() # Сетка
    plt.plot(data['Time'], data['Appraisal'])

    fig.autofmt_xdate()
    plt.savefig(pngName)

    return pngName
