# question : the current population of a town is 10000. The populatuon of the town is increasing at the rate of 10% per year . 
You have to write a program to find out the population at the end of the year of the last 10 years.
current_population = 10000
for i in range(10,0,-1):
    print(i, current_population)
    current_population = current_population/1.1

