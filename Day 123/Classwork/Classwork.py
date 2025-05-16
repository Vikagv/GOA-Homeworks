#1) Create a list and add some names. Use the sorted() function to sort the names by the first letter of each name (alphabetically).

names = ["Vika","Mari","Nino","andria"]
print(sorted(names))

#Create a list of numbers and add the numbers in descending order, your goal will be to sort these numbers in ascending order.

Num = [3,5,1,9,5]
print(sorted(Num))[::-1]

#Create a list of numbers and add at least 10 numbers in ascending order, your goal will be to sort these numbers in descending order.

Num = [3,5,1,9,5,0,16,89,72,34,12,456,23]
print(sorted(Num))[::+1]