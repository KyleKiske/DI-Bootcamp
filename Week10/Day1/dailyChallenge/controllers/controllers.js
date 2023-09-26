const { _getAllUsers, _getUserById, _registerUser, _loginUser, _updateUser } = require('../models/models.js')
const bcrypt = require('bcrypt');

const getAllUsers = (req, res) => {
    _getAllUsers()
        .then((data) => {
            res.json(data);
        })
        .catch((err) => {
            console.log(err);
            res.status(404).json({ msg: "not found" });
        });
};

const getUser = async (req, res) => {
    try {
        const {id} = req.params;
        const data = await _getUserById(id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: "no user with matching id" });
    }
};

const registerUser = async (req, res) => {
    try {
        const data = await _registerUser(req.body);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

const loginUser = async (req, res) => {
    const { username, password } = req.body;
    try {
        const data = await _loginUser(username, password);
        if (bcrypt.compareSync(password, data[0].password)) {
            res.json(data);
        } else{
            throw new Error("password do not match");
        }
    } catch (error) {
        res.status(404).json({ msg: error.message });
    }
};

const updateUser = async (req, res) => {
    const { id } = req.params;
    // _updateUser(id)
    //     .then((data) => {
    //         res.json(data);
    //     })
    const { email, username, first_name, last_name } = req.body;

    try {
        const data = await _updateUser(req.body, id);
        res.json(data);
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: error.message });
    }
};

module.exports = {getAllUsers, getUser, registerUser, loginUser, updateUser};