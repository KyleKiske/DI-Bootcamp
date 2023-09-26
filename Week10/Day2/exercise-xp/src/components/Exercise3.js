import "./Exercise.css"

const Exercise = () => {

    // const style_header = {
    //     color: "red",
    //     backgroundColor: "lightblue"
    // }
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
      };
    return (
        <div>
            <h1 style={style_header}>This is a Header</h1>
            <p className="para">This is a paragraph</p>
            <a href="https://react.dev">This is a link to React</a>
            <form>
                 <input type="text" defaultValue="THE FORM"></input>
                 <button type="button">The form button</button>
            </form>
            <br/>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/F1.svg/640px-F1.svg.png"></img>
            <ul>
                <li>node</li>
                <li>react</li>
                <li>yarn</li>
            </ul>
        </div>        
    )
}

export default Exercise;