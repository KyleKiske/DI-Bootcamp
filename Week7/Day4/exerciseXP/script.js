// 🌟 Exercise 1 : Colors

// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// colors.forEach((color, index) => {
//     console.log(`${index + 1}# choice is ${color}`);
// })

// if (colors.some((color) => {
//     return color == 'Violet';})) {
//     console.log("Yeah");
// } else {
//     console.log('No...');
// }

// 🌟 Exercise 2 : Colors #2

// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// const ordinal = ["th","st","nd","rd"];

// colors.map((color, index) => {
//     let ending = index >= 3 ? ordinal[0] : ordinal[index + 1];
//     console.log(`${index + 1}${ending} choice is ${color}.`);
// });

// 🌟 Exercise 3 : Analyzing

// // ------1------
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result);

// // ------2------
// const country = "USA";
// console.log([...country]);

// // ------Bonus------
// let newArray = [...[,,]];
// console.log(newArray);


// 🌟 Exercise 4 : Employees

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

const welcomeStudents = users.map((value) => `Welcome ${value.firstName}`);
console.log(welcomeStudents);

const filtered = users.filter(value => value.role == 'Full Stack Resident');
console.log(filtered);

const lastNameFiltered = users.filter(value => value.role == 'Full Stack Resident').map((value) => `${value.lastName}`);
console.log(lastNameFiltered);

// 🌟 Exercise 5 : Star Wars

const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

let SW = epic.reduce(function(prevVal, curVal) {
    return prevVal + " " + curVal;
})
console.log(SW);

// 🌟 Exercise 6 : Employees #2

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];

let passed = students.filter((value) => value.isPassed == true);
console.log(passed);

// Bonus 

let passedGJ = students.filter((value) => value.isPassed == true).forEach((value) => {
    console.log(`Good job ${value.name}, you passed the course in ${value.course}`);
});