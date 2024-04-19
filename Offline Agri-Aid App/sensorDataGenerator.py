import random
import pandas as pd
import random
import datetime

tempList = []
moistList = []
NList =[]
PList =[]
KList =[]


for i in range(1000):
    x = random.randint(10,30)
    tempList.append(x)

for i in range(1000):
    x = random.randint(20,70)
    moistList.append(x)

for i in range(1000):
    x = random.randint(0,200)
    NList.append(x)

for i in range(1000):
    x = random.randint(0,100)
    PList.append(x)

for i in range(1000):
    x = random.randint(0,400)
    KList.append(x)


timeList = pd.date_range(end = datetime.datetime(2024,4,24,11,0,0), periods = 1000, freq='H')
df = pd.DataFrame({'Datetime': timeList})

zipped = list(zip(tempList, moistList, NList, PList, KList, timeList))

df = pd.DataFrame(zipped, columns=['temperature','moisture', 'N', 'P', 'K', 'timestamp'])



gfg_csv_data = df.to_csv('sensorData.csv', index = False)