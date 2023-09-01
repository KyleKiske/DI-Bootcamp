// function makeAllCaps(arrOfWords) {
//   return new Promise ((resolve, reject) => {
//     isGood = true;
//     for (const word of arrOfWords) {
//       if (typeof(word) != "string") {
//         isGood = false;
//         break;
//       }
//     }
//     if (isGood) {
//       resolve(arrOfWords.map((x) => x.toUpperCase()));
//     } else {
//       reject("One of words is not string");
//     }
//   });
// }

// function sortWords(arrOfWords) {
//   return new Promise ((resolve, reject) => {
//     if (arrOfWords.length > 4) {
//       resolve(arrOfWords.sort());
//     } else{
//       reject('Arr length is smaller than 5');
//     }
//   });
// }

// makeAllCaps([1, "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error));

// //in this example, the catch method is executed
// makeAllCaps(["apple", "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error));

// //in this example, you should see in the console, 
// // the array of words uppercased and sorted
// makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
//       .catch(error => console.log(error));

const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`;

function toJs(morseString) {
  return new Promise ((resolve, reject) => {
    const MorseObject = JSON.parse(morseString);
    if (Object.keys(MorseObject).length === 0) {
      reject("Object is empty!");
    } else{
      resolve(MorseObject);
    }
  });
}

function toMorse(morseJS) {
  return new Promise ((resolve, reject) => {
    let userString = prompt("Write a sentence");
    let morseArray = [];
    for (const char of userString) {
      if (char.toLowerCase() in morseJS) {
        morseArray.push(morseJS[char.toLowerCase()]);
      } else{
        reject(`Character ${char} doesn't exist in morse!`)
      }
    }
    resolve(morseArray);
  });
}

function joinWords(morseTranslation) {
  const par = document.createElement('p');
  let theString = "";
  for (let word of morseTranslation) {
    theString += word;
    theString += " <br>";
  }
  par.innerHTML = theString;
  document.body.appendChild(par);
  return true;
}

toJs(morse)
  .then((morseObj) => toMorse(morseObj))
  .then((morseArray) => joinWords(morseArray))
  .catch((err) => console.log(err));