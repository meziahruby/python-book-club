# 16-1 San Francisco weather in 2014
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'sf_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Print header row containing column names
    # for index, header in enumerate(header_row):
    #     print(index, header_row[index])

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%m/%d/%Y")
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print('Missing data for ', current_date)
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot data
f = plt.figure()
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures in SF in 2014")

plt.xlabel('')
f.autofmt_xdate()

plt.ylabel('Temperature (F)')

plt.tick_params(axis='both', which='major')

axes = plt.gca()
axes.set_xlim([dates[0], dates[-1]])

plt.show()

# SF Temperature is more similar to Death Valley than Sitka