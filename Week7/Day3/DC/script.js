let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = (groceries) => {
    groceries.fruits.forEach(fruit => {
        console.log(fruit);
    });
}
displayGroceries(groceries);


const cloneGroceries = (groceries) => {
    let user = client;
    client = "Betty";
    console.log(client);
    console.log(user);
    let shopping = groceries;
    groceries.totalPrice = "35$";
    console.log(groceries.totalPrice);
    console.log(shopping.totalPrice);
    groceries.other.paid = false;
    console.log(groceries.other.paid);
    console.log(shopping.other.paid);


}

// User will not change it's value, because String is a primitive type. 
// Shopping will change totalPrice, because Groceries is an object. Same thing goes for paid - it's variable inside of object;

cloneGroceries(groceries);