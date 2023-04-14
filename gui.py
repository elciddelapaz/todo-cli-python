from modules.functions import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
list_box = sg.Listbox(values=get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
window = sg.Window('My To-do App', 
                   layout=[[label], [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=("Helvetica", 20))
while True: 
    event, values = window.read()
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo = values['todos'][0]
            todos = get_todos()
            todos.remove(todo)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()