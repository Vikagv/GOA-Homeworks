 //The user enters a number, your task is to check if the user enters a number less than 10 and print "LESS THAN 10" 
 // to the console, if the user enters a number greater than 10 and print MORE THAN 10 to the console,
 //  and if the user enters a number greater than 10 and print EQUAL TO 10 to the console.


 let usernum = Number(prompt("Enter a number"))

 if(usernum < 10){
    console.log("This Number is less than ten")
 }
  if(usernum == 10){
    console.log("This Number is equal to ten")
 }
 
 else{
    console.log("This Number is more than ten")
 }