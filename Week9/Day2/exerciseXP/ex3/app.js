const {writeFileSelf, readFileSelf} = require('./fileManager.js');

readFileSelf('./Hello World.txt');
writeFileSelf( "Writing to the file", "./Bye World.txt")