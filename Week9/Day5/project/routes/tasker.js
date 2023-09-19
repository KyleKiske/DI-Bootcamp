const fs = require('fs');
const express = require('express');
const router = express.Router();
const tasks = require('../tasks.json');
const {readJson, writeJson} = require("../fileHandler.js");

// Get all tasks
router.get('/', readJson, (req, res) => {
    res.json(req.tasks)
});

// Get task by id
router.get('/:id', readJson, (req, res) => {
    const id = req.params.id;
    const task = req.tasks.find((task) => task.id == id);
    if (!task) {
        return res.status(404).json({message : "Task not found"});
    }
    res.json(task).status(200);
});

// Add a new task
router.post('/', readJson, (req, res, next) => {
    const {title, timeframe} = req.body;
    if (!title || !timeframe) {
        return res.status(403).json({message : "Validation failed for new task"});
    }
    const Task = {
        id : req.tasks.length+1,
        title : title,
        timeframe : timeframe
    };
    req.tasks.push(Task);
    next();
}, writeJson, (req, res) => {
    res.json(req.tasks);
});

// Update a task by ID
router.put("/:id", readJson, (req, res, next) => {
    const id = req.params.id;
    const {title, timeframe} = req.body;
    const index = tasks.findIndex((task) => task.id == id);
    if (index == -1) {
        res.status(404).send("Task not found");
        return;
    }
    tasks[index] = {
        ...tasks[index],
        title : title,
        timeframe : timeframe
    };
    next();
}, writeJson, (req, res) => {
    res.json(req.tasks);
});

// Delete a task by ID
router.delete("/:id", readJson, (req, res, next) => {
    const id = req.params.id;
    const index = tasks.findIndex((task) => task.id == id);
    if (index == -1) {
        res.status(404).send("Task not found");
        return;
    }
    req.tasks.splice(index,1);
    next();
}, writeJson, (req, res) => {
    res.json(req.tasks);
})

module.exports = {router};