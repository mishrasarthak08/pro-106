import csv
import numpy as np
import plotly.express as px

def plot():
    file = open("data3.csv")
    d = csv.DictReader(file)
    fig = px.scatter(d, x = "Marks In Percentage",y = "Days Present")
    fig.show()

def getdatasource():
    days = []
    marks = []
    
    file = open("data3.csv")
    d = csv.DictReader(file)
    for i in d:
        marks.append(float(i["Marks In Percentage"]))
        days.append(float(i["Days Present"]))

    return {"x":marks,"y":days}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def setup():
    datasource = getdatasource()
    findcorrelation(datasource)
    plot()

setup()

