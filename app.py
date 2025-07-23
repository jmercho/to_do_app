from flask import Flask, render_template, request, redirect, url_for
from models import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def index():
    """Página principal: lista todas las tareas."""
    tasks = task_manager.list_tasks()
    message = request.args.get('message', '')
    return render_template('index.html', tasks=tasks, message=message)

@app.route('/add', methods=['POST'])
def add_task():
    """Agrega una nueva tarea."""
    title = request.form['title']
    if not task_manager.create_task(title):
        return redirect(url_for('index', message='Título vacío o duplicado.'))
    return redirect(url_for('index', message='Tarea agregada correctamente.'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    """Actualiza el estado de una tarea."""
    status = request.form['status']
    if not task_manager.update_task_status(task_id, status):
        return redirect(url_for('index', message='No se pudo actualizar la tarea.'))
    return redirect(url_for('index', message='Tarea actualizada correctamente.'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Elimina una tarea."""
    if task_manager.delete_task(task_id):
        return redirect(url_for('index', message='Tarea eliminada correctamente.'))
    return redirect(url_for('index', message='No se encontró la tarea.'))

if __name__ == '__main__':
    app.run(debug=True)
