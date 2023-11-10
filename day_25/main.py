# with open("C:\\Users\\ROHIT\\Desktop\\100 Days Python\\day_25\\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("C:\\Users\\ROHIT\\Desktop\\100 Days Python\\day_25\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data: 
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

# import pandas
# data = pandas.read_csv("C:\\Users\\ROHIT\\Desktop\\100 Days Python\\day_25\\weather_data.csv")
# # printing avg temprature
# temp_list = data["temp"].tolist()
# avg_temp = (sum(temp_list)/len(temp_list))
# print(avg_temp)
# # another way
# avg = (data["temp"].mean())
# print(avg)
# # you can also do this 
# print(data.condition)


# # now how will you get holde of rows in the data
# print(data[data.day == "Monday"])

# # getting holde of row with max temprature

# print(data[data.temp == data.temp.max()])

# # how to convert monday temp c to f

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 +  32
# print(monday_temp_f)

# creating a dataframe from datadct
# data_dict = {
#     "students": ["Amey", "james", "Rohit"],
#     "scores": [55, 28, 96]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("C:\\Users\\ROHIT\\Desktop\\100 Days Python\\day_25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = data["Primary Fur Color"].tolist()

# create a pandas DataFrame from the list of colors
df = pandas.DataFrame({'color': color_list})
# count the number of occurrences of each color and store the results in a new DataFrame
counts = df['color'].value_counts().reset_index()
counts.columns = ['color', 'count']

# write the counts to a new CSV file
counts.to_csv('color_counts.csv', index=False)
