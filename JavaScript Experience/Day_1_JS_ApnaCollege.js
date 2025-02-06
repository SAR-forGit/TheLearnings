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
