import fs from "fs/promises"

let a = await fs.readFile("SAR.txt")
// let b = await fs.writeFile("SAR3.txt", "\n\n\n\tThe promises are amazing, never knew about it")
let b = await fs.appendFile("SAR3.txt", "\n Nigga what?")

console.log(a.toString(), b);