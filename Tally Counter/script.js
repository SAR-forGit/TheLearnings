button = document.getElementById("TheButton");
text = document.getElementById("TheNumberText");

number=0;
targettedNumber = prompt("Give a target number");

TheButton.addEventListener("click", () => {
    number++;
    text.innerHTML = number;
    if (targettedNumber>0){
        if (number == targettedNumber){
        text.style.color = "red";
        }
    } 
});