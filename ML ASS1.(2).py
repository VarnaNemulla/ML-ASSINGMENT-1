dog = {'name':'Max','color':'white','breed':'Bulldog','legs':'4','age':'1.5'}# Dog dictionary is created with given key and values
print ("Dog Dictionary Created:",dog)

student = {'first_name':'Varna','last_name':'Nemulla','Gender':'Female','age':'22','marital_status':'single',
'skills':'dancer','Country':'India','City':'Hyderabad','Address':'2-89'}# Student dictionary is created with given key and values

print ("Student Dictionary Created:",student) 

skills = {'writer':'1','guitar player':'2','Bookreader':'3'}# Create another dictionary for skills

print ("Skills Dictionary Created:",skills)# Find the length of student dictionary

print ("Length of student:", len(student))  # Check the datatype of skills

print ("Datatype of skills:",type(skills)) 


print ("Values of skills:",skills.values()) # Get values of skills dictionary

skills['singer'] = 4                    # Add one item to skills
print ("New skill added:",skills)

print ("Dog keys:",dog.keys()) # Get dog and student key and values
print ("Student values:",student.values())
