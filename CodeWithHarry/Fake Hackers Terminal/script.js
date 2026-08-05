text = document.querySelector(".terminal").children;

randomDelay = () => {
    return new Promise((resolve, reject) => {
        timeOut = 1 + 6*Math.random();
        setTimeout(() => {
            resolve()
        },timeOut *1000)
    })
}

text = {}