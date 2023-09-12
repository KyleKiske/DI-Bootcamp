const emojiDiv = document.getElementById('emoji');
const optionsDiv = document.getElementById('options');
const scoreSpan = document.getElementById('score');
const guessForm = document.getElementById('guessForm');

async function loadGame() {
    const response = await fetch('/game');
    const { emoji, score, options } = await response.json();

    emojiDiv.textContent = emoji.emoji;
    scoreSpan.textContent = score;

    const radioButtons = document.querySelectorAll('input[type="radio"]');
    const labels = document.querySelectorAll('label');
    optionsDiv.innerHTML = '';

    options.forEach((option, index) => {
        radioButtons[index].value = option;
        labels[index].innerText = option;
    });
}

async function makeGuess(event) {
    event.preventDefault();

    const formData = new FormData(guessForm);
    const guess = formData.get('guess');

    const response = await fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ guess }),
    });

    const { correct, score } = await response.json();

    if (correct) {
        alert('Correct guess!');
    } else {
        alert('Incorrect guess. Try again.');
    }
    loadGame();
}

guessForm.addEventListener('submit', makeGuess);

loadGame();