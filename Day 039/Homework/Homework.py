#. Day 39:
#. 1) Bring the user ten numbers, add these 
#. numbers to the list, from this list sort, sort these numbers into two 
#. groups, numbers that are greater than 100 and 
#. numbers that are less than 100.

Less_then_100 = []
More_then_100 = []

for i in range (1,11) :
    Users_number = int(input("Please Enter any number:"))

if Users_number < 100 :
    Less_then_100 = (Users_number)

elif Users_number > 100 :
    More_then_100 = (Users_number)

print (Less_then_100)
print (More_then_100)