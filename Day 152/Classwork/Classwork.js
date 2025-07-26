//Have the user enter a number and find out if the number is positive, negative, or equal to 0.

let user = Number (prompt("Enter a Number:"))

if (user === "0"){
    console.log ("Your Number is Equal to Zero")
}
else if (user < "0"){
    console.log ("Your number is positive")
}
else if (user > "0"){
    console.log ("Your number is Negative")
}