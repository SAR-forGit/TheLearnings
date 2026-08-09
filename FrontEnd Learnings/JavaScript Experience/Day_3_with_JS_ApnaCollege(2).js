///////////////////////////////////////////////////////////////////// Classes ///////////////////////////////////////////////////////////////////////////

// Prototype:
const employee = {
    calcTax() {
        console.log("The tax is 10%");
    }
}

const KaranArjun = {
    salary : 50000,
    calcTax() {
        console.log("The tax is 20% from Karan Arjun method");
    }
}

KaranArjun__proto__ = employee;

// Class

class ToyotaCar {
    start() {
        console.log("car start with VROOOOOOOOOOOM VROOOOOOOOOOOOOOOOOM"); // object start
    }

    stop(){
        console.log("car stops with SCREEEEEEECH") // object stop
    }

    setBrand(brand){
        this.brandname = brand; // here this is like self from Python
    }
}

let Fortuner = new ToyotaCar(); // here Fortuner inherits from ToyotaCar class
Fortuner.setBrand("fortuner");

let Lexus = new ToyotaCar();
Lexus.setBrand("Sub brand")

// Constructor:
class GeneralMotors {
    constructor(brand, bodyType){
        console.log("From General Motors");

        this.brandName = brand;
        this.Body = bodyType;
    }

}

let Tahoe = new GeneralMotors("Chevrolet", "SUV");
console.log(`About Tahoe: \n`, Tahoe);

let Celestiq = new GeneralMotors("Cadillac", "Sedan");
console.log("About Cadillac Celestiq: \n", Celestiq);


// Inheritance

class Person{
    eat(){
        console.log("Eating Nom Nom");
    }

    sleep(){
        console.log("Sleeping zzzzz");
    }
}

class Engineer extends Person{
    develop(){
        console.log("Github and chill");
    }
}

let SAR = new Engineer();
console.log(SAR.develop())
console.log(SAR.eat())
console.log(SAR.sleep())


// super();

class HomoSepion{
    constructor(){
        console.log("hi there this Parent constructor");
    }
}

class Doc extends HomoSepion{
    constructor(branch){
        super(); // To invoke parent class
        this.branch = branch;
        console.log("This is child constructor");
        console.log('doc is from branch:', branch);
    }

    Surgery() {
        console.log("This is child class");
    }

}

let Shuja = new Doc("Plastic Surgeon");

// super(argument);

class person{
    constructor(name) {
        this.specie = "Homo Sepians";
        this.name = name;
    }

    eat() {
        console.log("eat");
    }
}

class engineer extends person{
    constructor(name){
        super(name);
    }

    work() {
        super.eat();
        console.log("Maintain 75% attendance");
    }
}

let enggObj = new engineer("Rancho");


/////////////////////////////////////////////////////////////////////////// Practice Question: //////////////////////////////////////////////////////////////////////////////////

// Q: You're creating a website for your college. Create a class user with 2 properties, name & email. It also has a method called viewData() that allow user to view data.

class Student{
    constructor(name, email){
        this.name = name;
        this.email = email;
    }
    
    viewData(){
        console.log("View data");
    }
}

let student1 = new Student("Md Rafi", "MainePuchaChandSe@gmail.com");
console.log(`${student1.name} has won the singing competition`);

let student2 = new Student("KK", "SajdeKiyeHainLakhoDuaeMangi@gmail.com");
console.log ("details of student 2:", student2);

// Q: Create a new class called Admin which inherits from user. Add new method called editData to Admin that allows to edit website data

let Data = "Some Secret Data"

class user{
    constructor(name, branch){
        this.name = name;
        this.branch = branch;
    }
}

class Admin extends user{
    constructor(name, branch){
        super(name, branch);
    }
    
    editData(){
        Data = "the new data";
    }
}

let admin1 = new Admin("Poor", "IT");

////////////////////////////////////////////////////////////////////////// Error handling: ///////////////////////////////////////////////////////////////////////////////////////

// try-catch

let a = 5, b = 10;

console.log(a+b);
console.log(a+b);
console.log(a+b);
console.log(a+b);
console.log(a+b);

try{
    console.log(a+c); // if this got error it will not execute 
}

catch(err){
    console.log(err); // it will pass through the catch method and here we're console.log it
}

console.log(a+b);
console.log(a+b);
console.log(a+b);
console.log(a+b);
console.log(a+b);
console.log(a+b);
console.log(a+b);
console.log(a+b);