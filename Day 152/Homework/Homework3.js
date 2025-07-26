//Enter a number for the user and if it matches your guessed number then alert them that they won. Otherwise, output to the console that they lost.

let userGuess = Number(Prompt("What do you think my number is?"))

if (userGuess === 12){
    alert("Congrats! You won")
}else{
    alert("Nope! You lost")
}