const form = document.getElementById("form");

form.addEventListener('submit', getRandomGif);

async function getRandomGif(event) {
  event.preventDefault();
  const category = event.target.textInput.value;
  try {
      const response = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${category}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`);
      if (!response.ok) {
          throw new Error("problem with fetch")
      } else {
          const data = await response.json();
          addGif(data);
      }
  } catch (err) {
      console.log("IN THE CATCH ", err);
  }
}

function addGif(gifData) {
  const divImg = document.createElement('div');
  const gifEmbed = gifData.data.images.original.url;
  // const html = `<div>
  //       <img src="${gifEmbed}" alt="">
  //     </div>
  //     <button style=margin-left: 30px>DELETE</button>`

  // divImg.innerHTML = html;
  const image = document.createElement('img');
  image.setAttribute("src", gifEmbed);
  image.style = 'height: 200px';
  const button = document.createElement('button');
  button.innerText = "Delete gif";
  divImg.style = "display: -webkit-box";
  divImg.classList = "imageDiv";
  divImg.append(image, button);
  document.body.appendChild(divImg);
  deleteImgByButtonPress(divImg, button);
}

function deleteImgByButtonPress(image, button) {
  button.addEventListener('click', () => {
      image.remove();
  })
};

function deleteAllImages() {
  const button = document.querySelector('#remover');
  button.addEventListener('click', () => {
    const images = document.querySelectorAll(".imageDiv");
    for (const img of images) {
      img.remove();
    }
    
  })
}

deleteAllImages();