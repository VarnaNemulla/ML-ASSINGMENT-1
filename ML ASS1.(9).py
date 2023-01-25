
L1=[int(num) for num in input().split(" ")]  #Creating a list(L1) for weights(lbs) of N students
W_kg=[]              #Creating another list called W_kg
for i in L1:   #Using for loop to iterate the values and appending the list
  W_kg.append(round(i/2.205,2))
print ("Values are:",W_kg)#Displaying the values in kgs after conversion
