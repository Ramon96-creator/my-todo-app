# Unchanged backend from Section 15. The GUI frontend below uses these
# same functions.
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(BASE_DIR, "todos.txt")


def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    # Si el archivo no existe en el contenedor (ej. en el servidor de Streamlit), lo crea vacío
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass

    with open(file_path, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list to a text file. """
    with open(file_path, "w") as file:
        file.writelines(todos_arg)
