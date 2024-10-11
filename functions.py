FILEPATH = "todos.txt"

# Custom functions are defined outside the code or the loop. They begin with the "def" keyword
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items
    The function is making use of default arguments, like filepath getting assigned up there
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__Main__":
    print("Hello")
    print(get_todos())
