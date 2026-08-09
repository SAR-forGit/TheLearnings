console.log("Promises");

prom = new Promise((resolve, reject) => {
    random = Math.floor((1 + Math.random() * 9));
    if(random<5) reject("the nigga is not loading");
    else setTimeout(() => {
        resolve("Maney follows brotha, maney follows");
    }, 2000); 
})

prom.then((random) => {
    console.log(random);
}).catch((ifError) => {
    console.log(ifError);
})
