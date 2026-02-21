let nameElement = document.querySelector(".js-name-input");
let dateElement = document.querySelector("js-date-input");

function loadTasks() {
  fetch("http://127.0.0.1:8000/tasks")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      renderTasks(data);
    })
    .catch(function (error) {
      console.error("Error fetching tasks:", error);
    });
}

function createTask(name, date, mark) {
  fetch("http://127.0.0.1:8000/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name,
      date: date,
      mark: mark,
    }),
  })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Failed to create task");
      }
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      loadTasks();
    })
    .catch(function (error) {
      console.error("Error:", error);
    });
}

function deleteTask(id) {
  fetch("http://127.0.0.1:8000/tasks/" + id, {
    method: "DELETE",
  })
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Delete failed");
      }
      loadTasks();
    })
    .catch(function (error) {
      console.error("Error:", error);
    });
}

function displayTasks() {
  let results = loadTasks();
  let displayHTML = "";
  for (task = 0; task < results.length; task++) {
    displayHTML =
      displayHTML +
      `<p>${task.name}</p>
        </div>
        <div class="active-div">
            <p>${task.is_critical}</p>
        </div>
        <div class="date-div">
            <p>${task.date}</p>
        </div>
        <div class="buttons-div">
            <button class="mark-btn">Mark</button>
            <button class="delete-btn">Delete</button>
        </div>`;
  }
}
