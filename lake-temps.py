# The temperature of a lake for one day is recorded every hour and data is stored
# in a one-dimensional array names TEMPDAY.

tempday = [12.4, 12.4, 12.3, 12.2, 12.1, 12.0, 11.9, 11.9, 11.8, 12.0, 12.1,
           12.9, 13.0, 13.1, 13.3, 13.5, 13.6, 13.4, 13.3, 13.2, 12.9, 12.8,
           12.3, 12.3 ]

print("Temperatures:",tempday)

# a) State the temperature of the lake at midday.
print("The temperature at midday was",tempday[11])

# b) Construct an algorithm that will calculate and output the average temperature

sum = 0
for t in range(len(tempday)):
    sum += tempday[t]

averageTemp = sum/len(tempday)
print("The average temperature was",format(averageTemp,'.1f'))

# c) Construct an algorithm to find and output the hours of the warmest and
#    coolest temperatures for the day.

warmestTemp = tempday[0]
coolestTemp = tempday[0]

warmestHour = 0
coolestHour = 0

for t in range(len(tempday)):
    if tempday[t] > warmestTemp:
        warmestTemp = tempday[t]
        warmestHour = t+1
    if tempday[t] < coolestTemp:
        coolestTemp = tempday[t]
        coolestHour = t+1

print("The warmest temperature was",warmestTemp,"occurring at hour:",warmestHour)
print("The coolest temperature was",coolestTemp,"occurring at hour:",coolestHour)
