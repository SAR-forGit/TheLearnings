console.log ("Hi there Day-2")

// Operators

var num1=2, num2=5

console.log ("Num1: ", num1, "\nNum2: ", num2)
console.log ("addition:", num1 + num2)
console.log ("subtraction:", num1 - num2)
console.log ("multiplication:", num1 * num2)
console.log ("division:", num1 / num2)
console.log ("Remainder:", num1 % num2)

// Comparision Operator

var num1=69, num2="69"

console.log (num1 == num2) //Output will be true 
console.log (num1 === num2) //Output will be false beacause it will also check the datatype and here num1 is number and num2 is string

// not operator

var bhool = 0 //eitehr write 'true' fully or 'false' fully or 1 or 0 
console.log ("!bhool =", !bhool)

// If-else

age = 17

if (age>18){
    console.log ("You're eligible to vote!")
}
else {
    console.log ('You are not eligible to vote!')
}

// Conditional Operator || Ternary operator

age = 19

age > 18 ? console.log ("You're eligible to vote!") : console.log ('You are not eligible to vote!')
