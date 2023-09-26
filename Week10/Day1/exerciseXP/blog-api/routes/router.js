const express = require('express');
const router = express.Router();
const {getAllPosts, getPost, createPost, updatePost, deletePost} = require("../controllers/controllers.js");

// list of all blog posts
router.get('/', getAllPosts);

// get blog post by id
router.get('/:id', getPost);

// create blog post
router.post('/', createPost);

// update blog post
router.put('/:id', updatePost);

// delete blog post
router.delete('/:id', deletePost);

module.exports = {router};