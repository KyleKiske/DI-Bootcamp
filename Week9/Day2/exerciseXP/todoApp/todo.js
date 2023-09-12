class Task {
    constructor(name, status) {
        this.name = name;
        this.status = status;
    }
}

class TodoList {
    listTasks = [];

    addTasks(taskName, taskStatus) {
        const newTask = new Task(taskName, taskStatus);
        this.listTasks.push(newTask);
    };

    markComplete(taskName) {
        const foundTask = this.listTasks.find((task) => task.name == taskName);
        foundTask.status = 'complete';
    };

    listAllTasks() {
        this.listTasks.forEach(element => {
            console.log(element);
        });
    };
}

export default TodoList; 