const express = require('express');
const router = express.Router();

// Sample in-memory database for storing to-do items
const todos = [];

// Get all to-do items
router.get('/', (req, res) => {
    res.json(todos);
});

// Add a new to-do item
router.post('/', (req, res) => {
    const name = req.body.name;
    const endTime = req.body.endTime;
    const Task = {
        id : todos.length+1,
        name : name,
        endTime : endTime
    };
    todos.push(Task);
    res.json(todos);
});

// Update a to-do item by ID
router.put("/:id", (req, res) => {
    const id = req.params.id;
    const name = req.body.name;
    const endTime = req.body.endTime;
    const index = todos.findIndex((task) => task.id == id);
    todos[index] = {
        ...todos[index],
        name : name,
        endTime : endTime
    };
    res.json(todos);
});

// Delete a to-do item by ID
router.delete("/:id", (req, res) => {
    const id = req.params.id;
    const index = todos.findIndex((task) => task.id == id);
    todos.splice(index,1);
    res.json(todos);
})

module.exports = {router};