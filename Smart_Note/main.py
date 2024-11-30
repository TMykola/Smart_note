from interface import *
from create_json import *
name_file = "data.json"
try:
    data = read_json(name_file)
except:
    data = dict()

def error(text):
    ms = QMessageBox()
    ms.setText(text)
    ms.exec_()

def show_note():
    note_list_widget.addItems(list(data.keys()))


def add_note():
    name_note = QInputDialog().getText(QInputDialog(), "Назва нотатка:", "Введіть назву нотатка:")[0]
    data[name_note] = {"TEXT": "", "TAG": {}}
    write_json(name_file, data)
    note_list_widget.addItem(name_note)

def save_file():
    try:
        name_note = note_list_widget.currentItem().text()
        data[name_note]["TEXT"] = text_edit.toPlainText()
        write_json(name_file, data)
    except:
        error("Щоб зберегти, спочатку виберіть нотаток!")

def show_text():
    name_note = note_list_widget.currentItem().text()
    text_edit.setPlainText(data[name_note]["TEXT"])

def remove_note():
    try:
        name_note = note_list_widget.currentItem().text()
        del data[name_note]
    except:
        error("Щоб видалити, спочатку виберіть нотаток!")


delete_note.clicked.connect(remove_note)
create_note.clicked.connect(add_note)
save_note.clicked.connect(save_file)
note_list_widget.clicked.connect(show_text)

show_note()
app.exec_()
