const express = require('express');
const app = express();
app.use(express.json());

let data = [
    {id : 1,
        title : 'first',
        content : 'the content'},
    {id : 2,
        title : 'second',
        content : 'the text'},
    {id : 3,
        title : 'third',
        content : 'the analysis'}
];

app.listen(3000, () => {
    console.log("server is listening on port 3000");
});

app.route('/posts').get((req, res) => {
    res.json(data);
}).post((req, res) => {
    const newPost = {
        id: data.length + 1,
        title: req.body.title,
        content: req.body.content,
      };
      data.push(newPost);
      res.status(201).json(newPost);
}).get((req, res) =>
    res.json(data));

app.route('/posts/:postID').get((req, res) => {
    const id = Number(req.params.postID);
    const post = data.find((post) => post.id === id);
  
    if (!post) {
        return res.status(404).send("Post not found");
    }
    res.json(post);
}).put((req, res) => {
    const id = Number(req.params.postID);
    const index = data.findIndex((post) => post.id === id);
    if (index === -1) {
      return res.status(404).send("Post not found");
    }
    const updatedPost = {
      id: data[index].id,
      title: req.body.title,
      content: req.body.content,
    };
    data[index] = updatedPost;
    res.status(200).json("Post updated");
}).delete((req,res) => {
    const id = Number(req.params.postID);
  const index = data.findIndex((post) => post.id === id);
  if (index === -1) {
    return res.status(404).send("Post not found");
  }
  data.splice(index, 1);
  res.status(200).json("Post deleted");
});

