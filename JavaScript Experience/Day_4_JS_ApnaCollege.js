/////////////////////////////////////////////////////////////////////////// Callback //////////////////////////////////////////////////////////////////////////////////////////////

// Asynchronous: (code that will not execute in order)

console.log("one");
console.log("two");

setTimeout(() => {
    console.log("Hello");
}, 4000); // Set time of 4seconds

console.log("three");
console.log("four");

// Callback 

function sum(a, b){
    console.log(a + b);
}

function calculator(a, b, sumCallback){
    sumCallback(a, b);
}

calculator(1, 2, sum);

// Example

const hello = () => {
    console.log("Hello");
}

setTimeout(hello, 4000);

// Callback Hell: (Complex code which developer himself can't understand code is called Callback hell)
"Nested callbacks stacked below one another forming a pyramid structure is called pyramid of doom or Callback hell"

function getData(dataID, getNextID){
    setTimeout(() => {
        console.log("data", dataID);
        if(getNextID){
            getNextID();
        }
    }, 2000)
}

// // To get data 1 & data 2
// getData(1, () => {
//     getData(2);
// })

// // To get data 1, data 2 & data 3
// getData(1, () => {
//     getData(2, () => {
//         getData(3);
//     })
// })

// To get data 1, data 2, data 3 & data 4
getData(1, () => {
    console.log("Getting data 2.......");
    getData(2, () => {
        console.log("Getting data 3.......");
        getData(3, () => {
            console.log("Getting data 4.......");
            getData(4);
        });
    })
})

///////////////////////////////////////////////////////////////////////// Promises //////////////////////////////////////////////////////////////////////////////////////////////

let pinkyPromise = new Promise((resolve, reject) => {
    console.log("Hi there promise")
    resolve("It's resolved successfully");
    reject("Its' rejected and an error occured")
})

// Example 1

let lowercaseAlphabet = prompt ("Enter an alphabet in lowercase");

let CheckerOfCases = () => {
    return new Promise((resolve, reject) => {
        if (lowercaseAlphabet == lowercaseAlphabet.toLocaleLowerCase()){
            resolve();
        }
        else{
            reject("Bruh you wrote in capital");
        }
    })
}

let promise = CheckerOfCases()
promise.then(() => {
    console.log("Nigga");
})

promise.catch ((err) => {
    console.log("You are wrong dhoondu,", err); // here err is a parameter which was send in the real promise reject time
})

// Promise chain 

function getData(DataID) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("data", DataID);
            resolve("success");
        }, 2000)
    })
}

console.log("Getting data 1.......");
getData(1).then((result) => {
    console.log("Getting data 2.......");
    return getData(2)
})
.then((result) => {
    console.log("Getting data 3.......");
    return getData(3);
})
.then((result) => {
    console.log("Everything is executed successfully");
})

////////////////////////////////////////////////////////////////// Async - Await ///////////////////////////////////////////////////////////////////////////////////
function API(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("This is Weather API");
            resolve(200);
        }, 2000)
    })
}

async function getWeather() {
    await API();
    await API();
}

// Example 1:
function getchData(DataID) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("data", DataID);
            resolve("success");
        }, 2000)
    })
}

async function TheDataTeller(){
    console.log("Getting Data 1 using Async-Await...........");
    await getchData(1);
    console.log("Getting Data 2 using Async-Await...........");
    await getchData(2);
    console.log("Getting Data 3 using Async-Await...........");
    await getchData(3);
    console.log("Getting Data 4 using Async-Await...........");
    await getchData(4);
    console.log("Getting Data 5 using Async-Await...........");
    await getchData(5);
    console.log("Getting Data 6 using Async-Await...........");
    await getchData(6);
}

TheDataTeller();