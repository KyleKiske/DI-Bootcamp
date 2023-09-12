import array from "./data.js";

function avgAge(array) {
        const result = array.reduce((a,b) => a + b.age, 0) / array.length;
        return result;
}

console.log(avgAge(array));