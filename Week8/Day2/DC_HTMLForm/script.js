const form = document.getElementById('form');
form.addEventListener('submit', getInputs);

function getInputs(event) {
  event.preventDefault();
  const name = event.target.firstName.value;
  const lastName = event.target.lastName.value;
  const div = document.createElement("div");
  div.innerHTML = `{name: ${name}, lastName: ${lastName}}`;
  document.body.appendChild(div);
}