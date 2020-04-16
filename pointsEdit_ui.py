# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pointsEdit_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.comboBorder = QtWidgets.QComboBox(Form)
        self.comboBorder.setGeometry(QtCore.QRect(10, 30, 83, 32))
        self.comboBorder.setMaxCount(10)
        self.comboBorder.setObjectName("comboBorder")
        self.spinWidth = QtWidgets.QSpinBox(Form)
        self.spinWidth.setGeometry(QtCore.QRect(10, 100, 81, 32))
        self.spinWidth.setMaximum(100000)
        self.spinWidth.setVisible(False)
        self.spinWidth.setObjectName("spinWidth")
        self.spinHeight = QtWidgets.QSpinBox(Form)
        self.spinHeight.setGeometry(QtCore.QRect(10, 160, 81, 32))
        self.spinHeight.setMaximum(100000)
        self.spinHeight.setVisible(False)
        self.spinHeight.setObjectName("spinHeight")
        self.labelBorder = QtWidgets.QLabel(Form)
        self.labelBorder.setGeometry(QtCore.QRect(10, 10, 91, 18))
        self.labelBorder.setObjectName("labelBorder")
        self.labelWidth = QtWidgets.QLabel(Form)
        self.labelWidth.setGeometry(QtCore.QRect(10, 80, 71, 18))
        self.labelWidth.setVisible(False)
        self.labelWidth.setObjectName("labelWidth")
        self.labelHeight = QtWidgets.QLabel(Form)
        self.labelHeight.setGeometry(QtCore.QRect(10, 140, 71, 18))
        self.labelHeight.setVisible(False)
        self.labelHeight.setObjectName("labelHeight")
        self.graphArea = QtWidgets.QGraphicsView(Form)
        self.graphArea.setGeometry(QtCore.QRect(130, 0, 661, 591))
        self.graphArea.setObjectName("graphArea")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Размещение скважин"))
        self.labelBorder.setText(_translate("Form", "Тип границы:"))
        self.labelWidth.setText(_translate("Form", "Ширина:"))
        self.labelHeight.setText(_translate("Form", "Высота:"))
