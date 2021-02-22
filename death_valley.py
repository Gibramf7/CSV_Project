import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

#The enumerate() function returns both of the index of each item and the value of each
# item as you loop through a list.

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
lows = []
dates = []

#as an example
#mydate = "2018-07-01"
#converted_date = datetime.strptime(mydate, "%Y-%m-%d")

#print(converted_date)

for row in csv_file:
    try:
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(converted_date)
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs.append(highs)
        lows.append(lows)
        dates.append(converted_date)


#print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolors='blue', alpha=0.1)


plt.title("Daily high and low temperatures, 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

plt.show()

figure2, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
