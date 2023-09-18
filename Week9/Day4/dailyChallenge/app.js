const {router} = require('./routes/quiz.js');
const express = require('express');

const app = express();
app.use(express.json());
app.use('/quiz', router);

app.listen(3000, () => {
    console.log(`Server is running on port 3000`);
});