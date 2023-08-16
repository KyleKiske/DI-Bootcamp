let sentence = "This movie is not that bad, I like it";

let wordNot = -1;

let wordBad = -1;

for (let i = 0; i < sentence.length - 2; i++) {
    if (sentence.slice(i, i+3) == 'not'){
        wordNot = i;
    }  else if (sentence.slice(i, i+3) == 'bad') {
        wordBad = i;
    }
}
let result = "";
if (wordBad >= 0 && wordNot >= 0){
    if (wordNot < wordBad) {
        result = sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad+3);
    }
}
if (result.length != 0){    
    console.log(result);
} else {
    console.log(sentence);
}
