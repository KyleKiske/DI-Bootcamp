const { db } = require("../config/db.js");

const _getAllPosts = () => {
    return db("posts").select("id", "title", "content");
};

const _getPostById = (id) => {
    return db("posts").select("id", "title", "content").where({ id: id });
};


const _insertPost = ({ title, content }) => {
    return db("posts").insert({ title, content }, ['*']);
};

const _updatePost = ({ title, content }, id) => {
    return db("posts")
        .update({ title, content })
        .where({ id : id })
        .returning(["id", "title", "content"]);
};

const _deletePost = (id) => {
    return db("posts").where({id : id}).del().returning(['*']);
};

module.exports = {
    _getAllPosts,
    _getPostById,
    _insertPost,
    _updatePost,
    _deletePost
};