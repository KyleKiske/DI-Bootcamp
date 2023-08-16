console.log('one loop');
for (let i = 0; i < 6; i++) {
    const star = "* "
    console.log(star.repeat(i+1));
}

console.log('nested loop');
for (let i = 0; i < 6; i++) {
    const star = "* "
    let result = "";
    for (let j = 0; j <= i; j++) {
        result += star;
    }
    console.log(result);
}

