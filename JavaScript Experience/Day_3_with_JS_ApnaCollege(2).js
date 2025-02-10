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

let Shuja = new Doc("Plastic Surgeon")