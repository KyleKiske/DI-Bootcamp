import express from 'express';
import { fetchPosts } from './data/dataService.js';

const app = express();
app.use(express.json());

app.listen(5000, () => {
    console.log("server is listening on port 5000");
});

app.get("/api/palceholder", async (req,res) => {
    const data = await fetchPosts();
    res.status(200).json(data);
    console.log('Data has been successfully retrieved and sent as a response.');
})