const express = require('express');
const router = express.Router();
const triviaQuestions = require('../public/questions.js');
const e = require('express');

let score = 0;
let curIndex = 0;
// Get all books
router.get('/', (req, res) => {
    score = 0;
    curIndex = 0;
    res.json(triviaQuestions[0].question);
});

// Add a new book
router.post('/', (req, res) => {
    const {answer} = req.body;
    if (triviaQuestions.length == curIndex) {
        res.send("There are no more questions. Proceed to quiz/score to find out your result");
        return;
    } 
    if (answer == triviaQuestions[curIndex].answer) {
        score++;
    }
    curIndex++;
    if (triviaQuestions.length == curIndex) {
        res.send("There are no more questions. Proceed to quiz/score to find out your result");
        return;
    } 
    res.json(triviaQuestions[curIndex].question);
});

router.get('/score', (req, res) => {
    res.send(`You scored ${score}`);
});

module.exports = {router};