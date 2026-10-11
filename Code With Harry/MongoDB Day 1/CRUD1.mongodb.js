use("CrudDBVery1")

db.createCollection("courses");

// CREATE
db.courses.insertOne({
    Name: 'SAR',
    age: 22,
    branch: "CSE",
    Section: "B"
})

db.courses.insertMany([[
  {
    name: "John",
    age: 25,
    email: "john@example.com"
  },
  {
    name: "Alice",
    age: 30,
    email: "alice@example.com"
  },
  {
    name: "Bob",
    age: 28,
    email: "bob@example.com"
  }
]])

// READ
let freshSkin = db.courses.find({age:22})
console.log(freshSkin);

// UPDATE
db.courses.update({age: 22}, {$set:{age:23}})

// DELETE
db.courses.deleteOne({age:28});
// db.courses.deleteMany({age: 28});