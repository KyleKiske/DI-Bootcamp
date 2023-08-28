// #1
// function funcOne() {
//     const a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne()
//Alert with 3.

// #1.2 What will happen if the variable is declared 
// with const instead of let ?

// Error, because we try to reassign value to const.

// #2
// const a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// // alert with 0, alert with 5

// #2.2 What will happen if the variable is declared 
// with const instead of let ?

// alert with 0 then error, because we try to reassign value to const.

// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// Alert with hello.

// //#4
// const a = 1;
// function funcSix() {
//     const a = "test";
//     alert(`inside the funcSix function ${a}`);
// }

// // #4.1 - run in the console:
// funcSix()
//Alert with value from function body.

// #4.2 What will happen if the variable is declared 
// with const instead of let ?
// Nothing will change, since these are different scopes.

// //#5
// const a = 2;
// if (true) {
//     const a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared 
// with const instead of let ?
//Nothing will change, since these are different scopes.

// 🌟 Exercise 2 : Ternary Operator

// function winBattle(){
//     return true;
// }

// winBattle = () => {
//     return true;
// }

// let experiencePoints = 0;
// experiencePoints = winBattle() ? 10 : 1;

// console.log(experiencePoints);

// 🌟 Exercise 3 : Is It A String ?

// isString = (argument) => {
//     return typeof(argument) == "string" ? true : false
// }

// console.log(isString('hello')); 
// console.log(isString([1, 2, 4, 0]));

// 🌟 Exercise 4 : Find The Sum

// sum = (a, b) => a + b;

// console.log(sum(2,7));

// 🌟 Exercise 5 : Kg And Grams

// function convert(mass) {
//     return mass * 1000;
// }
// console.log("Declaration =>", convert(3.5));

// let result = function(mass) {return mass * 1000}
// console.log("Expression =>", result(4.5));
// // With expression we assign function to a variable.

// convertMetric = (mass) => mass * 1000;
// console.log("Arrow =>", convertMetric(5.5));

// 🌟 Exercise 6 : Fortune Teller

// (function (childCount, spouseName, location, jobTitle) {
//     result = `You will be a ${jobTitle} in ${location}, and married to ${spouseName} with ${childCount} kids.`;
//     let div = document.createElement("div");
//     div.tex = result;
//     document.body.appendChild(div);
// })(5,"Jane", "DC", "interpreter")

// 🌟 Exercise 7 : Welcome

// (function (userName) {
//     let div = document.createElement("div");
//     div.innerText = userName;
//     document.getElementById('nam').appendChild(div);
// })("Jane")

// 🌟 Exercise 8 : Juice Bar

// Part I
// function makeJuice(size) {
//     let ingredients = [];
//     function addIngredients(ingredFirst, ingredSecond, ingredThird) {
//         ingredients.push(ingredFirst, ingredSecond, ingredThird);
//         result = `The client wants a ${size} juice, containing ${ingredFirst}, ${ingredSecond}, ${ingredThird}`;
//         let div = document.createElement("div");
//         div.innerText = result;
//         document.body.appendChild(div);
//     }
//     return addIngredients;
// }
// makeJuice("small")("pivo", "vodka", "jin");


// Part II
function makeJuice(size) {
    let ingredients = [];
    function addIngredients(ingredFirst, ingredSecond, ingredThird) {
        ingredients.push(ingredFirst, ingredSecond, ingredThird);
    }
    function displayJuice() {
        let result = `The client wants a ${size} juice, containing ${ingredients.join(", ")}`;
        let div = document.createElement("div");
        div.innerText = result;
        document.body.appendChild(div);
    }
    addIngredients('blueberry', 'grape', 'carrot');
    addIngredients('scotch', 'jin', 'rum');
    displayJuice();
}
makeJuice("small");