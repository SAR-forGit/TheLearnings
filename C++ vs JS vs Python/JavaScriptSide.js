// Username Verifier
givenName = prompt("Enter your name: ");

recomendedUsername  = "@" + givenName.toLowerCase() + givenName.length;

while(1){
    var userName = prompt(`we recomend you username: ${recomendedUsername} . Do you want to use it?`);

    var userAnswer = userName;

    if(userAnswer == "yes" || userAnswer == "YES" || userAnswer == "Y" || userAnswer == "y"){
        userName = recomendedUsername;
        break;
    }
    else if(userAnswer == "No" || userAnswer == "no" || userAnswer == "NO" || userAnswer == "n" || userAnswer == "N"){
        userName = prompt("Enter your desired username: ");
        userAnswer = prompt(`are you sure for the username ${"@"+userName}`);
        while(1 || userAnswer == "No" || userAnswer == "no" || userAnswer == "NO" || userAnswer == "n" || userAnswer == "N"){
            userName = prompt("Enter your desired username: ");
            userAnswer = prompt(`are you sure for the username ${"@"+userName}`);
            if(userAnswer == "yes" || userAnswer == "YES" || userAnswer == "Y" || userAnswer == "y") break;
            else continue;    
        }
        break;
    }
    else{
        userName = prompt(`Wrong Answer! Try Again.`);
        continue;
    }
}
console.log(`Hey ${givenName}, your username is set to ${userName}`);
