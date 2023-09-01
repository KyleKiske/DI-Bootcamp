const button = document.getElementById("button");
button.addEventListener('click', getSomeoneRandom);
const container = document.querySelector('.info-container');

async function getSomeoneRandom() {
  container.innerHTML = `
  <div class="fa-4x">
  <i id='loader' class="fa-solid fa-spinner fa-spin-pulse fa-spin-reverse"></i>
  </div>
  <span>Loading...</span>`;
  let randomNumber = Math.floor(Math.random() * (83-1) + 1);
  try {
    const response = await fetch(`https://www.swapi.tech/api/people/${randomNumber}`);
    if (!response.ok) {
        const name = document.getElementById("name");
        name.innerText = "Oh No! That person isnt available.";
        throw new Error("Person not found")
    } else {
        const data = await response.json();
        displayInfo(data.result);
    }
  } catch (err) {
      console.log("IN THE CATCH ", err);
  }
}

async function displayInfo(result) {
  let worldName = "";
  container.innerHTML = ``;
  try {
    const response = await fetch(result.properties.homeworld);
    if (!response.ok) {
        throw new Error("Planet not found")
    } else {
        const data = await response.json();
        worldName = data.result.properties.name;
    }
  } catch (err) {
      console.log("IN THE CATCH ", err);
  }
  container.innerHTML = `
  <h1 id="name">${result.properties.name}</h1>
  <p id="height">Height: ${result.properties.height}</p>
  <p id="gender">Gender: ${result.properties.gender}</p>
  <p id="birth-year">Birth Year: ${result.properties.birth_year}</p>
  <p id="home-world">Home World: ${worldName}</p>`;
}