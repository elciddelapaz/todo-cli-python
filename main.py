todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    match user_action.strip():
        case 'add':
            todo = input("Enter to do: ")
            todos.append(todo)
        case 'show':
            for i, item in enumerate(todos):
                print(f"{i+1}-{item}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            todos[number - 1] = input("New todo: ")
        case 'exit':
            break
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case _:
            print("Add, show, or exit only!")