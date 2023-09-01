const button = document.getElementById("button");
button.addEventListener('click', getSomeoneRandom);

async function getSomeoneRandom() {
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
  const name = document.getElementById("name");
  name.innerText = result.properties.name;
  const height = document.getElementById("height");
  height.innerText = `Height: ${result.properties.height}`;
  const gender = document.getElementById("gender");
  gender.innerText = `Gender: ${result.properties.gender}`;
  const birthYear = document.getElementById("birth-year");
  birthYear.innerText = `Birth Year: ${result.properties.birth_year}`;
  const homeWorld = document.getElementById("home-world");
  homeWorld.innerText = `Home World: ${worldName}`;
}