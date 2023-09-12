import TodoList from "./todo.js";

const theList = new TodoList();

theList.addTasks("First", 'pending');
theList.addTasks("Second", 'in progress');
theList.addTasks("Third", 'declined');

theList.markComplete("First");
theList.markComplete("Second");

theList.listAllTasks();