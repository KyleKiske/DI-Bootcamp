const form = document.body.querySelector('#libform');

console.log(form);
const noun = document.body.querySelector("#noun");
const adjective = document.body.querySelector("#adjective");
const person = document.body.querySelector("#person");
const verb = document.body.querySelector("#verb");
const place = document.body.querySelector("#place");

function formSubmit(event) {
    event.preventDefault();
    const nounVal = noun.value;
    const adjVal = adjective.value;
    const personVal = person.value;
    const verbVal = verb.value;
    const placeVal = place.value;
    if (nounVal.length == 0 || adjVal.length == 0 || personVal.length == 0 || verbVal.length == 0 || placeVal == 0){
        return;
    }
    const span = document.querySelector('#story');
    span.innerText = `I haven't thought, that ${nounVal} saw ${adjVal} ${personVal} ${verbVal} in ${placeVal}`;
}

form.addEventListener('submit', formSubmit)
