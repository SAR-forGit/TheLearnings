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

