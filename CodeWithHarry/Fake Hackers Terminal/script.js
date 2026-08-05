text = document.querySelector("#terminal").children;

randomDelay = (dataID) => {
    return new Promise((resolve, reject) => {
        timeOut = Math.floor(1 + 6*Math.random());
        setTimeout(() => {
            // resolve(text(dataID));
            text.innerHTML = text.innerHTML + text[dataID];
            resolve(console.log(`delay of ${timeOut}`))
        },timeOut *1000)
    })
}

(async function(){
    await randomDelay(0);
    await randomDelay(1);
    await randomDelay(2);
    await randomDelay(3);
    await randomDelay(4);
})();