const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
];

const usernames = []
gameInfo.forEach((value) => {
    usernames.push(value.username + "!");
});
console.log((usernames));

const winners = [];
gameInfo.forEach(value => {
    if (value.score > 5) {
        winners.push(value.username);
    }
});
console.log(winners);

let totalScore = gameInfo.reduce(function(prevVal, curVal) {
    return prevVal + curVal.score;
}, 0);

console.log(totalScore);
