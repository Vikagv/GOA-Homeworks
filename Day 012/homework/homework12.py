user_test_score =int (input("your test score is:  "))

if user_test_score < 90 :
    print ("you will be funded for your studies")
if user_test_score < 80 :
    print("you will be funded 1500 GEL")
if user_test_score < 70 :
    print("you will be funded 500 GEL")
if user_test_score < 40 :
    print ("your study process will not be financed")

#second homework
    
students_grade_in_test = int (input("your grade on the test is:  "))
if students_grade_in_test < 10 :
    print ("the teacher will praise the student with the parent")
if students_grade_in_test < 8 or 9 :
    print ("the teacher should give a small note to the parent. ") 
if students_grade_in_test < 5 :
    print (" the teacher will expel the student from the school.")