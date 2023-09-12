const products = require('./products.js');

function search(name) {
    const found = products.find((product) => product.name == name);
    console.log(found);
}

search("banana");

search("cucumber");