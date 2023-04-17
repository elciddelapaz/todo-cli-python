from modules.functions import get_todos, write_todos
import PySimpleGUI as sg
from time import strftime
sg.theme("Black")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
list_box = sg.Listbox(values=get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
window = sg.Window('My To-do App', 
                   layout=[[clock],[label], [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=("Helvetica", 20))
while True: 
    event, values = window.read(timeout=10)
    window['clock'].update(value=strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo = values['todos'][0]
                todos = get_todos()
                todos.remove(todo)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()