const fs = require('fs');

function readFileSelf(path) {
    fs.readFile(path, 'utf-8', (err, data) => {
        if (err) {
            return console.log(err);
        }
        console.log(data);
    });
}

function writeFileSelf(data, path) {
    fs.writeFile(path, data, function (err) { 
        if (err){ 
            console.log(err);
        }
        else{
            console.log('Write operation complete.');
        }
    });
}

writeFileSelf("Hello, World !!", "Hello World.txt");
writeFileSelf("Bye, World !!", "Bye World.txt");

module.exports = {writeFileSelf, readFileSelf};