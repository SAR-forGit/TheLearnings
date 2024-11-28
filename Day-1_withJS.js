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

// Replace
console.log ("Replacing nigg with aura -1000:", nigg.replace("NIGG", "Aura -1000"))
console.log ("Still nigg is:", nigg)
console.log ("New length of nigg:", nigg.length) //length doesn't change as it is only changed for one line it is'nt replaced in the variable

// Include
console.log (nigg.includes("NIGG")) //if it's including then it wil print true
console.log (nigg.includes("NIGGA")) //If it's not including it will print false
console.log (nigg.includes("Nigg")) //it's also case sensitive

// ______________________________________________________________________________________________________________________________________________________________//

// parse (to change datatype)
var nigg = "6969.1010" //is string
console.log (nigg, "&", typeof(nigg)) //still a string
console.log (parseInt(nigg), "&", typeof(parseInt(nigg))) //changed to int or number
console.log (parseFloat(nigg), "&", typeof(parseFloat(nigg))) //changed to float

var nigg = "nigga6969" 
console.log (parseInt(nigg)) //Output: NaN (not a nummber)
var nigg = "6969nigga" 
console.log (parseInt(nigg)) //Output: 6969 and characters will be ignored
var nigg = "69nigga69" 
console.log (parseInt(nigg)) //Output: 6969 and characters will be ignored

// ______________________________________________________________________________________________________________________________________________________________//

// tostring
var nigg = 1010;
console.log ("Number nigg:", nigg)
console.log ("string nigg:", nigg.toString())
console.log ("Locale string nigg:", nigg.toLocaleString())

// ______________________________________________________________________________________________________________________________________________________________//

// Split operator
var nigg = "Good Morning nigga"
console.log (nigg.split(' ')) //it will spli this string from wherever it find space and make it an array
console.log (nigg.split('i')) //it will spli this string from wherever it find 'i' and make it an array
// ______________________________________________________________________________________________________________________________________________________________//

// Obj (dict from python)
var nigg = {
    nigga1 : "aura -1000",
    nigga2 : 5050,
    nigga3 : "GAY"
}

console.log (nigg)
console.log (nigg.nigga1)
console.log (nigg.nigga2)
console.log (nigg.nigga3)
console.log (Object.keys(nigg))
console.log (Object.values(nigg))

nigg.nigger = "kullu manali"

console.log (nigg)
// ______________________________________________________________________________________________________________________________________________________________//
