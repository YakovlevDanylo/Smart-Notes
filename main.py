import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QHBoxLayout, \
    QVBoxLayout

notes = {
    "Ласкаво просимо!": {
        "текст": "Вітаю вас у нашому додатку",
        "теги": ["Вітання", "Привіт"]
    },
    "Домашка": {
        "текст": "Треба зробити домашку до понеділка",
        "теги": ["Хімія", "Математика"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Розумні замітки")
window.resize(900,600)

list_notes = QListWidget()
list_notes_label = QLabel("Список заміток")

button_note_create = QPushButton("Створити замітку")
button_note_del = QPushButton("Видалити замітку")
button_note_save = QPushButton("Зберегти замітку")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введіть тег...")
field_text = QTextEdit()
list_tags = QListWidget()
list_tags_label = QLabel("Список тегів")
button_tag_add = QPushButton("Додати до замітки")
button_tag_del = QPushButton("Відкріпити від замітки")
button_tag_search = QPushButton("Шукати замітки по тегу")

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(field_text)

col2 = QVBoxLayout()
col2.addWidget(list_notes_label)
col2.addWidget(list_notes)
row1 = QHBoxLayout()
row1.addWidget(button_note_create)
row1.addWidget(button_note_del)
row2 = QHBoxLayout()
row2.addWidget(button_note_save)
col2.addLayout(row1)
col2.addLayout(row2)

col2.addWidget(list_tags_label)
col2.addWidget(list_tags)
col2.addWidget(field_tag)
row3 = QHBoxLayout()
row3.addWidget(button_tag_add)
row3.addWidget(button_tag_del)
row4 = QHBoxLayout()
row4.addWidget(button_note_save)

col2.addLayout(row3)
col2.addLayout(row4)

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)
window.setLayout(layout_notes)

def show_notes():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

list_notes.itemClicked.connect(show_notes)

list_notes.addItems(notes)

window.show()
app.exec_()
