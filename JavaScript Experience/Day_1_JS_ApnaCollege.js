//////////////////////////////////////////////// String Concatenation Apna College question ///////////////////////////////////////////////////////
let givenName = prompt("Enter your name: ");

recommendedUsername = "@" + givenName + givenName.length;

while(1){
    var userName = prompt(`we recommend you username: ${recommendedUsername}. Do you want to use it?`);
    let userAnswer = userName.toLowerCase()

    if(userAnswer == "yes" || userAnswer == "Y" || userAnswer == "y"){
        userName = recommendedUsername;
        break;
    }
    else if(userAnswer == "no" || userAnswer == "N" || userAnswer == "n"){
            userName = prompt("Enter your desired username:");
            userName = "@".concat(userName)
            break;
    }
    else{
        alert("Invalid Answer..... please retry");
        continue;
    }
}
console.log(`Name = ${givenName}\nUser Name = ${userName}`);

// Q: For a given array with marks of students -> [85, 97, 44, 37, 76, 60], Find the average marks of the entire class

let marks = [85, 97, 44, 37, 76, 60];
let total = 0;

for (let mark of marks){
    total = total + mark;
}    

let average = total / marks.length;

console.log(`Average marks of the entire class is: ${average}`);

// Q: For a given array with price of 5 items -> [250, 645, 300, 900, 50], all items has an offer of 10% off on them. 
// Change the array to store the final price after applying offer 

let items = [250, 645, 300, 900, 50], i = 0;

//way 1
for (let val of items){
    let offer = val / 10;
    items[i] = items[i] - offer;
    console.log(items[i]);
    i++;
}    

//way 2
for(let i = 0; i<items.length; i++){
    let offer = items[i] / 10;
    items[i] -= offer;
}    

console.log(items);

///////////////////////////////////////////////////// Arrow Function //////////////////////////////////////////////////////
//Full-size real function:
function the_multiplier(a, b){
    console.log(a*b);
}

//Arrow Function:
let the_summer = (a, b) => {
    console.log(a+b);
}

the_summer(5, 8);
the_multiplier(5, 8);

//Another example of arrow Function
let hello_printer = () => console.log("Hello");

hello_printer();
hello_printer();
hello_printer();
hello_printer();

//Q: Create a function using the "function" keyword that takes string as an argument & returns the number of vowels in the string

function vowelCounter(given){
    let vowels = 0;

    str = given.toLowerCase();

    for (let i of str){
        if(i === "a" || i === "e" || i === "i" || i === "o" || i === "u"){
            vowels++;
        }
    } 
    console.log(`The number of vowels in the word ${given} are ${vowels}`);
}

givenWord = prompt("Enter a word: ");
vowelCounter(givenWord);

///////////////////////////////////////////////////////// For Each Function ////////////////////////////////////////////////////////////

let anArray = [69, 77, 45, 100, 102, 1001];

anArray.forEach (
    function printVal(val){
        console.log(val);
    }
);

let anArray3 = ["BrainRot", "Skibidi", "Sigma"];

anArray3.forEach ((val) => {
        console.log(val.toUpperCase());
    }
);

//Example 1:
let anArray2 = [2, 4, 6, 8];
anArray2.forEach(
    function powerer(val){
        console.log (val*val)
    }
);

//Example 2:
let anArray4 = [1, 2, 4, 6, 8];

let Halfer = (num) => {
    console.log(`Half of the number ${num} is ${num / 2}`);
};

anArray4.forEach(Halfer)

/////////////////////////////////////////////////////////// Map Function //////////////////////////////////////////////////////////////
//Example 1
let anArray5 = [5, 6, 8];

anArray5.map ((val) => {
    console.log(val);
});

//Example 2:
let anArray6 = [5, 6, 8];

let newArray = anArray6.map ((val) => {
    return val;
});

console.log(newArray);

// Example 3:
let anArray7 = [47, 4, 5, 5, 2, 1];

let Squarer = anArray7.map ((val) =>{
    return val*val;
})

console.log(Squarer);

// Q: For a given array with marks of students -> [85, 97, 44, 37, 76, 60], Find the average marks of the entire class
let marks1 = [97, 85, 49, 65], total1 = 0;

let Averager = marks1.map ((mark) => {
    total = total + mark;
});

let average1 = total / marks1.length;

console.log (`average of class is ${average1}`);

/////////////////////////////////////////////////////////// Filter Function //////////////////////////////////////////////////////////////
let anArray8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];

let evener = anArray8.filter ((val) => {
    return val % 2 === 0;
})

console.log(`Even numbers of the given array is ${evener}`);

// Example:
let anArray9 = [8, 90, 26, 5, 3, 47, 69, 56, 46];

let odder = anArray9.filter ((num) => {
    return num % 2 !== 0;
})

console.log(`Odd number for the given array is ${odder}`);

/////////////////////////////////////////////////////////// Reduce Method //////////////////////////////////////////////////////////////
let anArray10 = [1, 2, 3, 4, 5];

let adder = anArray10.reduce ((result, current) => {
    return result + current;
})

console.log (adder);

// Example 2:
let anArray11 = [69, 77, 58, 10, 12, 4, 2, 12, 16, 20, 36, 46, 58]

let biggest = anArray11.reduce ((result, current) => {
    return result > current ? result : current;
})

console.log(biggest);

// Q: We are given an array of marks of students. Filter out of the marks of students that scored 90+.

let studentMarks = [96, 52, 75, 27, 34, 99, 88, 98, 89];

let toppers = studentMarks.filter ((val) => {
    return val > 90;
})

console.log (toppers)

// Q: Take a number n as input from user. Create an array of numbers from 1 to n.
//  Use the reduce method to calculate sum of all numbers in the array
//  Use the reduce method to calculate product of all numbers in the array

let givenArray = [];

let givenNumber = 0;

while(1){
    if (givenNumber !== "Finish"){
        givenNumber = prompt('Enter number (1-n) (or Enter "Finish" to stop): ');
        if (isNaN(givenNumber) == true && givenNumber !== "Finish"){
            continue;
        }
        else{
        givenArray.push(givenNumber);
        }
    }
    
    else if (givenNumber == "Finish"){
        let temp = givenArray.pop();
        break;
    }
}



let SumOfArray = givenArray.reduce ((result, current) => {
    return Number(result) + Number(current);
})

let ProductOfArray = givenArray.reduce ((result, current) => {
    return current * result;
})

console.log(`Your given array is ${givenArray}`)
console.log (`Sum of your given array is ${SumOfArray}`);
console.log (`Product of your given array is ${ProductOfArray}`);