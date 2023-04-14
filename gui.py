from modules.functions import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
window = sg.Window('My To-do App', 
                   layout=[[label], [input_box, add_button], [exit_button]], 
                   font=("Helvetica", 20))
while True: 
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()