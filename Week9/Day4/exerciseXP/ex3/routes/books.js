const express = require('express');
const router = express.Router();

// Sample in-memory database for storing books
const books = [];

// Get all books
router.get('/', (req, res) => {
    res.json(books);
});

// Add a new book
router.post('/', (req, res) => {
    const {title, author} = req.body;
    const Book = {
        id : books.length+1,
        title : title,
        author : author
    };
    books.push(Book);
    res.json(books);
});

// Update a book by ID
router.put("/:id", (req, res) => {
    const id = req.params.id;
    const {title, author} = req.body;
    const index = books.findIndex((book) => book.id == id);
    if (index == -1) {
        res.status(404).send("no index found");
        return;
    }
    books[index] = {
        ...books[index],
        title : title,
        author : author
    };
    res.json(books);
});

// Delete a book by ID
router.delete("/:id", (req, res) => {
    const id = req.params.id;
    const index = books.findIndex((book) => book.id == id);
    if (index == -1) {
        res.status(404).send("no index found");
        return;
    }
    books.splice(index,1);
    res.json(books);
})

module.exports = {router};