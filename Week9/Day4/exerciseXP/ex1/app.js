const {router} = require('./routes/index.js');
const express = require('express');

const app = express();

app.use('/', router);

// app.use('/about/', router);

app.listen(3000, () => {
    console.log(`Server is running on port 3000`);
});