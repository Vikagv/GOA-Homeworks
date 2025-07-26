//Enter a score for the user up to 100. If the entered score is greater than 95, display 'A' in the alert, if it is greater than
//  80 and less than 95 then B, between 75-80 'C', between 70-75 "D". If it is less than 70 then F.

let usergrade = Number(Prompt("Enter Your grade from 1-100"))

if (usergrade >= 95){
    alert ("Your Grade is A")
}
else if (usergrade >80<95){
    alert ("Your Grade is B")
}
else if (usergrade >75<80){
    alert ("Your Grade is C")
}
else if (usergrade >70<75){
    alert ("Your Grade is D")
}else{
    alert ("Your Grade is F")
}