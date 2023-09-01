// 🌟 Exercise 1 : Giphy API

// async function getPics () {
//   try {
//       const response = await fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
//       if (!response.ok) {
//           throw new Error("problem with fetch")
//       } else {
//           const data = await response.json();
//           console.log(data);
//       }
//   } catch (err) {
//       console.log("IN THE CATCH ", err);
//   }
// }
// getPics();

// 🌟 Exercise 2 : Giphy API

// async function getMorePics () {
//   try {
//       const response = await fetch("https://api.giphy.com/v1/gifs/search?q=sun&limit=10&offset=2&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
//       if (!response.ok) {
//           throw new Error("problem with fetch")
//       } else {
//           const data = await response.json();
//           console.log(data);
//       }
//   } catch (err) {
//       console.log("IN THE CATCH ", err);
//   }
// }
// getMorePics();

// 🌟 Exercise 3 : Async Function

// async function getstarShips(){
//   try{
//     const starshipsResponse = await fetch("https://www.swapi.tech/api/starships/9/")
//     if (!starshipsResponse.ok) {

//     } else{
//       const data = await starshipsResponse.json();
//       console.log(data.result);
//     }
//   } catch (err) {
//     console.log("CATCH", err);
//   }
// }
// getstarShips();

// 🌟 Exercise 4: Analyze

function resolveAfter2Seconds() {
  return new Promise(resolve => {
      setTimeout(() => {
          resolve('resolved');
      }, 2000);
  });
}

async function asyncCall() {
  console.log('calling');
  let result = await resolveAfter2Seconds();
  console.log(result);
}

asyncCall();

// Calling then result after timeout.