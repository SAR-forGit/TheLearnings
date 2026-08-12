fs = require("fs")
// console.log(fs)

console.log("starting")
// fs.writeFileSync("SAR.txt", "Hey there")  // this makes file in workspace/main directory

fs.writeFile("SAR2.txt", "Hey there nigger", () => { // this makes file in workspace/main directory and writes in it
    console.log("Done"); 
    fs.readFile("SAR2.txt", (error, data) => {
        console.log(error, data.toString());
    })
})

// fs.appendFile("SAR2.txt", " you are nigger! not me." (e, d) => {
//     console.log(d) // idk why its not running 
// })

console.log("ending");