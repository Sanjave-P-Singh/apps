# FrontEnd
import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

Label1 = sg.Text("Selective archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key='archive')

Label2 = sg.Text("Selective des dir: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor", layout=[[Label1, input1, choose_button1],
                                                [Label2, input2, choose_button2],
                                                [extract_button, output_label]])

while True:
    event,values = window.read()
    print(event , values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed")

window.close()

