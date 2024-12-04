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
filteredArray = anArray.filter((data) => (data<=3))
console.log ("Filtered Array =", filteredArray)

//or 

filteredArray = anArray.filter((data) => {
    if (data<=3){
    return data
    }
})

// 3. find
findedArray = anArray.find (data => data>60)
console.log ("Finded Array =", findedArray)