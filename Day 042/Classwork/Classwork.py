#. 1) შევქმნათ სია რომელშიც გვექნება რომელშიც გვექნება დადებითი და უარყოფითი რიცხვები. გავფილტროთ, უნდა დავაბრუნოთ ორი სია ერთში მხოლოდ 
#. დადებითი რიცხვები მეორეში მხოლოდ უარყოფითი რიცხვები.

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