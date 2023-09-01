const button = document.getElementById("button");
button.addEventListener('click', getExchangedAmount);

let codes = []

async function getCodes() {
  try {
    const response = await fetch(`https://v6.exchangerate-api.com/v6/76c5b554f57b26db6ea9ee0c/codes`);
    if (!response.ok) {
        throw new Error("Something went wrong")
    } else {
        const data = await response.json();
        codes = data.supported_codes;
        putCodesInSelects(data);
    }
  } catch (err) {
      console.log("IN THE CATCH ", err);
  }
}

function putCodesInSelects(data) {
  let curFrom = document.getElementById('curFrom');
  let curTo = document.getElementById('curTo');
  for (let i = 0; i < data.supported_codes.length; i++) {
    let opt = document.createElement('option');
    opt.value = data.supported_codes[i][0];
    opt.innerHTML = ` ${data.supported_codes[i][0]} - ${data.supported_codes[i][1]}`;
    curFrom.appendChild(opt);
  }
  for (let i = 0; i < data.supported_codes.length; i++) {
    let opt = document.createElement('option');
    opt.value = data.supported_codes[i][0];
    opt.innerHTML = ` ${data.supported_codes[i][0]} - ${data.supported_codes[i][1]}`;
    curFrom.appendChild(opt);
    curTo.appendChild(opt);
  }
}

getCodes();

async function getExchangedAmount() {
  var fromSelect = document.getElementById("curFrom");
  var toSelect = document.getElementById("curTo");
  let amount = document.getElementById('amount');
  try {
    const response = await fetch(`https://v6.exchangerate-api.com/v6/76c5b554f57b26db6ea9ee0c/pair/${fromSelect.value}/${toSelect.value}`);
    if (!response.ok) {
        throw new Error("Something went wrong")
    } else {
        const data = await response.json();
        let exchangeRate = data.conversion_rate;
        let result = exchangeRate * amount.value;
        let resultField = document.getElementById('result');
        resultField.innerText = result;
    }
  } catch (err) {
      console.log("IN THE CATCH ", err);
  }
  
}
