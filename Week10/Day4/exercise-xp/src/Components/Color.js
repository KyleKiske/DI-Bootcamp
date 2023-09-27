import React, { useEffect } from "react";

class Color extends React.Component {
    constructor() {
        super();
        this.state = { 
            color: "red",
            show: true
        };
    }

    shouldComponentUpdate() {
        return true;
    }

    componentDidUpdate() {
        console.log("After update");
    }

    getSnapshotBeforeUpdate() {
        console.log("in getSnapshotBeforeUpdate")
    }

    setFavoriteColor = (color) => {
        this.setState({color : color});
    }

    render() {
        return (
            <div>
                <header>My favorite color is {this.state.color}</header>
                <button onClick={() => this.setFavoriteColor('blue')}>Change to blue</button>
                {this.state.show ? <Child/> : <div/>}
                <button onClick={() => this.setState({show: false})}>Hide Text above</button>
            </div>
        )
        
    }
}

class Child extends React.Component {
    constructor() {
        super();
    }


    componentWillUnmount() {
        alert("Component will unmount!!!");
    }

    render() {
        return (
            <div>
                <header>Hello, world!</header>
            </div>
        )
        
    }
}

export default Color;