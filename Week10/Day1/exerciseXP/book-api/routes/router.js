const express = require('express');
const router = express.Router();
const {getAllBooks, getBook, createBook, updateBook, deleteBook} = require("../controllers/controllers.js");

// list of all blog posts
router.get('/', getAllBooks);

// get blog post by id
router.get('/:id', getBook);

// create blog post
router.post('/', createBook);

// update blog post
router.put('/:id', updateBook);

// delete blog post
router.delete('/:id', deleteBook);

module.exports = {router};