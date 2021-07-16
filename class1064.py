import csv
import numpy as np
import plotly.express as px

def plot():
    file = open("data4.csv")
    d = csv.DictReader(file)
    fig = px.scatter(d , x = "Coffee in ml",y = "sleep in hours")
    fig.show()

def getdatasource():
    Coffee = []
    sleep = []
    
    file = open("data4.csv")
    d = csv.DictReader(file)
    for i in d:
        sleep.append(float(i["sleep in hours"]))
        Coffee.append(float(i["Coffee in ml"]))

    return {"y":sleep,"x":Coffee}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def setup():
    datasource = getdatasource()
    findcorrelation(datasource)
    plot()

setup()

