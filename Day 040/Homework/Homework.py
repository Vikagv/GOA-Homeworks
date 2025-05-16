#. "Let the user enter 10 numbers then add them to a list, filter this list into two parts even and odd and 
#. add even to a new list odd separately"

numbers = []
Odd_numbers = []
Eaven_numbers = []

for i in range(10) :
   user_input = int(input("enter any number:"))
numbers.append(user_input)

for i in range(len(numbers)):
   if numbers[i] % 2 == 0:
      Eaven_numbers.append(numbers)
else:
       Odd_numbers.append(numbers)

print("These numbers are Odd",Odd_numbers)
print("These numbers are Eaven",Eaven_numbers)
