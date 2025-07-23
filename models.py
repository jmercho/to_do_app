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

    def update_status(self, new_status: str) -> bool:
        """
        Actualiza el estado de la tarea.
        :param new_status: Nuevo estado a asignar.
        :return: True si el estado es válido y se actualizó, False si no.
        """
        if new_status in self.STATUS_OPTIONS:
            self.status = new_status
            return True
        return False

class TaskManager:
    """
    Gestiona la colección de tareas.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def create_task(self, title: str) -> bool:
        """
        Crea una nueva tarea y la agrega a la lista si el título es válido y no está duplicado.
        :param title: Título de la tarea.
        :return: True si la tarea fue creada, False si no.
        """
        title = title.strip()
        if not title:
            return False
        if any(task.title.lower() == title.lower() for task in self.tasks):
            return False
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return True

    def list_tasks(self) -> List[Task]:
        """
        Devuelve la lista de tareas.
        :return: Lista de objetos Task.
        """
        return self.tasks

    def update_task_status(self, task_id: int, status: str) -> bool:
        """
        Actualiza el estado de una tarea por su ID.
        :param task_id: ID de la tarea.
        :param status: Nuevo estado.
        :return: True si se actualizó, False si no.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task.update_status(status)
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Elimina una tarea por su ID.
        :param task_id: ID de la tarea.
        :return: True si la tarea fue eliminada, False si no.
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False
