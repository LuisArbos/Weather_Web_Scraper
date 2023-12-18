from tabulate import tabulate

def print_table_info(data):
    sorted_data = sorted(data, key=lambda x: x['city'])
    headers = sorted_data[0].keys()
    table = tabulate([item.values() for item in sorted_data], headers=headers, tablefmt='grid')
    print(table)
    

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('My Weather App')
    
def run_visualization():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())