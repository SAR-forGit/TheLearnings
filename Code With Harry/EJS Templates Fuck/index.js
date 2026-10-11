const express = require("express");
const app = express();
const port = 3000;

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    let siteName = 'Adidas ici', searchText = 'Commo Sa Va?';
    res.render("index", { siteName, searchText});
})

app.get('/blog/:slug', (req, res) => {
    let BlogTitle = 'Adidas why and when?', BlogContent = "It's very Good";
    res.sendFile("blogpost", { BlogTitle: BlogTitle, BlogC: BlogContent});
})

app.listen(port, () => {
    console.log('Example app listening on port ${port');
})