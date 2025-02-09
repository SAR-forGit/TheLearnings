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
