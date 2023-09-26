const UserFavoriteAnimal = (props) => {
    const {info} = props;
    console.log(props);
    return (
        <ul>
            {info.map((item, index) => {
                return <li id={index}>{item}</li>
            })}
        </ul>
    )
}

export default UserFavoriteAnimal;