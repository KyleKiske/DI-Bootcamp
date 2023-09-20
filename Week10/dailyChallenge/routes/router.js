const express = require('express');
const router = express.Router();
const {getAllUsers, getUser, registerUser, loginUser, updateUser} = require("../controllers/controllers.js");

// register new user
router.post('/register', registerUser);

// login user
router.post('/login', loginUser);

// list of all users
router.get('/users', getAllUsers);

// get user by id
router.get('/users/:id', getUser);

// update user info 
router.put('/users/:id', updateUser);

module.exports = {router};