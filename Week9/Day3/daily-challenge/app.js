const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const app = express();
const emojis = require('./emojiData.js')

app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }
  
let score = 0;
let currentEmoji = getRandomEmoji();
let distractors = getRandomDistractors(emojis, currentEmoji, 3);

function getRandomEmoji() {
  const randomIndex = Math.floor(Math.random() * emojis.length);
  return emojis[randomIndex];
}

function getRandomDistractors(emojis, currentEmoji, numDistractors) {
    const distractors = [];
    while (distractors.length < numDistractors) {
      const randomIndex = Math.floor(Math.random() * emojis.length);
      const randomEmoji = emojis[randomIndex];
      if (randomEmoji.name !== currentEmoji.name && !distractors.includes(randomEmoji.name)) {
        distractors.push(randomEmoji.name);
      }
    }
    return distractors;
  }

app.get('/game', (req, res) => {
    const options = [currentEmoji.name, ...distractors];  
    shuffleArray(options);
  
    res.json({ emoji: currentEmoji, score, options });
  });

app.post('/guess', (req, res) => {
    const { guess } = req.body;
    if (guess === currentEmoji.name) {
      score++;
      currentEmoji = getRandomEmoji();
      distractors = getRandomDistractors(emojis, currentEmoji, 3);
      res.json({ correct: true, score });
    } else {
      res.json({ correct: false, score });
    }
  });
  
app.listen(5000, () => {
  console.log(`Server is running on port 5000`);
});