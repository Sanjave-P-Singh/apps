import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue8")

clock = sg.Text('', key='clock', font=("Times New Roman", "15"))
label = sg.Text("Type in a to-do: ", font=("Times New Roman", "15"))
input_box = sg.InputText(tooltip="Enter a todo", key="todo", font=("Times New Roman", "15"))
# add_button = sg.Button("Add",size = 10, font=("Times New Roman", "15"))
add_button = sg.Button(size = 2, image_source="add.png", mouseover_colors="LightBlue2",
                     tooltip="Add todo", key="Add")
edit_button = sg.Button("Edit", font=("Times New Roman", "15"))
# edit_button = sg.Button(size=4, image_source="edit.png", mouseover_colors="LightBlue2",
#                    tooltip="edit todo", key="Edit")
complete_button = sg.Button("Complete", font=("Times New Roman", "15"))
# complete_button = sg.Button(size=1, image_source="delete.png", mouseover_colors="LightBlue2",
#                    tooltip="complete todo", key="Complete")
exit_button = sg.Button("Exit", font=("Times New Roman", "15"))
# exit_button = sg.Button(size=1, image_source="exit.png", mouseover_colors="LightBlue2",
#                    tooltip="exit todo", key="Exit")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10], font=("Times New Roman", "15"))


window = sg.Window('My To-Do List Application',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Times New Roman', 15))
while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Times New Roman", "15"))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Times New Roman", "15"))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
