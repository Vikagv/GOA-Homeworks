#. 1) We are given a list full of numbers, we need to create a new list and to this list we need to add the
#. elements of the existing list in a rotated form, reverse

Normal_numbers = [1,2,3,4,5,6,7,8,9,10]
Upside_down_list = []

for i in range (len(Normal_numbers)):
    Upside_down_list.append(Normal_numbers[-i-1])

print (Upside_down_list)