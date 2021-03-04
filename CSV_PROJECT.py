import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

place_name = ''
fig, ax = plt.subplots(2)
for i in range (2):

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        print(header_row)
        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        name_index = header_row.index('NAME')


        dates = []
        highs =[]
        lows = []
        for row in reader:
            place_name = row[name_index]
            print(place_name)
            
            converted_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {converted_date}")
            else:
                dates.append(converted_date)
                highs.append(high)
                lows.append(low)
        
        # Plot the high and low temperatures
        ax[i].plot(dates, highs, c='red', alpha=0.5)
        ax[i].plot(dates, lows, c='blue', alpha=0.5)
        ax[i].fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
        ax[i].set_title(place_name, fontsize=12)


        filename = 'death_valley_2018_simple.csv'
        i += 1

# Format plot.
suptitle = f"Temperature comparison between SITKA AIRPORT, AK US and {place_name}"
plt.suptitle(suptitle, fontsize=13)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.tick_params(axis='both', labelsize=12)

plt.show()

