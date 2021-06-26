from os import stat
import pandas as pd
import plotly.figure_factory as pf
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv('data.csv')
temp = df['temp'].to_list()

tempMean = statistics.mean(temp)
tempSD = statistics.stdev(temp)

graph = pf.create_distplot([temp], ['Temp'], show_hist= False)
graph.add_trace(go.Scatter(x = [tempMean,tempMean], y = [0,0.1], 
    mode = "lines", name = "Temperature Mean"))
#graph.show()

print("Mean: ", tempMean)
print("St Dev: ", tempSD)


def getSample(count):
    sampleData = []
    for i in range(0,count):
        index = random.randint(0, len(temp)-1)
        value = temp[index]
        sampleData.append(value)
    
    sampleMean = statistics.mean(sampleData)
    sampleSD = statistics.stdev(sampleData)
    return sampleMean

meanList = []
for i in range(0,1000):
    randomMean = getSample(400)
    meanList.append(randomMean)

meanOfMeans = statistics.mean(meanList)
sdOfMeans = statistics.stdev(meanList)


graph = pf.create_distplot([meanList], ['Mean Data'], show_hist= False)
graph.add_trace(go.Scatter(x = [meanOfMeans,meanOfMeans], y = [0,1.5], 
    mode = "lines", name = "Temperature Mean"))
graph.show()

#Mean remains almost the same in the sample data
print('Mean of Means: ', meanOfMeans)
#new SD becomes 1/10th of the orignal sd
print('SD of Means  ', sdOfMeans)
