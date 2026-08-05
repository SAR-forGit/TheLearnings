box = document.querySelector(".BoxesSection").children
randomNumber = () => Math.floor(0 + Math.random() * 255);
randomColor = () =>{
    value1= randomNumber();
    value2= randomNumber();
    value3= randomNumber();
    return (`rgb(${value1}, ${value2}, ${value3})`)
    // return (`rgb(${(Math.floor(0 + Math.random() * 255))}, ${(Math.floor(0 + Math.random() * 255))}, ${(Math.floor(0 + Math.random() * 255))})`)
} 

console.log(box)
console.log(randomColor);

for(i = 0; i<box.length; i++){
    console.log(box[i]);
    box[i].style.backgroundColor = randomColor();
}
