it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of it_companies:", len(it_companies))
it_companies.add('Twitter')   #Add twitter
print("After adding another item:",it_companies) 
it_companies.update({'Infosys','Capgemini','Wipro','TCS'})#Add multiple it_companies
print("After adding multiple items:",it_companies)
it_companies.remove('TCS')#Remove
print("After removing one company:",it_companies)
it_companies.discard('TCS')#Discard
print("After discarding company:",it_companies)#Discard doesn't raise any error if any item is not present in the set
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27} 
print("Join A and B:", A.union(B)) #Join A & B
print("Intersection of A and B:", A.intersection(B))#Intersection
print("Subset of A and B:", A.issubset(B))#Subset
print("Disjoint:", A.isdisjoint(B))#Disjoint
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Converting list to set:", set(age))#Convert list to set
print("Length of set:",len(set(age))) #Length of set
print("Length of list:",len(age))#Length of list
print("Symmetric diff:",A.symmetric_difference(B))#Symmetric diff- returns values which are not in common with other set
A.clear()#delete set 
print(A) 
B.clear()
print(B)
