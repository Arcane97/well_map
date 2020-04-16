# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pointsEdit_ui_with_grid_layout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.labelHeight = QtWidgets.QLabel(self.centralwidget)
        self.labelHeight.setObjectName("labelHeight")
        self.labelHeight.setVisible(False)
        self.gridLayout.addWidget(self.labelHeight, 4, 0, 1, 1)
        self.labelBorder = QtWidgets.QLabel(self.centralwidget)
        self.labelBorder.setObjectName("labelBorder")
        self.gridLayout.addWidget(self.labelBorder, 0, 0, 1, 1)
        self.comboBorder = QtWidgets.QComboBox(self.centralwidget)
        self.comboBorder.setMinimumSize(QtCore.QSize(100, 25))
        self.comboBorder.setMaximumSize(QtCore.QSize(100, 25))
        self.comboBorder.setMaxCount(10)
        self.comboBorder.setObjectName("comboBorder")
        self.gridLayout.addWidget(self.comboBorder, 1, 0, 1, 1)
        self.labelWidth = QtWidgets.QLabel(self.centralwidget)
        self.labelWidth.setObjectName("labelWidth")
        self.labelWidth.setVisible(False)
        self.gridLayout.addWidget(self.labelWidth, 2, 0, 1, 1)
        self.spinWidth = QtWidgets.QSpinBox(self.centralwidget)
        self.spinWidth.setMinimumSize(QtCore.QSize(100, 25))
        self.spinWidth.setMaximumSize(QtCore.QSize(100, 25))
        self.spinWidth.setMaximum(100000)
        self.spinWidth.setVisible(False)
        self.spinWidth.setObjectName("spinWidth")
        self.gridLayout.addWidget(self.spinWidth, 3, 0, 1, 1)
        self.spinHeight = QtWidgets.QSpinBox(self.centralwidget)
        self.spinHeight.setMinimumSize(QtCore.QSize(100, 25))
        self.spinHeight.setMaximumSize(QtCore.QSize(100, 25))
        self.spinHeight.setMaximum(100000)
        self.spinHeight.setVisible(False)
        self.spinHeight.setObjectName("spinHeight")
        self.gridLayout.addWidget(self.spinHeight, 5, 0, 1, 1)
        self.graphArea = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphArea.setObjectName("graphArea")
        self.gridLayout.addWidget(self.graphArea, 0, 1, 7, 1)
        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Размещение скважин"))
        self.labelHeight.setText(_translate("Form", "Высота:"))
        self.labelBorder.setText(_translate("Form", "Тип границы:"))
        self.labelWidth.setText(_translate("Form", "Ширина:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

