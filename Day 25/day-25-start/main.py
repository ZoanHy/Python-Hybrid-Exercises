import csv

# CSV: Comma Separated Values


# with open("weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     # data = weather_data.readlines()
#     # print(data)
#
# print(temperatures)


import pandas

# data = pandas.read_csv("weather-data.csv")
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(round(average_temp, 2))
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # Get Data in Columns
#
# print((data["condition"]))
# print(data.condition)

# Get Data in Rows
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print(float(monday.temp) * 9 / 5 + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 46, 69]
# }
#
# data_convert = pandas.DataFrame(data_dict)
# print(data_convert)
# data_convert.to_csv("new_data_student.csv")

# ,Fur Color,Count
# 0,grey,2473
# 1,red.392

data_squirrel = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
list_primary_colors = data_squirrel["Primary Fur Color"].dropna().to_list()
list_fur_color = list(set(list_primary_colors))

count_color = []


for color in list_fur_color:
    count = 0
    for color_primary in list_primary_colors:
        if color == color_primary:
            count += 1
    count_color.append(count)

print(list_primary_colors)
print(list_fur_color)

list_primary_colors_dict = {}
list_primary_colors_dict["Fur Color"] = list_fur_color
list_primary_colors_dict["Count"] = count_color

pandas.DataFrame(list_primary_colors_dict).to_csv("squirrel_count.csv")