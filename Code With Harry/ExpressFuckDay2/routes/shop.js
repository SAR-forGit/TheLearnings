const express = require('express')
const router = express.Router()

router.get('/', (req, res) => res.send('Welcome to Shop'));

router.get('/aboutShop', (req, res) => res.send('We open this shop recently'));

module.exports = router;