//Have the user enter a number and check it. If it matches your guessed number, then display an alert saying 
// 'Guess it's a good number'. If the entered value is greater than your guessed number, then display an alert saying 
// 'You entered a slightly larger number'. If the entered value is
//  less, then display an alert saying 'You entered a slightly smaller number'.

let Guess = Number(Prompt("Enter your guess: "))
if (Guess === 6){
    alert("You have entered thee correct number!")
}
else if(Guess > 6){
    alert("Your Guess is too big!")
}
else if(Guess < 6){
    alert("Your Guess is too Small!")
}