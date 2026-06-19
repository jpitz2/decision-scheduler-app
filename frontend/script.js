// Test to make sure backend is reachable
fetch("/health")
    .then((res) => res.json())
    .then((data) => console.log("Backend says: ", data));

// TODO: fetch tasks from /tasks and render
async function loadTasks() {
    const response = await fetch("/tasks");
    const tasks = await response.json();
    
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";   // clears out anything currently there

    tasks.forEach((task)=> {
        const li = document.createElement("li");
        li.textContent = `${task.name} - ${task.priority}`;
        taskList.append(li)
    });
    // console.log(tasks);
}

loadTasks();

// TODO: handle form submissions to POST /tasks
const form = document.getElementById("task-form");

form.addEventListener("submit", async (event) => {
    event.preventDefault();   // stops page from refreshing on a submission

    const name = document.getElementById("task-name").value;
    const priority = document.getElementById("task-priority").value;
    const duration = document.getElementById("task-duration").value;

    fetch("/tasks", {
        method: "POST",   // HTTP method (POST request)
        headers: {"Content-Type": "application/json"},   // Data format being sent (JSON text)
        body: JSON.stringify({name: name, priority: priority, duration: duration})   // The data itself (converted into a JSON format --> body must be text, not a raw object)
    });

    await loadTasks();
    form.reset();
});