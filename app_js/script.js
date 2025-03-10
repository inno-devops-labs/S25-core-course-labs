let tasks = [];

function addTask() {
    const input = document.getElementById('task-input');
    const text = input.value.trim();
    
    if (text) {
        tasks.push({
            id: Date.now(),
            text: text,
            completed: false
        });
        input.value = '';
        renderTasks();
    }
}

function toggleTask(id) {
    tasks = tasks.map(task => 
        task.id === id ? {...task, completed: !task.completed} : task
    );
    renderTasks();
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    renderTasks();
}

function renderTasks() {
    const list = document.getElementById('tasks-list');
    list.innerHTML = tasks.map(task => `
        <div class="task ${task.completed ? 'completed' : ''}">
            <div>
                <input type="checkbox" 
                       ${task.completed ? 'checked' : ''} 
                       onclick="toggleTask(${task.id})">
                <span>${task.text}</span>
            </div>
            <button onclick="deleteTask(${task.id})">Delete</button>
        </div>
    `).join('');
}

// Добавляем обработчик Enter для input
document.getElementById('task-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask();
    }
});

// Начальный рендер
renderTasks();