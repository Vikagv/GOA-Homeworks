#. Think of a task and write the task code -- Task = create a list in which will have positive 
#. and negative number to filter, we need to return the two lists into just one
#. positive numbers in the other negative numbers

Numbers = [10 ,-1, -193 , 42378, 454 , -235]
Positive_numbers = []
Negative_numbers = []

for i in range (len(Numbers)):
    if Numbers [i] == 0 :
        continue
    elif Numbers [i] < 0 :
       Negative_numbers.append(Numbers[i]) 
    else :
       Positive_numbers.append(Numbers[i])   

print("These are Negative numbers", Negative_numbers)
print("These are Positive numbers", Positive_numbers)