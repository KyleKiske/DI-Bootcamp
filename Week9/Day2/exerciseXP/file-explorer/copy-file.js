const fs = require('fs');

const content = fs.readFileSync('./source.txt', (err,data) => {
    if (err) {
        console.error(err);
    } else {
        return data;
    }
});

fs.writeFile("destination.txt", content, (err) => {
    if (err) {
        console.error(err);
        return;
    }
});