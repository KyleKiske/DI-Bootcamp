const {router} = require('./routes/todos.js');
const express = require('express');

const app = express();
app.use(express.json());
app.use('/todos', router);

app.listen(3000, () => {
    console.log(`Server is running on port 3000`);
});