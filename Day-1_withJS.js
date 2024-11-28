console.log ("hello world");

var nigg = "Hi, NIGG how are you";

console.log ("Normal:", nigg);
console.log ("Lower Case:", nigg.toLowerCase());
console.log ("Upper Case:", nigg.toUpperCase());

// Slice
console.log ("Slice some up:", nigg.slice(2,6)) //Does'nt go till 6 means will show up to 5 from 2 i.e (index, index-1)

var sliced_nigg = nigg.slice(3,8)
console.log ("Another way of slicing: ", sliced_nigg);

// Length
console.log ("Length of Variable Nigg:", nigg.length)