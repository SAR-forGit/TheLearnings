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

//////////////////////////////////////////////// String Concatenation Apna College question ///////////////////////////////////////////////////////
let givenName = prompt("Enter your name: ");

recommendedUsername = "@" + givenName + givenName.length;

while(1){
    var userName = prompt(`we recommend you username: ${recommendedUsername}. Do you want to use it?`);
    let userAnswer = userName.toLowerCase()

    if(userAnswer == "yes"){
        userName = recommendedUsername;
        break;
    }
    else if(userAnswer == "no"){
            userName = prompt("Enter your desired username:");
            userName = "@".concat(userName)
            break;
    }
    else{
        prompt("Invalid Answer..... please retry");
        continue;
    }
}
console.log(`Name = ${givenName}\nUser Name = ${userName}`);

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