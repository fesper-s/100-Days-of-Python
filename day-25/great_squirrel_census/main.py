import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231030.csv")

grey_squirrels_cout = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_cout = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_cout = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_cout, red_squirrels_cout, black_squirrels_cout]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
