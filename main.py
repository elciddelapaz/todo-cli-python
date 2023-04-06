while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    match user_action.strip():
        case 'add':
            todo = input("Enter to do: ") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            for i, j in enumerate(todos):
                j = j.strip('\n')
                print(f"{i+1}-{j}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            new_todo = input("New todo: ")
            todos[number - 1] = new_todo + "\n"
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
            print(f"Removed '{todo_to_remove}'")
        case 'exit':
            break
        case _:
            print("Add, show, or exit only!")