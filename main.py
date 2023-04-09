while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:
        todo = user_action[4:]
        # todo = input("Enter to do: ") + '\n'
        with open('todos.txt', 'r') as file:
                todos = file.readlines()
        todos.append(todo) 
        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        for i, j in enumerate(todos):
                j = j.strip('\n')
                print(f"{i+1}-{j}")
    elif 'edit' in user_action:
        number = int(user_action[5:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("New todo: ")
        todos[number - 1] = new_todo + "\n"
        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number - 1)
        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)
        print(f"Removed '{todo_to_remove}'")
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")