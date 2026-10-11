const express = require('express')
const router = express.Router()

router.get('/', (req, res) => res.send('Blog Home Page'));

router.get('/aboutBlog', (req, res) => res.send('About birds'));
router.get('/blogpost/:slug', (req, res) => res.send(`fetch the blogpost ${req.params.slug}`));

module.exports = router;