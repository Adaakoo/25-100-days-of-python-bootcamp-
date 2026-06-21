import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_count = 0
red_count = 0
black_count = 0

for color in data["Primary Fur Color"]:
    if color == "Gray":
        grey_count += 1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1
    else:
        pass

data_dict = {
    "Color" : ["Grey","Red","Black"],
    "Count" : [grey_count,red_count,black_count]
}
df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("data_dict.csv")