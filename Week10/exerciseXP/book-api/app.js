const {router} = require('./routes/router.js');
const express = require('express');

const app = express();
app.use(express.json());
app.use('/api/books', router);

app.listen(3000, () => {
    console.log(`Server is running on port 3000`);
});
    