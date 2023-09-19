const fs = require('fs');

function readJson(req, res, next) {
    fs.readFile('users.json', 'utf8', (err, data) => {
        if (err) {
            next(err);
        } else {
            req.users = JSON.parse(data) || [];
            next();
        }
    });
}

function writeJson(req, res, next) {
    const users = req.users;
    fs.writeFile('users.json', JSON.stringify(users), 'utf8', (err) => {
        if (err) {
            next(err);
        } else {
            next();
        }
    });
}

module.exports = { readJson, writeJson };