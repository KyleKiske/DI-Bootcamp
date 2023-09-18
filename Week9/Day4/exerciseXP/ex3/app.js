const {router} = require('./routes/books.js');
const express = require('express');

const app = express();
app.use(express.json());
app.use('/books', router);

app.listen(3000, () => {
    console.log(`Server is running on port 3000`);
});