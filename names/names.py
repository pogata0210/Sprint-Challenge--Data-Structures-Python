import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""


names_1.sort()
names_2.sort()

duplicates = [] #creat a list

i = 0  #set initial value
j = 0   #set initial value

while i < len(names_1) and j < len(names_2): #while i is smaller than name_1 and j is smaller than name_2 do if 
    if names_1[i] == names_2[j]: #check if varieble is == to eachother.
        duplicates.append(names_1[i]) #append
        i += 1 #keep incrementing
        j += 1 #keep incrementing
    elif names_1[i] < names_2[j]:
        i += 1 #constant so run time desn't matter, if there are not == moveon
    else:
        j += 1        #same here for the run time, moveon
  
        
        




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

