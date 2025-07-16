#. 1) Create an initially empty list, then add 7 elements to this list, again to 
# this list the element standing on the third index and without changing the position 
# of the element standing on the second index,
#  you will add a new number to the fourth index and also to the fifth index.

Numbers = []
for i in range (1,8):
    Numbers.append(i)

two = Numbers[2]
three = Numbers[3]

Numbers[2] = three
Numbers[3] = two

Numbers.insert(4,9)

Numbers.remove(Numbers[0])
Numbers.remove(Numbers[-1])

print(Numbers)