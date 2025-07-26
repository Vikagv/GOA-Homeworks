//მომხმარებელს შემოატანინეთ ორი რიცხვი და ოპერაცია რომელიც უნდა რომ შეასრულოს. და გამოიტანეთ შედეგი alert-ით.
//( კალკულატორია ) 

let num1 =Number (prompt("Enter your first number"))
let num2 =Number (prompt("Enter your Second number"))
let operation = prompt (" Choose opperation */-+")
let result 

if ( operation === "+"){
    result = num1 + num2
}
else if ( operation === "-"){
    result = num1 - num2
}
else if ( operation === "/"){
    result = num1 / num2
}

else if ( operation === "*"){
    result = num1 * num2
}

else {
    result = "Wrong opperation"
}

alert(result)