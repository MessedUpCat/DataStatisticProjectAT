import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#importing raw data
data1 = pd.read_csv("DATA/solarData269.txt", sep=",", header=None,  names=["Panel_location_type_and_ID", "Date","kWh produced", "On/Off"])
data2 = pd.read_csv("DATA/solarData280.txt", sep=",", header=None,  names=["Panel_location_type_and_ID", "Date","kWh produced", "On/Off"])
data3 = pd.read_csv("DATA/solarData290.txt", sep=",", header=None,  names=["Panel_location_type_and_ID", "Date","kWh produced", "On/Off"])
data4 = pd.read_csv("DATA/solarData391.txt", sep=",", header=None,  names=["Panel_location_type_and_ID", "Date","kWh produced", "On/Off"])

frames = [data1, data2,data3,data4]
data = pd.concat(frames)
print(data)
print("shit data")

data[['location', 'type','ID']] = data.Panel_location_type_and_ID.str.split("_", expand = True)
#fixing tables

data = data.drop(['Panel_location_type_and_ID'], axis = 1)
print(data)

#fixing date fotmat
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m%d')
print(data)

#fixing type location ID
data.type = data.type.str.slice(4)
data.location = data.location.str.slice(3)
data.ID = data.ID.str.slice(2)
print(data)
#exporting data
data.to_csv('SolarData.txt',index=False)