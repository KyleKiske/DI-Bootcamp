// 🌟 Exercise 6 : Change The Navbar

let elem = document.querySelector('#navBar');
elem.setAttribute("id", "socialNetworkNavigation");
let li = document.createElement('li');

let newTextNode = document.createTextNode('Logout');
li.append(newTextNode);

let ul = document.querySelector('ul');
ul.append(li);

let first = ul.firstElementChild.textContent;
let last = ul.lastElementChild.textContent;

console.log(first);
console.log(last);

const holmes = {
    title : "A study in Scarlet",
    author : "Sir Arthur Conan Doyle",
    image : "https://upload.wikimedia.org/wikipedia/commons/2/2c/ArthurConanDoyle_AStudyInScarlet_annual.jpg",
    alreadyRead : true
};

const prince = {
    title : "The Prince",
    author : "Niccolo Machiavelli",
    image : "https://upload.wikimedia.org/wikipedia/commons/7/77/Machiavelli_Principe_Cover_Page.jpg",
    alreadyRead : false
};

let allBooks = [holmes, prince];

let listBooks = document.getElementsByClassName("listBooks")[0];

for (let i = 0; i < allBooks.length; i++) {
    let div = document.createElement('div');
    let divText = document.createTextNode(`${allBooks[i].title} by ${allBooks[i].author}`);
    if (allBooks[i].alreadyRead) {
        div.style.color = 'red';
    }
    div.append(divText);
    let myImage = new Image(100);
    myImage.src = allBooks[i].image;
    div.append(myImage);
    listBooks.append(div);
}