//Have the user enter a number. If the number is less than 10, display an alert 
// message saying “Enter a number greater than 10”. Otherwise, print all numbers up to and includin
//  the number entered by the user. (if/else will be needed)

let usernum = Number(prompt("Enter a Number!"))

if(usernum < 10){
    alert=("Enter a number greater than 10")
}

for(let sum = 0; sum < usernum; sum ++){
    console.log(sum)
}
