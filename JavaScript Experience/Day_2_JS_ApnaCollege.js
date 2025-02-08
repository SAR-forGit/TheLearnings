// DOM - Document Object Manipulation

//////////////////////////////////////////////////////// Get Element by: ///////////////////////////////////////////////////////////////////
let first_para = document.getElementById("ManId");
// console.dir(first_para);
console.log(first_para);

let second_para = document.getElementsByClassName("ManClass")
console.log(second_para);

let all_paras = document.getElementsByTagName("p");
console.log(all_paras);

//////////////////////////////////////////////////////// Query Selectors: //////////////////////////////////////////////////////////////////

let first_para_qs = document.querySelector("#ManId")
console.log(first_para_qs);

let second_para_qs = document.querySelector(".ManClass")
console.log(second_para_qs);

let all_para_qs = document.querySelectorAll("p");
console.log(all_para_qs)

//////////////////////////////////////////////////////// Practice: /////////////////////////////////////////////////////////////////////

// Q" Create a h2 heading element with text - "Hello JavaScript". Append from "from Apna College Students" to this text using JS 
let hello_sayer = document.getElementById("Hello_js");
console.log(hello_sayer);
console.log(typeof hello_sayer);

let text_inside = hello_sayer.innerText + " from Apna College Students";
console.log (text_inside);

// Q: Create 3 divs with common class name "box". Access them & add unique text to each of them

// Way 1
let box = document.getElementsByClassName("box");
console.log(box[0].innerText + " is of Niggas");
console.log(box[1].innerText + " is of Brainrot");
console.log(box[2].innerText + " is of Sigma");

// Way 2:
let boxes = document.querySelectorAll(".box"), idx = 0, genz = ['Niggas', "Brainrot", "Sigma"];

for (box of boxes){
    console.log (`${box.innerText} is of ${genz[idx]}`);
    idx++;
}

/////////////////////////////////////////////////////////// Styles: ///////////////////////////////////////////////////////////////////////

let Brainrot_box = document.getElementById("brainrot_box");

Brainrot_box.style.backgroundColor = "green";
Brainrot_box.style.border = "black 4px solid";
Brainrot_box.style.color = "white";

// Example 1:
let kk_image = document.getElementById("KK_Image");
kk_image.style.visibility = "hidden"

givenAnswer = prompt("Who is KK?").toLowerCase();

if(givenAnswer == "singer"){
    kk_image.style.visibility = "visible"
}
else kk_image.style.visibility = "hidden"
