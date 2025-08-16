//The user enters a number, then check if this number is even and output to the console
//  "This number is even", otherwise output to the console "This number is odd"

let usernum = Number(prompt("Enter a Number:"))

if (usernum % 2 === 0){
 console.log("Your Number is even!")
}
else{
    console.log("Your number is odd")
}
