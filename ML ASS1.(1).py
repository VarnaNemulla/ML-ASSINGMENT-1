import statistics #Importing library called statistics which helps in calculating mathematical data
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()# Sorts age list in ascending order by default
print ("Sorted age:", ages) # Displays sorted values
# Minimum
print ("Min:", min(ages)) # Displays min value as we used min() method
# Maximum
print ("Max:", max(ages)) # Displays max value as we used max() method
# Adding again min and max values so we use append() method to insert values to the list
ages.append(min(ages)) 
ages.append(max(ages))
print ("Added min and max values again:",ages) #Displays the list again with new values
# Median (one middle item or two middle items divided by two, as we imported statistics library it calculates easily and provides the opt) 
mdn_age = statistics.median(ages)
print ("Median:", mdn_age)
# Average age
average= sum(ages)/len(ages)
print ("Avg = ", average)
# Range
rng=max(ages)-min(ages)
print ("Range = ", rng)
