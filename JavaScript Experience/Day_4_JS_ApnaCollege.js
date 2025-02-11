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

