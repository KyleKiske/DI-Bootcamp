const fs = require('fs');
const bcrypt = require('bcrypt');
const express = require('express');
const router = express.Router();
const users = require('../users.json');
const {readJson, writeJson} = require("../fileHandler.js");


// Register
router.post('/register', readJson, (req, res, next) => {
    const {firstName, lastName, email, username, password} = req.body;
    if (!firstName || !lastName || !email || !username || !password) {
        return res.status(403).json({message : "Validation failed for new user"});
    }
    const usernameTaken = req.users.find((user) => user.username === username);
    if (usernameTaken) {
        return res.status(409).json({ message: 'Username already exists' });
    }
    const hashedPass = bcrypt.hashSync(password, 10);
    const user = {
        id : req.users.length+1,
        firstName : firstName,
        lastName : lastName,
        email : email,
        username : username,
        password : hashedPass
    };
    req.users.push(user);
    next();
}, writeJson, (req, res) => {
    res.redirect('login.html');
});

// Login
router.post("/login", readJson, (req, res) => {
    const {username, password} = req.body;
    const user = req.users.find((user) => user.username == username);
    if (!user) {
        res.status(404).send("User not found");
        return;
    }
    if (bcrypt.compareSync(password, user.password)) {
        return res.redirect("index.html");
    } else {
        return res.status(400).json({message: "Wrong password"});
    }
});

// Get all users
router.get('/users', readJson, (req, res) => {
    res.json(req.users)
});

// Get user by id
router.get('/users/:id', readJson, (req, res) => {
    const id = req.params.id;
    const user = req.users.find((user) => user.id == id);
    if (!user) {
        return res.status(404).json({message : "User not found"});
    }
    res.json(user).status(200);
});

// Update user by ID
router.put("/users/:id", readJson, (req, res, next) => {
    const id = req.params.id;
    const {firstName, lastName, email, username, password} = req.body;
    if (!firstName || !lastName || !email || !username || !password) {
        return res.status(403).json({message : "Validation failed for updating user"});
    }
    const index = users.findIndex((user) => user.id == id);
    if (index == -1) {
        res.status(404).send("User not found");
        return;
    }
    const hashedPass = bcrypt.hashSync(password, 10);
    req.users[index] = {
        ...req.users[index],
        firstName : firstName,
        lastName : lastName,
        email : email,
        username : username,
        password : hashedPass
    };
    next();
}, writeJson, (req, res) => {
    res.json(req.users);
})

module.exports = {router};