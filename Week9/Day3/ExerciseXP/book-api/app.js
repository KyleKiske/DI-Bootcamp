import express from 'express';

const app = express();
app.use(express.json());

let data = [
    {id : 1,
    title : "The Industrial Society and it's future",
    author : "Ted Kaczynski",
    publishedYear: 1995
    },
    {id : 2,
    title : '1984',
    author : 'George Orwell',
    publishedYear: 1948
    },
    {id : 3,
    title : 'book',
    author : 'Author',
    publishedYear: 2003
    }
];

app.listen(5000, () => {
    console.log("server is listening on port 5000");
});

app.route('/api/books').get((req, res) => {
    res.json(data);
}).post((req, res) => {
    const newBook = {
        id: data.length + 1,
        title: req.body.title,
        author: req.body.author,
        publishedYear: req.body.publishedYear
      };
      data.push(newBook);
      res.status(201).json(newBook);
}).get((req, res) =>
    res.json(data));

app.route('/api/books/:bookID').get((req, res) => {
    const id = Number(req.params.bookID);
    const book = data.find((book) => book.id === id);
    
    if (!book) {
        return res.status(404).send("Book not found");
    }
    res.json(book);
})