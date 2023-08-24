// Create an array which value is the planets of the solar system.

let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
let colors = ['grey', 'orange', 'green', 'red', 'brown', 'yellow', 'blue', 'lightblue'];

let moons = [
    {count: 1, planet : "Earth"},
    {count: 2, planet : "Mars"},
    {count: 90, planet : "Jupiter"},
    {count: 145, planet : "Saturn"},
    {count: 27, planet : "Uranus"},
    {count: 14, planet : "Neptune"}];

let section = document.getElementsByClassName("listPlanets")[0];

let listPlanets = [];

for (let i = 0; i < planets.length; i++) {
    let div = document.createElement('div');
    div.setAttribute('class', `planet ${planets[i]}`);
    div.textContent = planets[i];
    div.style.backgroundColor = colors[i];
    listPlanets.push(div);
    section.appendChild(div);
}

for (let i = 0; i < moons.length; i++) {
    let div = document.createElement('div');
    div.setAttribute('class', 'moon');
    div.textContent = moons[i].count; 
    div.style.color = 'black';
    planetOfMoon = document.getElementsByClassName(moons[i].planet)[0];
    planetOfMoon.append(div);
}

// for (let i = 0; i < listPlanets.length; i++) {
//     section.append(listPlanets[i]);
// }