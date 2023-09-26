const { db } = require("../config/db.js");
const bcrypt = require('bcrypt');
// const knex = require('knex');

const _getAllUsers = () => {
    return db("users").select("id", "email", "username", "first_name", "last_name");
};

const _getUserById = (id) => {
    return db("users").select("id", "email", "username", "first_name", "last_name").where({ id });
};


const _registerUser = ({email, username, first_name, last_name, password}) => {
    const hashedPass = bcrypt.hashSync(password, 10);
    db.transaction(trx => {
        return trx('users').insert({email, username, first_name, last_name}).then(() => {
            return trx('hashpwd').insert({username, password: hashedPass});
        });
    }).then(() => {
        console.log('inserted 2 rows');
    }).catch(err => {
        console.log(err);
        console.log('one of the queries failed, transction rollback');
    });
    // return db("users").insert({email, username, first_name, last_name, password: hashedPass}, ["id", "email", "username", "first_name", "last_name"]);
};

const _loginUser = (username, password) => {
    const hashedPass = bcrypt.hashSync(password, 10);
    return db('users')
    .join('hashpwd', 'users.username', '=', 'hashpwd.username')
    .select("users.username", "hashpwd.password")
    .where('users.username', username);
    // return db("users").where({username : username})..returning(['*']);
};

const _updateUser = ({email, username, first_name, last_name}, id) => {
    return db("users")
        .update({email, username, first_name, last_name})
        .where({ id : id })
        .returning(["id", "email", "username", "first_name", "last_name"]);
};


module.exports = {
    _getAllUsers,
    _getUserById,
    _registerUser,
    _loginUser,
    _updateUser
};