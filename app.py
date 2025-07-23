from flask import Flask, render_template, request, redirect, url_for
from models import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def index():
    """Página principal: lista todas las tareas."""
    tasks = task_manager.list_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Agrega una nueva tarea."""
    title = request.form['title']
    task_manager.create_task(title)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    """Actualiza el estado de una tarea."""
    status = request.form['status']
    task_manager.update_task_status(task_id, status)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
