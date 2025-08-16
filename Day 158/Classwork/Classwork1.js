//Let the user enter a number, loop through the for loop from 1 to the number entered by the user and output all even numbers.

let usernum = Number(prompt("Enter any Number:"))

for(let sum = 0; sum < usernum; sum ++){
    if (sum % 2 === 0){
        console.log (sum)
    }
}