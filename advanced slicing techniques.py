# task 1
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print("Temperatures for the second week:", second_week_temperatures)
# task 2
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
above_100_temperatures = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", above_100_temperatures)



# task 1 and 2
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
above_100_temperatures = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100\n", above_100_temperatures,"\nTemperatures for the second week\n", second_week_temperatures)
