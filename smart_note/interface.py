from PyQt5.QtWidgets import (QTextEdit, QListWidget, QLineEdit,QApplication,QWidget,
    QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QInputDialog, QMessageBox
)
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setFixedSize(700,600)
window.setWindowTitle("SMART NOTE")

create_note = QPushButton("Створити замітку")
save_note = QPushButton("Зберегти замітку")
delete_note = QPushButton("Видалити замітку")
create_tag = QPushButton("Створити тег")
delete_tag = QPushButton("Видалити тег")
search_tag = QPushButton("Пошук по тегу")
label_note = QLabel("Список заміток")
label_tag = QLabel("Список тегів")
note_list_widget = QListWidget("")
tag_list_widget = QListWidget("")
searching_tag_input = QInputDialog("Введіть тег") 
text_edit = QTextEdit("")

layout = QHBoxLayout()

layout2 = QHBoxLayout()

main_layout = QHBoxLayout()

panel_layout = QVBoxLayout()

layout1








window.show()
app.exec_()