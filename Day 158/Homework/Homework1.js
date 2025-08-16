//The user enters two numbers, your task is to loop through the for loop from the first number 
// entered by the user to the second number entered by the user and output each number in this range

let usernum1 = Number(prompt("Enter first Number:"))
let usernum2 = Number(prompt("Enter second Number:"))

let sum = usernum1 + usernum2

for(let i = 1; i < sum; i ++){
    console.log(i)
}