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

var age = 19

age > 18 ? console.log ("You're eligible to vote!") : console.log ('You are not eligible to vote!')

age > 18 
    ? console.log ('You are eligible to vote!') 
    : console.log ('You are not eligible to vote!')

// 1.Function 

function hello_printer(){
    console.log ('Hello')
}

hello_printer()

// 2. Anonymous Function || Function expression

hello_printer = function(){                                                           // Another way of declaring function or anonymous function
    console.log ("Hello printer is saying hello")
}

hello_printer()

//Another example of function:

var obj1 = {
    name : "TVS",
    bikeName : function(){                                                           // Another way of declaring function
        console.log ('Hello, this is bike name')
    }
}

console.log (obj1.name)
obj1.bikeName()

//Function addder

function adder(a, b){
    return a+b
}

chint = adder(2, 5)

console.log (chint)


// 3. Hello Function

adder = (a, b) => {
    return a+b
}

console.log (adder(10, 12))

