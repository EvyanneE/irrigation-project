import random
import pandas as pd
import random
import datetime

idList = []
hrList = []
outputList =[]



idList = [i for i in range(1,1001)]

for i in range(1000):
    x = random.randint(1,24)
    hrList.append(x)

for i in range(1000):
    x = random.randint(0,1000)
    outputList.append(x)



timestampList = pd.date_range(end = datetime.datetime(2024,4,24,11,0,0), periods = 1000, freq='H')
df = pd.DataFrame({'Datetime': timestampList})

zipped = list(zip(idList, hrList, outputList, timestampList))

df = pd.DataFrame(zipped, columns=['id','hr','output','timestamp'])



gfg_csv_data = df.to_csv('irrigationData.csv', index = False)