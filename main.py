import math
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)

        self.setWindowTitle('Сложные табличные вычисления в Python')

        self.setWindowIcon(QtGui.QIcon('images/1.png'))
        self.label_img.setPixmap(QPixmap('images/imagel.png'))

        self.rndm_Btn.clicked.connect(self.fill_random_numbers)
        self.clear_Btn.clicked.connect(self.clear)
        self.exit_Btn.clicked.connect(self.close)
        self.calc_Btn.clicked.connect(self.solve)

    def fill_random_numbers(self):
        i = 0
        while i < self.tableWidget.rowCount():
            random_num = randint(-33, 99)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1

    def solve(self):
        Calc.solve(self)

    def clear(self):
        self.tableWidget.clearContents()

class Calc(Main):
    def __init__(self):
        pass

    def solve(self):
        if validation_of_data(self.tableWidget):
            i = 0
            j = 1
            sum1 = 0
            sum2 = 0
            proiz = 1

            while i < self.tableWidget.rowCount():
                item = int(self.tableWidget.item(i, 0).text())
                if i == 0:
                    self.tableWidget.setItem(i, j, QTableWidgetItem('none'))
                    i += 1
                    continue
                else:
                    item1 = int(self.tableWidget.item(i - 1, 0).text())
                if item > 0:
                    sum1 += item
                else:
                    proiz *= item
                sum2 += item1
                val = (math.sqrt(sum1) + (math.factorial(i) / 2)) / (proiz - sum2)
                try:
                    val = format(val, '.3f')
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                except Exception:
                    self.tableWidget.setItem(i, j, QTableWidgetItem('none'))
                i += 1
        else:
            QMessageBox.critical(self, "Ошибка ", "Таблица пуста", QMessageBox.Ok)


def validation_of_data(table_widget):
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False
    return True



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()