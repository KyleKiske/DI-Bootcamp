import React from "react";
import { useState } from "react";

const Events = (props) => {
    let [isToggleOn, setToggle] = useState(true);
    const clickMe = (event) => {
        alert("I was clicked");
    }

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            alert(`Enter was pressed, your input: ${event.target.value}`)
        }
    }

    return (
        <div>
            <button onClick={clickMe}>Click me!</button>
            <br></br>
            <input onKeyDown={handleKeyDown}></input>
            <button onClick={() => setToggle(!isToggleOn)}>{isToggleOn ? 'ON' : 'OFF'}</button>
        </div>
    )
}

export default Events;