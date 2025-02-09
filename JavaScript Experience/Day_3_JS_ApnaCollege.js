//////////////////////////////////////////////////////////// Events: ///////////////////////////////////////////////////////////////////

// onClick
let TheButton = document.getElementById("TheButton")

TheButton.onclick = () => {
    console.log("This button is clicked");
}

// onmouseover:

let chameleon = document.querySelector("#NiggaButton");

chameleon.onmouseover = () => {
    console.log("This will not execute")
}

chameleon.onmouseover = () => {
    console.log ("This will execute")
}

////////////////////////////////////////////////////////// Event Listener: //////////////////////////////////////////////////////////////////

// addEventListener:

let abuser = document.querySelector("#asfbutton");

abuser.addEventListener("click", () => {
    console.log ("Hey fuck you")
    console.log("joke apart, this is from function 1 and will also get executed")
})

let function2Sayer = () => {
    console.log("And this is from function 2 which wil also will execute")
}

abuser.addEventListener ("click", function2Sayer)

// Also accessing here event object
abuser.addEventListener ("click", (evt) => {
    console.log(evt);
    console.log(evt.target);
    console.log(evt.type);
    console.log("event object can also be acessed from event handler")
})

// removeEventListener:
abuser.removeEventListener ("click", function2Sayer)

//////////////////////////////////////////////////////// Practice Question: //////////////////////////////////////////////////////////////

// Q: Create a toggle button that changes the screen to dark-mode when clicked & light-mode when clicked again.

// Way 1:
// let DaynNight = document.querySelector("#DaynNight"), currentMode = "light";

// DaynNight.onclick = () => {
//     if (currentMode === "light"){
//         currentMode = "dark";
//         document.querySelector("body").style.backgroundColor = "black";
//         console.log(`Current Mode = ${currentMode}`);
//     }
//     else{
//         currentMode = "light";
//         document.querySelector("body").style.backgroundColor = "white";
//         console.log(`Current Mode = ${currentMode}`);
//     }
// }

// Way 2:
let DaynNight = document.querySelector("#DaynNight"), currentMode = "light", bodee = document.querySelector("body");

DaynNight.addEventListener("click", () => {
    if (currentMode === "light"){
        bodee.classList.add("dark");
        bodee.classList.remove("light")
        currentMode = "dark";
        console.log (`Current mode : ${currentMode}`);
    }
    else{
        bodee.classList.add("light");
        bodee.classList.remove("dark")
        currentMode = "light";
        console.log (`Current mode : ${currentMode}`);
    }
})