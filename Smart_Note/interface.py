from PyQt5.QtWidgets import (QTextEdit, QListWidget, QLineEdit,QApplication,QWidget,
    QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QInputDialog, QMessageBox, QSizePolicy
)
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setFixedSize(700,600)
window.setWindowTitle("Розумні замітки")

create_note = QPushButton("Створити замітку")
save_note = QPushButton("Зберегти замітку")
delete_note = QPushButton("Видалити замітку")
create_tag = QPushButton("Додати до замітки")
delete_tag = QPushButton("Відкріпити від замітки")
search_tag = QPushButton("Шукати замітку по тегу")
label_note = QLabel("Список заміток")
label_tag = QLabel("Список тегів")
note_list_widget = QListWidget()
tag_list_widget = QListWidget()
searching_tag_input = QLineEdit() 
text_edit = QTextEdit()

main_layout = QHBoxLayout()


layout1 = QHBoxLayout()
layout2 = QHBoxLayout()

panel_layout = QVBoxLayout()

main_layout.addWidget (text_edit)
main_layout.addLayout(panel_layout)

panel_layout.addWidget (label_note)
panel_layout.addWidget (note_list_widget)
layout1.addWidget (create_note)
layout1.addWidget (delete_note)
panel_layout.addLayout(layout1)
panel_layout.addWidget (save_note)
panel_layout.addWidget (label_tag)
panel_layout.addWidget (tag_list_widget)
panel_layout.addWidget (searching_tag_input)
layout2.addWidget (create_tag)
layout2.addWidget (delete_tag)
panel_layout.addLayout(layout2)
panel_layout.addWidget (search_tag)

text_edit.setFixedSize(400,577)
window.setLayout (main_layout)



window.show()
app.exec_()