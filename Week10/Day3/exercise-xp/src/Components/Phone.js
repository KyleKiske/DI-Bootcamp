import React from "react";
import { useState } from "react";

const Phone = (props) => {
    const [brand, setBrand] = useState("Samsung");
    const [model, setModel] = useState("Galaxy S20");
    const [color, setColor] = useState("black");
    const [year, setYear] = useState("2020");
    const changeColor = () => {
        setColor('blue');
    }
    return (
        <div>
            <h3>My phone is a {brand}</h3>
            <p>It is a {color} {model} from {year}</p>
            <button onClick={changeColor}>Change phone color</button>
        </div>
    )
}

export default Phone;