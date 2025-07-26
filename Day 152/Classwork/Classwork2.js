//Have the user enter a password and name. If both the password and name match yours, then output an alert indicating that the 
// user has successfully logged in. Otherwise, the name or password is incorrect.

let Name = prompt("Enter the name")
let userpas = prompt("Enter The password")

if ( userpas === "Qwerty" && Name === "Vika"){
    console.log("Correct")
}
else {
    console.log("incorrect")
}