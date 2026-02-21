console.log("js connected");

let nameElement = document.querySelector(".js-name-input");
let dateElement = document.querySelector(".js-date-input");
let gridElement = document.querySelector(".list-grid");

// LOAD TASKS
function loadTasks() {
  console.log("show clicked");

  gridElement.innerHTML = "<p class='loader'></p>";
  fetch("https://fullstack-todo-app-itpx.onrender.com/tasks")
    .then(function (res) {
      console.log("fetch response received");
      return res.json();
    })
    .then(function (tasks) {
      console.log("data: ", tasks);
      renderTasks(tasks);
    });
}

// CREATE TASK
function createTask() {
  console.log("create clicked");
  console.log(nameElement.value, dateElement.value);
  fetch("https://fullstack-todo-app-itpx.onrender.com/tasks", {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      name: nameElement.value,
      date: dateElement.value,
      mark: true,
    }),
  })
    .then(function (res) {
      console.log("POST status:", res.status);
      if (!res.ok) {
        throw new Error("Create failed");
      }
      return res.json();
    })
    .then(function () {
      nameElement.value = "";
      dateElement.value = "";
      loadTasks();
    });
}

// DELETE TASK
function deleteTask(id) {
  console.log("delete clicked");
  fetch("https://fullstack-todo-app-itpx.onrender.com/tasks/" + id, {
    method: "DELETE",
  })
    .then(function (res) {
      if (!res.ok) {
        throw new Error("Delete failed");
      }
      return res.json();
    })
    .then(function () {
      loadTasks();
    })
    .catch(function (err) {
      console.error(err);
    });
}

// RENDER TASKS
function renderTasks(tasks) {
  console.log("render called", tasks);
  let html = "";
  if (tasks.length === 0) {
    gridElement.innerHTML = "<p class='loading-text'>No tasks yet</p>";
    return;
  }
  for (let i = 0; i < tasks.length; i++) {
    let task = tasks[i];

    html += `
      <div class="task-row">

        <div class="name-div">
          <p>${task.name}</p>
        </div>

        <div class="date-div">
          <p>${task.date}</p>
        </div>

        <div class="buttons-div">
          <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
        </div>

      </div>
    `;
  }

  gridElement.innerHTML = html;
}

// LOAD ON START
loadTasks();
