import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset
flight = pd.read_csv("flight.csv")

# Checking missing data
print(flight.info())
print(flight.miles.count())

# Extracting columns from the dataset
coach_price = flight["coach_price"]
first_price = flight["firstclass_price"]

# Summary statistics - Average coach price and first class price
avg_coach = round(np.mean(coach_price), 2)
avg_first = round(np.mean(first_price), 2)

# Adjusting the size of the figure
plt.figure(figsize = (6, 7))

# Creating combined boxplot for the distribution of coach prices and first class prices
data_to_plot = [coach_price, first_price]
plt.boxplot(data_to_plot)

# Adding the title and labels
title_text = "Distribution of Ticket Prices by Class\n" + \
             "(Avg Coach: " + str(avg_coach) + " €, Avg First Class: " + str(avg_first) + " €)"
labels = ['Coach Prices', 'First Class Prices']
plt.title(title_text)
plt.ylabel("Price [€]")
ax = plt.subplot()
ax.set_xticklabels(labels)
plt.grid(axis='y', linestyle='--', alpha=0.7)

#plt.savefig("combined_boxplot.png")
# Showing the plot
plt.show()
plt.clf()

# Displaying the distribution of long flights
long_flight = flight.coach_price[flight.hours == 8]
avg_long = round(np.mean(long_flight),2)
plt.hist(long_flight, bins = 15, color = "orange")
plt.title("Distribution of Flight Prices for Long Flights\n" + \
             "(Avg Coach Price: " + str(avg_long) + " €)")
plt.xlabel("Flight Price [€]")
plt.ylabel("Number of Flights")
plt.show()
plt.clf()

# Displaying the distribution of flights equal or shorter than 3 hours
short_flight = flight.coach_price[flight.hours <= 3]
avg_short = round(np.mean(short_flight),2)
plt.hist(short_flight, bins = 15, color = "orange")
plt.title("Distribution of Flight Prices for Flight length shorter than 3 hours\n" + \
             "(Avg Coach Price: " + str(avg_short) + " €)")
plt.xlabel("Flight Price [€]")
plt.ylabel("Number of Flights")
plt.show()
plt.clf()

# Displaying the distribution of delays
# There were some outliers on the graph so I had to reduce the delay time to 100 minutes
delays = flight.delay[flight.delay < 100]
plt.hist(delays, bins = 20, color = "orange")
plt.axis([0, 50, 0, 80000])
plt.title("Distribution of Flight Delays")
plt.xlabel("Delay in minutes")
plt.ylabel("Number of Flights")
plt.show()
plt.clf()

# Displaying the relationship between coach and first class prices
flight_sample = flight.sample(n=1000) # Getting a sample from the data
#plt.scatter(flight_sample.coach_price,flight_sample.firstclass_price, alpha=0.3, color = "orange")
sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight_sample, line_kws={'color': 'black'},  scatter_kws={'color': 'orange', 'alpha': 0.3}, lowess=True)
plt.title("Relationship Between Coach and First Class Prices")
plt.xlabel("Coach Price [€]")
plt.ylabel("First Class Price [€]")
plt.show()
plt.clf()

# Checking the price based on different features of the flight
sns.histplot(data=flight, x="coach_price", hue="inflight_meal")
plt.gca().legend_.set_title("Inflight Meal")
plt.xlabel("Coach Ticket Price (€)")
plt.ylabel("Number of Flights")
plt.title("Distribution of Basic Coach Prices by Inflight Meal Availability")
plt.show()
plt.clf()


sns.histplot(data=flight, x="coach_price", hue="inflight_entertainment")
plt.gca().legend_.set_title("Inflight Entertainment")
plt.xlabel("Coach Ticket Price (€)")
plt.ylabel("Number of Flights")
plt.title("Distribution of Basic Coach Prices by Inflight Entertainment Availability")
plt.show()
plt.clf()

sns.histplot(data=flight, x="coach_price", hue="inflight_wifi")
plt.gca().legend_.set_title("Inflight Wifi")
plt.xlabel("Coach Ticket Price (€)")
plt.ylabel("Number of Flights")
plt.title("Distribution of Basic Coach Prices by Inflight Wifi Availability")
plt.show()
plt.clf()

# Checking the relationship between coach and first class prices on weekends compared to weekdays
sample = flight.sample(n=2000) # Getting a sample from the data
sns.lmplot(x="coach_price", y="firstclass_price", data=sample, hue="weekend", fit_reg=False)
plt.title("Coach vs. First Class Prices: Weekends vs. Weekdays", fontsize=11, pad=15)
plt.xlabel("Coach Price [€]")
plt.ylabel("First Class Price [€]")
plt.show()
plt.clf()

# Daily comparison of night flight and daytime flight prices
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sns.boxplot(x="day_of_week", y="coach_price", hue="redeye", data=flight, order=day_order)
plt.xticks(rotation = 30)
plt.title("Daily comparison of night flight and daytime flight coach prices")
plt.ylabel("Coach Price [€]")
ax = plt.subplot()
ax.set_xticks(range(7))
ax.set_xticklabels(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
plt.show()
plt.clf()

# Comparison of flight distance and flight prices
flight_sample = flight.sample(n=3000) # Getting a sample from the data
sns.lmplot(x = "coach_price", y = "miles", data = flight_sample, line_kws={'color': 'black'},  scatter_kws={'color': 'orange', 'alpha': 0.3}, lowess=True)
plt.title("Relationship Between Coach Ticket Price and Flight Distance")
plt.xlabel("Coach Price [€]")
plt.ylabel("Miles")
plt.show()
plt.clf()