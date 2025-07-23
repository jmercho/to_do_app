# Gestor de Tareas Pendientes

Esta es una aplicación web desarrollada en Python usando Flask para gestionar tareas pendientes. Permite crear, listar y marcar tareas con los siguientes estados: Completada, Documentada, Revisada por pares y Automatizada.

## Características
- Crear tareas
- Listar tareas
- Marcar tareas con diferentes estados

## Instalación
1. Asegúrate de tener Python 3.8+ instalado.
2. Instala las dependencias:
   ```bash
   pip install flask
   ```
3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
4. Accede a `http://127.0.0.1:5000` en tu navegador.

## Estructura del Proyecto
- `app.py`: Punto de entrada de la aplicación Flask.
- `models.py`: Definición de la clase Task y lógica de negocio.
- `templates/`: Archivos HTML para la interfaz de usuario.
- `static/`: Archivos estáticos (CSS, JS, imágenes).

## Buenas Prácticas
- El código sigue los principios SOLID.
- Documentación mediante docstrings y este README.

## Licencia
MIT
