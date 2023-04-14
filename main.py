from modules.functions import get_todos, write_todos
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n') 
        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        for i, j in enumerate(todos):
                j = j.strip('\n')
                print(f"{i+1}-{j}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos()
            new_todo = input("New todo: ")
            todos[number - 1] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue             
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            write_todos(todos)
            print(f"Removed '{todo_to_remove}'")
        except IndexError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("exit"): 
        break
    else:
        print("Command is not valid")