# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sell.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class sell_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sell_manage_label = QtWidgets.QLabel(self.centralwidget)
        self.sell_manage_label.setGeometry(QtCore.QRect(350, 20, 171, 61))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(28)
        self.sell_manage_label.setFont(font)
        self.sell_manage_label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 600, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../picture/11.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 430, 600, 100))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../picture/22.jpg"))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 180, 741, 241))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.drug_allocate_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.drug_allocate_btn.setFont(font)
        self.drug_allocate_btn.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.drug_allocate_btn, 1, 1, 1, 1)
        self.sell_and_return_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.sell_and_return_btn.setFont(font)
        self.sell_and_return_btn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.sell_and_return_btn, 0, 0, 1, 1)
        self.return_query_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.return_query_btn.setFont(font)
        self.return_query_btn.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.return_query_btn, 1, 0, 1, 1)
        self.store_manage_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.store_manage_btn.setFont(font)
        self.store_manage_btn.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.store_manage_btn, 0, 1, 1, 1)
        self.sell_bill_manage_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.sell_bill_manage_btn.setFont(font)
        self.sell_bill_manage_btn.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.sell_bill_manage_btn, 2, 0, 1, 1)
        self.drug_split_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.drug_split_btn.setFont(font)
        self.drug_split_btn.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.drug_split_btn, 1, 2, 1, 1)
        self.sell_information_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.sell_information_btn.setFont(font)
        self.sell_information_btn.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.sell_information_btn, 0, 2, 1, 1)
        self.reduce_price_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.reduce_price_btn.setFont(font)
        self.reduce_price_btn.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.reduce_price_btn, 2, 1, 1, 1)
        self.on_sale_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.on_sale_btn.setFont(font)
        self.on_sale_btn.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.on_sale_btn, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 23))
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
        self.sell_manage_label.setText(_translate("MainWindow", "销售管理"))
        self.drug_allocate_btn.setText(_translate("MainWindow", "药品调拨"))
        self.sell_and_return_btn.setText(_translate("MainWindow", "销售及退药"))
        self.return_query_btn.setText(_translate("MainWindow", "退药查询"))
        self.store_manage_btn.setText(_translate("MainWindow", "库存管理"))
        self.sell_bill_manage_btn.setText(_translate("MainWindow", "销售账目管理"))
        self.drug_split_btn.setText(_translate("MainWindow", "药品拆分"))
        self.sell_information_btn.setText(_translate("MainWindow", "销售查询"))
        self.reduce_price_btn.setText(_translate("MainWindow", "打折优惠"))
        self.on_sale_btn.setText(_translate("MainWindow", "促销"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = sell_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())