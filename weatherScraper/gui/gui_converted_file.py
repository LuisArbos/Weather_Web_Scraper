# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(59, 80, 681, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 7, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 5, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 10, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 11, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 11, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 10, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 6, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 9, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 6, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 10, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 8, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 9, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 5, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 8, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 7, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 11, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 12, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 12, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 12, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 13, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 13, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 13, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "City1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "City2"))
        self.label_27.setText(_translate("MainWindow", "Weather"))
        self.label_24.setText(_translate("MainWindow", "Weather"))
        self.label_8.setText(_translate("MainWindow", "Today_Date"))
        self.label_15.setText(_translate("MainWindow", "SNOW"))
        self.label_32.setText(_translate("MainWindow", "Weather"))
        self.label_33.setText(_translate("MainWindow", "Weather"))
        self.label_34.setText(_translate("MainWindow", "Weather"))
        self.label_19.setText(_translate("MainWindow", "Weather"))
        self.label_16.setText(_translate("MainWindow", "WIND"))
        self.label_17.setText(_translate("MainWindow", "SUNRISE"))
        self.label_22.setText(_translate("MainWindow", "Weather"))
        self.label_29.setText(_translate("MainWindow", "Weather"))
        self.label_4.setText(_translate("MainWindow", "Today"))
        self.label_10.setText(_translate("MainWindow", "Weather"))
        self.label_5.setText(_translate("MainWindow", "Weather"))
        self.label_6.setText(_translate("MainWindow", "Tomorrow"))
        self.label_21.setText(_translate("MainWindow", "Weather"))
        self.label_31.setText(_translate("MainWindow", "Weather"))
        self.label_3.setText(_translate("MainWindow", "08:00"))
        self.label_25.setText(_translate("MainWindow", "Weather"))
        self.label_9.setText(_translate("MainWindow", "Tomorrow_Date"))
        self.label_11.setText(_translate("MainWindow", "12:00"))
        self.label_30.setText(_translate("MainWindow", "Weather"))
        self.label_23.setText(_translate("MainWindow", "Weather"))
        self.label_26.setText(_translate("MainWindow", "Weather"))
        self.label_14.setText(_translate("MainWindow", "RAIN"))
        self.label_13.setText(_translate("MainWindow", "20:00"))
        self.label_28.setText(_translate("MainWindow", "Weather"))
        self.label_18.setText(_translate("MainWindow", "SUNSET"))
        self.label_12.setText(_translate("MainWindow", "16:00"))
        self.label_20.setText(_translate("MainWindow", "Weather"))

def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())