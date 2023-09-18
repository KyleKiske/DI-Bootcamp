const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.json({message: "hello" });
});

router.get('/about/', (req, res) => {
    res.json({message: "this is a routed path"});
});

module.exports = {router};