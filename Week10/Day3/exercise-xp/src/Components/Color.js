import React, { useEffect } from "react";
import { useState } from "react";

const Color = (props) => {
    const [favoriteColor, setFavoriteColor] = useState("red");
    
    useEffect(() => {
        alert('useEffect reached');
    }, [])

    return (
        <div>
            <header>My favorite color is {favoriteColor}</header>
            <button onClick={() => setFavoriteColor('blue')}>Change to blue</button>
        </div>
    )
}

export default Color;