// 🌟 Exercise 1 : Find The Numbers Divisible By 23

function displayNumbersDivisible(divisor) {
    let sum = 0;
    resultString = 'Outcome :';
    for (let i = 0; i <= 500; i++){
        if (i % divisor == 0) {
            sum += i;
            resultString += " " + i;
        }
    }
    console.log(resultString);
    console.log("sum :", sum);
}

// displayNumbersDivisible(50);

// 🌟 Exercise 2 : Shopping List

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// shoppingList = ["banana", "orange", "apple"];

// function myBill() {
//     cost = 0;
//     for (let i = 0; i < shoppingList.length; i++) {
//         if (shoppingList[i] in stock){
//             if (stock[shoppingList[i]] > 0){
//                 stock[shoppingList[i]]--;
//                 cost += prices[shoppingList[i]];
//             }
//         }
//     }
//     return cost;
// }
// console.log(stock);
// console.log(myBill());
// console.log(stock);

// 🌟 Exercise 3 : What’s In My Wallet ?

// function changeEnough(itemPrice, amountOfChange){
//     let sum = 0;
//     sum += amountOfChange[0] * 0.25;
//     sum += amountOfChange[1] * 0.10;
//     sum += amountOfChange[2] * 0.05;
//     sum += amountOfChange[3] * 0.01;
//     if (sum > itemPrice) {
//         return true;
//     } else {
//         return false;
//     }
// }

// console.log(changeEnough(14.11, [2,100,0,0]));
// console.log(changeEnough(0.75, [0,0,20,5]));

// 🌟 Exercise 4 : Vacations Costs

// function hotelCost() {
//     let nights = 0
//     while(nights == 0 || nights == NaN){
//         nights = prompt("How many nights will you stay?")
//     }
//     return nights * 140;
// }

// function planeRideCost() {
//     let destonation = ""
//     while(destonation == "" || destonation == NaN){
//         destonation = prompt("Where are you traveling to?")
//     }
//     if (destonation == "London") {
//         return 183;
//     } else if (destonation == "Paris") {
//         return 220;
//     } else {
//         return 300;
//     }
// }

// function rentalCarCost() {
//     let days = 0
//     while(days == 0 || days == NaN){
//         days = prompt("How many days will you rent car?")
//     }
//     if (days > 10) {
//         return days * 40 * 0.95;
//     } else {
//         return days * 40;
//     }
// }

// function totalVacationCost(){
//     hotel = hotelCost();
//     plane = planeRideCost();
//     car = rentalCarCost();
//     return `Your vacation will cost $${hotel} for hotel, $${car} for car and $${plane} for plane ticket.`;
// }

// console.log(totalVacationCost());