// Part 1
// function alertFunction() {
//     alert("Hello, World!")
// }

// setTimeout(alertFunction, 2000);

// Part 2
// function addPar() {
//     const divak = document.querySelector('#container');
//     const par = document.createElement('p');
//     par.innerText = "Hello World";
//     divak.appendChild(par);
// }

// setTimeout(addPar, 2000);

// Part 3
// let timer = setInterval(addPar, 2000);

// const button = document.querySelector('#clear');

// function myStopFunction() { 
//     clearInterval(timer);
// };

// button.addEventListener('click', myStopFunction);

// Part 3 continued
// let timer = setInterval(limitedFill, 2000);

// function limitedFill() { 
//     const divak = document.querySelector('#container');
//     const par = document.createElement('p');
//     par.innerText = "Hello World";
//     divak.appendChild(par);
//     if (divak.querySelectorAll('p').length >= 5 ){
//         clearInterval(timer);
//     }
// };

// myStopFunction();
 
// 🌟 Exercise 2 : Move The Box
let move = 0;
let timer;
const button = document.querySelector('button');
button.addEventListener('click', () => {
    timer = setInterval(myMove, 1);
});

function myMove() {
    move++;
    const red = document.querySelector('#animate');
    red.style.left = `${move}px`;
    const yellow = document.querySelector('#container');
    if (move + red.offsetWidth >= yellow.offsetWidth) {
        clearInterval(timer);
    }
}