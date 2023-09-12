import chalk from "chalk";

function colorfulMessage() {
    console.log(chalk.red.bold("Red") + chalk.green.bgBlack(" Green ") + chalk.blue.bgWhite("Blue"));
}

export default colorfulMessage;