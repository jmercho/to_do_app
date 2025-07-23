from typing import List

class Task:
    """
    Representa una tarea pendiente.
    """
    STATUS_OPTIONS = [
        'Pendiente',
        'Completada',
        'Documentada',
        'Revisada por pares',
        'Automatizada'
    ]

    def __init__(self, id: int, title: str, status: str = 'Pendiente'):
        """
        Inicializa una nueva tarea.
        :param id: Identificador único de la tarea.
        :param title: Título de la tarea.
        :param status: Estado de la tarea.
        """
        self.id = id
        self.title = title
        self.status = status

    def update_status(self, new_status: str):
        """
        Actualiza el estado de la tarea.
        :param new_status: Nuevo estado a asignar.
        """
        if new_status in self.STATUS_OPTIONS:
            self.status = new_status

class TaskManager:
    """
    Gestiona la colección de tareas.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def create_task(self, title: str):
        """
        Crea una nueva tarea y la agrega a la lista.
        :param title: Título de la tarea.
        """
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1

    def list_tasks(self) -> List[Task]:
        """
        Devuelve la lista de tareas.
        :return: Lista de objetos Task.
        """
        return self.tasks

    def update_task_status(self, task_id: int, status: str):
        """
        Actualiza el estado de una tarea por su ID.
        :param task_id: ID de la tarea.
        :param status: Nuevo estado.
        """
        for task in self.tasks:
            if task.id == task_id:
                task.update_status(status)
                break
