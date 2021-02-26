
import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

#The enumerate() function returns both of the index of each item and the value of each
# item as you loop through a list.

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

#as an example
#mydate = "2018-07-01"
#converted_date = datetime.strptime(mydate, "%Y-%m-%d")

#print(converted_date)

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

#print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolors='blue', alpha=0.1)


plt.title("SITKA AIRPORT, AK US", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

plt.title("DEATH VALLEY, CA US", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)


plt.show()

fig, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()



fig, (ax1, ax2) = plt.subplots(2, sharex=True)
fig.suptitle('Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US')
ax1.plot(x, y)
ax2.plot(x + 1, -y)

fig, ax = plt.subplots(2) 

