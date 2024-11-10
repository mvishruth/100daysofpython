import os

print(os.getcwd())

with open('weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)


import pandas

data = pandas.read_csv("weather_data.csv")
print (type(data))   # pandas.core.frame.DataFrame
print (type(data["temp"]))  # pandas.core.series.Series
#
data_dict = data.to_dict()
print(data_dict)  
#
temp_list = data["temp"].to_list()
print(len(data_dict)) 
#
print(data["temp"].mean())
#
print(data["temp"].max())


# How to fetch data in rows

# print( data[data.day == "Monday"])

# monday = (data[(data.temp == data.temp.max())])
# print(monday.temp * 9/5 + 32)

# data.to_csv("new_data.csv")

print(max(data["temp"]))
print(data["temp"].max())

data.temp.temp
