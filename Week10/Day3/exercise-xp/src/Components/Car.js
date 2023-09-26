import React from "react";
import { useState } from "react";
import Garage from "./Garage";

const Car = (props) => {
    const [color] = useState("black");
    return (
        <div>
            <header>This car is {color} {props.info.model}</header>
            <Garage size='small'></Garage>
        </div>
    )
}

export default Car;