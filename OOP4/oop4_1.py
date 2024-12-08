import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Combo Box Example")
    window.setGeometry(100, 100, 400, 200) 

    layout = QVBoxLayout()
    country = {'Германия': 'Федеративная Республика Германия', 'Россия': 'Российская Федерация',
               'Китай': 'Китайская Народная Республика', 'Беларусь': 'Республика Беларусь',
               'Австралия': 'Австралийский Союз'}

    combo_box = QComboBox(window)
    combo_box.addItems(country.keys())
    layout.addWidget(combo_box)
    
    label = QLabel(window)
    layout.addWidget(label)

    def update_label():
        selected_item = combo_box.currentText()
        label.setText("Официальное название: " + country[selected_item])

    combo_box.currentIndexChanged.connect(update_label)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
