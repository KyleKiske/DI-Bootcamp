// 🌟 Exercise 1 : Location

// const person = {
//   name: 'John Doe',
//   age: 25,
//   location: {
//       country: 'Canada',
//       city: 'Vancouver',
//       coordinates: [49.2827, -123.1207]
//   }
// }

// const {name, location: {country, city, coordinates: [lat, lng]}} = person;

// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);

// 🌟 Exercise 2: Display Student Info

// user = {
//   first: "Elie",
//   last: "Schoppik"
// };

// function displayStudentInfo(objUser){
//   const {first, last} = objUser;
//     console.log(`Your full name is ${first} ${last}`);
// }

// displayStudentInfo({first: 'Elie', last:'Schoppik'});
// 🌟 Exercise 3: User & Id

// const users = { user1: 18273, user2: 92833, user3: 90315 }

// let entries = Object.entries(users);
// console.log(entries);
// let partTwo = Object.entries(users).map(([user, id]) => [user, id*2]);
// console.log(partTwo);

// Exercise 4 : Person Class

// class Person {
//   constructor(name) {
//     this.name = name;
//   }
// }

// const member = new Person('John');
// console.log(typeof member);

// tyoe will be object.

// 🌟 Exercise 5 : Dog Class

// class Dog {
//   constructor(name) {
//     this.name = name;
//   }
// };

// 1
// class Labrador extends Dog {
//   constructor(name, size) {
//     this.size = size;
//   }
// };
// This won't work, because it doesn't call parent constructor

// // 2
// class Labrador extends Dog {
//   constructor(name, size) {
//     super(name);
//     this.size = size;
//   }
// };
// This one is fine

// // 3
// class Labrador extends Dog {
//   constructor(size) {
//     super(name);
//     this.size = size;
//   }
// };
// This one doesn't assign name anywhere.

//   // 4
// class Labrador extends Dog {
//   constructor(name, size) {
//     this.name = name;
//     this.size = size;
//   }
// };
// This won't work, because it doesn't call parent constructor

// 🌟 Exercise 6 : Challenges 

// console.log([2] === [2]); 
// console.log({} === {});

// const object1 = { number: 5 }; 
// const object2 = object1; 
// const object3 = object2; 
// const object4 = { number: 5};

// object1.number = 4;
// console.log(object2.number);
// console.log(object3.number);
// console.log(object4.number);

// 1 : 4
// 2 : 4
// 3 : 4
// 4 : 5

class Animal {
  constructor(name, type, color) {
    this.name = name;
    this.type = type;
    this.color = color;
  }
}

class Mamal extends Animal {
  constructor(name, type, color) {
    super(name, type, color);
  };

  sound(sound) {
    return (`${sound} I'm a ${this.type}, named ${this.name} and I'm ${this.color}`);
  }
}

let farmerCow = new Mamal("Daisy", "Cow", "brown", "moo");

console.log(farmerCow.sound("Moo"));