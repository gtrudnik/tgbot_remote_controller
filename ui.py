from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import QtCore

import sys


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 700, 500)
        self.setWindowTitle("Session1")

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 600, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.table_Columns_size = 0
        self.table_Rows_size = 0

        self.info_output(["1столбец","2столбец","3столбец"], [[2,4,5],[0,0,0]])
        # print(self.read_table())

    def info_output(self, names, data):
        """Вывод информации в таблицу"""
        self.tableWidget.clear()
        self.table_Columns_size = len(names)
        self.tableWidget.setColumnCount(self.table_Columns_size)

        # названия столбцов
        for i in range(self.table_Columns_size):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(names[i]))

        # заполнение строк таблицы
        i = 1
        for items in data:
            self.tableWidget.setRowCount(i)
            for j in range(len(items)):
                itm = QTableWidgetItem(f'{items[j]}')
                itm.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i - 1, j, itm)
            i += 1

        self.tableWidget.resizeColumnsToContents()
        self.table_Rows_size = i - 1

    def read_table(self):
        """ эта функция возвращает данные таблицы
            список состоит из списков,  вот так:
            [["комплектющее", "серийный номер", "количество"]]"""

        info_table = []

        for i in range(self.table_Rows_size):
            a = []
            for j in range(self.table_Columns_size):
                a.append(self.tableWidget.item(i, j).text())
            info_table.append(a)
        return info_table


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = UiMainWindow()
    MainWindow.show()
    sys.exit(app.exec())
