import express from 'express';
import mogoose from 'mongoose';
import { Todo } from './models/Todo.js';

let conn = await mogoose.connect("mongodb://localhost:27017/todo");

const app = express();
const port = 3000;

app.get('/', (req, res) => {
    const todo = new Todo({ title: "Bonjour! ce d'abord Todo", desc: "ce d'abord Todo", isDone: 1 })
    todo.save();
    res.send('Hello World!');
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});