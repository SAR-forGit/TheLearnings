//3. Arrow function
var sum = (a,b) => console.log (a+b) //Can write in a single line if there is one command

//or

var sum = (a, b) => {
    // console.log (a+b) // multiple line of codes so can use curly brackets
    return a+b
}

var a =10, b = 20

console.log ("a = ", a,", b = ", b, " & a+b = ", sum (a, b))

//////////////////////////////////////////////// Arrow methods / Methodoloy ///////////////////////////////////////////////////////
var anArray = [50, 60, 70, 80, 90]
console.log ("Original Array =", anArray)

// 1. map
var mappedArray = anArray.map((data) => (data+2))
console.log ("Mapped array (i.e +2 for each element) =", mappedArray)

// 2. filter
var anArray = [50, 60, 70, 80, 90]

filteredArray = anArray.filter((data) => (data<=3))
console.log ("Filtered Array =", filteredArray)

//or 

filteredArray = anArray.filter((data) => {
    if (data<=3){
    return data
    }
})

// 3. find
var anArray = [50, 60, 70, 80, 90]

findedArray = anArray.find (data => data>60)
console.log ("Finded Array =", findedArray)

//  4. reduce
var anArray = [50, 60, 70, 80, 90]

var reducedArray = anArray.reduce ((accumalation, cuurentValue) => {
    return accumalation + cuurentValue;
}, 0)

console.log ("Reduced Array =", reducedArray)

// Example of using reduce

console.log ("_________________________________Flipkart Cart________________________________________")

FlipkartCart = [
    {
        price : 50000, 
        quantity : 1
    },
    {
        price : 300000,
        quantity : 1
    },
    {
        price : 20,
        quantity : 3
    },
    {
        price : 70,
        quantity : 5
    }
]

GrandTotal = FlipkartCart.reduce ((a, b) => {
    return a + b.price * b.quantity
}, 0)



console.log  ("PS5 =", Object.values(FlipkartCart)[0])
console.log  ("Sony A95L OLED 55' =", Object.values(FlipkartCart)[1])
console.log  ("Halke Fulke Chips =", Object.values(FlipkartCart)[2])
console.log  ("TV Screw =", Object.values(FlipkartCart)[3])

console.log ("_______________________________________________________________________________________")
console.log  ("Your Grand Total is =", GrandTotal)