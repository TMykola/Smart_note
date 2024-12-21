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

def show_tag(name_note):
    tag_list_widget.clear()
    tag_list_widget.addItems(data[name_note]["TAG"])

def add_note():
    name_note = QInputDialog().getText(QInputDialog(), "Назва нотатка:", "Введіть назву нотатка:")[0]
    data[name_note] = {"TEXT": "", "TAG": []}
    write_json(name_file, data)
    note_list_widget.addItem(name_note)

def add_tag():
    try:
        name_note = note_list_widget.currentItem().text()
        name_tag = QInputDialog().getText(QInputDialog(), "Введення тега:", "Введіть назву тега:")[0]
        data[name_note]["TAG"].append(name_tag)
        write_json(name_file, data)
        tag_list_widget.addItem(name_tag)
    except:
        error("Щоб створити тег, спочатку виберіть нотаток")
        
def remove_tag():
    try:
        name_note = note_list_widget.currentItem().text()
        name_tag = tag_list_widget.currentItem().text()
        data[name_note]["TAG"].remove(name_tag)
        write_json(name_file, data)
        tag_list_widget.clear()
        show_tag(name_note)
    except:
        error("Щоб видаляти тег, спочатку виберіт нотаток а потім тег")

def searching_tag():
    try:
        stag = searching_tag_input.text()
        keys = list(data.keys())
        result = list()
        for key in keys:
            for TAG in data[key]["TAG"]: 
                if TAG == stag:
                    result.append(key)
        note_list_widget.clear()
        note_list_widget.addItems(result)
        write_json(name_file, data)
    except:
        error("Щоб знайти, спочатку напишіть назву тега")
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
    text_edit.setDisabled(False)
    show_tag(name_note)

def remove_note():
    try:
        name_note = note_list_widget.currentItem().text()
        del data[name_note]
        write_json(name_file, data)
        note_list_widget.clear()
        show_note()
        text_edit.setPlainText("")
        text_edit.setDisabled(True)
    except:
        error("Щоб видалити, спочатку виберіть нотаток!")

search_tag.clicked.connect(searching_tag)
delete_tag.clicked.connect(remove_tag)
create_tag.clicked.connect(add_tag)
delete_note.clicked.connect(remove_note)
create_note.clicked.connect(add_note)
save_note.clicked.connect(save_file)
note_list_widget.clicked.connect(show_text)
tag_list_widget.clicked.connect(show_text)

show_note()
app.exec_()
