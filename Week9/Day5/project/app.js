const {router} = require('./routes/tasker.js');
const express = require('express');

const app = express();
app.use(express.json());
app.use('/tasks', router);

app.listen(3000, () => {
    console.log(`Server is running on port 3000`);
});