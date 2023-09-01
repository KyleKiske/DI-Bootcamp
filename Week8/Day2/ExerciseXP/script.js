// 🌟 Exercise 1 : Comparison

function compareToTen(num) {
  if (num <= 10) {
    return Promise.resolve("Number is less or equal to 10");
  } else {
    return Promise.reject("Number is bigger that 10");
  }
};

//In the example, the promise should reject
compareToTen(15)
  .then(result => console.log(result))
  .catch(error => console.log(error));

//In the example, the promise should resolve
compareToTen(8)
  .then(result => console.log(result))
  .catch(error => console.log(error));


// 🌟 Exercise 2 : Promises

let promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('success');
  }, 4000);
});

promise.then(result => {
  console.log(result);
});

// 🌟 Exercise 3 : Resolve & Reject

console.log(Promise.resolve(3));
console.log(Promise.reject("Boo"));