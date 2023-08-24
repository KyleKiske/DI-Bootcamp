// // 🌟 Exercise 1 : Change The Article

h1 = document.getElementsByTagName("h1")[0];
console.log(h1);

article = document.querySelector('article');
lastP = article.querySelector("p:last-of-type");
article.removeChild(lastP);

h2 = document.getElementsByTagName("h2")[0];
h2.addEventListener("click", function() {h2.style.backgroundColor = 'red'});


h3 = document.getElementsByTagName("h3")[0];
h3.addEventListener("click", function() {h3.style.display = 'none'});


button = document.createElement('button')
button.innerText = 'Embolden the text'
document.body.appendChild(button)
button.addEventListener('click', () => {
    const ps = article.querySelectorAll("p");
    for (let i = 0; i < ps.length; i ++) {
        ps[i].style.fontWeight = 'bold';
    }
})

h1.addEventListener("mouseover", function() {h1.style.fontSize = Math.random()*100 + "px"});

const secondP = article.querySelectorAll('p')[1];
secondP.addEventListener("mouseover", function() {secondP.classList.add('fadeout');});

// 🌟 Exercise 2 : Work With Forms

// const form = document.body.getElementsByTagName('form')[0];

// console.log(form);
// const fname = document.body.querySelector("[name=firstname]");
// const lname = document.body.querySelector("[name=lastname]");
// console.log(fname);
// console.log(lname);

// function formSubmit(event) {
//     event.preventDefault();
//     const name = fname.value;
//     const surname = lname.value;
//     if (name.length == 0 || surname.length == 0){
//         return;
//     }
//     const ilName = document.createElement('il');
//     ilName.textContent = name;
//     const ilLName = document.createElement('il');
//     ilLName.textContent = surname;
//     const answers = document.getElementsByClassName('usersAnswer')[0];
//     answers.appendChild(ilName);
//     answers.appendChild(ilLName);
// }

// form.addEventListener('submit', formSubmit)

// 🌟 Exercise 3 : Transform The Sentence

// let allBoldItems = '';

// function getBoldItems() {
//     let bolds = document.body.querySelectorAll('strong');
//     for (let i = 0; i < bolds.length; i++) {
//         allBoldItems += bolds[i].innerText;
//     }
// }

// getBoldItems();
// console.log(allBoldItems);

// function highlight() {
//     let bolds = document.body.querySelectorAll('strong');
//     for (let i = 0; i < bolds.length; i++) {
//         bolds[i].style.color = 'blue';
//     }
// }

// function returnItemsToDefault() {
//     let bolds = document.body.querySelectorAll('strong');
//     for (let i = 0; i < bolds.length; i++) {
//         bolds[i].style.color = null;
//     }
// }
// const par = document.querySelector('p');
// par.addEventListener("mouseover", highlight);
// par.addEventListener("mouseout", returnItemsToDefault);

// 🌟 Exercice 4 : Volume Of A Sphere

// const form = document.body.getElementsByTagName('form')[0];

// const radius = document.body.querySelector("#radius");
// const volume = document.body.querySelector("#volume");

// function formSubmit(event) {
//     event.preventDefault();
//     const radVal = radius.value;
//     let volumeVal = 0;
//     // const surname = lname.value;
//     if (radVal >= 0){
//         volumeVal = 4 /3 * Math.PI * Math.pow(radVal, 3);
//     } else { 
//         alert("Radius should be not negative");
//         return;
//     }
//     volume.value = volumeVal;
// }

// form.addEventListener('submit', formSubmit);

//🌟 Exercise 5 : Event Listeners

// const div = document.querySelector('#ex')

// div.addEventListener("click", (e) => {
//     div.style.position = 'absolute';
//     div.style.left = '100px';
// })

// div.addEventListener("mouseover", (e) => {
//     div.style.backgroundColor = 'lightblue';
// })

// div.addEventListener("mouseout", (e) => {
//     div.style.backgroundColor = null;
// })

// div.addEventListener("dblclick", (e) => {
//     div.style.position = null;
// })