import fs from "fs";

const content = fs.readFileSync("./file-data.txt", "utf-8", (err, data) => {
    if (err) {
        console.error(err);
    } return data;
});

export default content;