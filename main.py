while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    match user_action.strip():
        case 'add':
            todo = input("Enter to do: ") + '\n'
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('todos.txt', 'w') 
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for i, j in enumerate(todos):
                j = j.strip('\n')
                print(f"{i+1}-{j}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            todos[number - 1] = input("New todo: ")
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Add, show, or exit only!")