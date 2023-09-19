const fs = require('fs');

function readJson(req, res, next) {
    fs.readFile('tasks.json', 'utf8', (err, data) => {
        if (err) {
            next(err);
        } else {
            req.tasks = JSON.parse(data) || [];
            next();
        }
    });
}

function writeJson(req, res, next) {
    const tasks = req.tasks;
    fs.writeFile('tasks.json', JSON.stringify(tasks), 'utf8', (err) => {
        if (err) {
            next(err);
        } else {
            next();
        }
    });
}

module.exports = { readJson, writeJson };