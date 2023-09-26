const { db } = require("../config/db.js");

const _getAllBooks = () => {
    return db("books").select("id", "title", "author", "publishedYear");
};

const _getBookById = (id) => {
    return db("books").select("id", "title", "author", "publishedYear").where({ id: id });
};


const _insertBook = ({ title, author, publishedYear}) => {
    return db("books").insert({ title, author, publishedYear }, ['*']);
};

const _updateBook = ({ title, author, publishedYear }, id) => {
    return db("books")
        .update({ title, author, publishedYear })
        .where({ id : id })
        .returning(["id", "title", "author", "publishedYear"]);
};

const _deleteBook = (id) => {
    return db("books").where({id : id}).del().returning(['*']);
};

module.exports = {
    _getAllBooks,
    _getBookById,
    _insertBook,
    _updateBook,
    _deleteBook
};