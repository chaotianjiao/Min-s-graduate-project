# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class buy_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buy_manage_label = QtWidgets.QLabel(self.centralwidget)
        self.buy_manage_label.setGeometry(QtCore.QRect(350, 20, 171, 61))
        font = QtGui.QFont()
        font.setFamily("华文宋体")
        font.setPointSize(28)
        self.buy_manage_label.setFont(font)
        self.buy_manage_label.setObjectName("label")
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
        self.widget.setGeometry(QtCore.QRect(0, 180, 841, 241))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buy_plan_make = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.buy_plan_make.setFont(font)
        self.buy_plan_make.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.buy_plan_make, 1, 1, 1, 1)
        self.drug_information = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.drug_information.setFont(font)
        self.drug_information.setObjectName("pushButton")
        self.gridLayout.addWidget(self.drug_information, 0, 0, 1, 1)
        self.bill_information = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.bill_information.setFont(font)
        self.bill_information.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.bill_information, 1, 0, 1, 1)
        self.supply_information = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.supply_information.setFont(font)
        self.supply_information.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.supply_information, 0, 1, 1, 1)
        self.drug_settlement = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.drug_settlement.setFont(font)
        self.drug_settlement.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.drug_settlement, 2, 0, 1, 1)
        self.procurement_of_drugs = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.procurement_of_drugs.setFont(font)
        self.procurement_of_drugs.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.procurement_of_drugs, 1, 2, 1, 1)
        self.change_purchase_bill = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.change_purchase_bill.setFont(font)
        self.change_purchase_bill.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.change_purchase_bill, 0, 2, 1, 1)
        self.drug_purchase = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.drug_purchase.setFont(font)
        self.drug_purchase.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.drug_purchase, 2, 1, 1, 1)
        self.drug_return = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.drug_return.setFont(font)
        self.drug_return.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.drug_return, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 23))
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
        self.buy_manage_label.setText(_translate("MainWindow", "采购管理"))
        self.buy_plan_make.setText(_translate("MainWindow", "采购计划制定"))
        self.drug_information.setText(_translate("MainWindow", "采购药品信息查询"))
        self.bill_information.setText(_translate("MainWindow", "采购账目查询"))
        self.supply_information.setText(_translate("MainWindow", "供货商信息查询"))
        self.drug_settlement.setText(_translate("MainWindow", "药品结算"))
        self.procurement_of_drugs.setText(_translate("MainWindow", "采购药品入库"))
        self.change_purchase_bill.setText(_translate("MainWindow", "采购账目修改"))
        self.drug_purchase.setText(_translate("MainWindow", "药品采购"))
        self.drug_return.setText(_translate("MainWindow", "药品退货"))
