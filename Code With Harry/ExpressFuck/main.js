const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public'));

function htlm(){
    b = "<h1>Hello World how are you?</h1> <p> niggesh hi </p>"

    return b;
}

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get("/blog:slug", (req, res) => res.send(`hello ${req.params.slug}`));
app.get("/blog/:slug", (req, res) => res.send(`hello ${req.params.slug}`));

app.get('/contact', (req, res) => res.send(htlm()))

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});