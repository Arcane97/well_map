#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
        QGraphicsScene, QGraphicsView, QComboBox, QSpinBox,
        QGraphicsItem, QGraphicsEllipseItem, QGraphicsRectItem)
from PyQt5 import QtCore, QtGui
from pointsEdit_ui_with_grid_layout import Ui_Form 

"""Класс Well
    Предствляет собой скважину
"""
class Well:
    def __init__ (self, widArg, xArg, yArg, statusArg = "NA"):
        """Конструктор класса скважины
        :param widArg: число уникально идентиф-е скважину
        :type widArg: int
        :param xArg: расположение по x
        :type xArg: int
        :param yArg: расположение по y
        :type yArg: int
        :param statusArg: одна из строк ["NA", "Buldyga", "W"]
        NA == неактивна, Buldyga == дичь, W == работает
        :type statusArg: str
        """
        self.wid    = idArg
        self.x      = xArg
        self.y      = yArg
        self.status = statusArg

    def setID (self, widArg):
        """Сеттер ID
        :param widArg: новый уникальный идентиф-р
        :type widArg: int
        """
        self.wid = widArg

    def setX (self, xArg):
        """Сеттер коор-ы x
        :param xArg: установить x равный xArg
        :type xArg: int
        """
        self.x = xArg

    def setY (self, yArg):
        """Сеттер коор-ы y
        :param yArg: установить y равный yArg
        :type yArg: int
        """
        self.y = yArg

    def setStatus (self, statusArg):
        """Сеттер статуса скважины
        :param statusArg: одна из строк ["NA", "Buldyga", "W"]
        NA == неактивна, Buldyga == дичь, W == работает
        :type statusArg: str
        """
        self.status = statusArg

    def getID (self):
        """Получить WID скважины
        :rtype: int
        """
        return self.wid

    def getX (self):
        """Получить коор-у x
        :rtype: int
        """
        return self.x

    def getY (self):
        """Получить коор-у y
        :rtype: int
        """
        return self.y
    
    def getTuple (self):
        """Получить коор-ы в виде кортежа
        :rtype: tuple
        """
        return (self.x, self.y,)


"""Класс OWEModel
    Оперирует с данными
"""
class OWEModel():
    def __init__ (self, bType = "1", bWidth = 100, bHeight = 100, wDict = {}):
        """Конструктор OWEModel
        :param bType: Число в виде строки, к-е указывает тип границы
        :type bType: str
        :param bWidth: Ширина области
        :type bWidth: int
        :param bHeight: Высота области
        :type bHeight: int
        :param wDict: Скважины, хранящиеся в виде словаря, ключ - это wid
        скважины, а значение - экземпляр класса с данным wid
        :type wDict: dict
        """
        self._borderType   = bType
        self._borderWidth  = bWidth
        self._borderHeight = bHeight
        self._wellDict     = wDict

        # self._signalsModelView = SignalsModelView()  ###############################################      

    def setBorderWidth (self, valArg):
        """Сеттер ширины
        :param valArg: значение ширины
        :type valArg: int
        """
        self._borderWidth = valArg

    def setBorderHeight (self, valArg):
        """Сеттер высоты
        :param valArg: значение высоты
        :type valArg: int
        """
        self._borderHeight = valArg

    def setBorderType (self, typeArg):
        """Сеттер типа границы
        :param typeArg: тип границы в виде строкового числа
        :type typeArg: str
        """
        self._borderType = typeArg
        # self._signalsModelView.changeBorderType(typeArg) ###############################################

    def getBorderWidth (self):
        """Геттер ширины
        :rtype: int
        """
        return self._borderWidth

    def getBorderHeight (self):
        """Геттер высоты
        :rtype: int
        """
        return self._borderHeight

    def getBorderType (self):
        """Геттер типа границы
        :rtype: str
        """
        return self._borderType

    def addWell (self, wArg):
        """Добавить по ключу WID экземпляр Well. Если такого же ключа
        не было и значение было добавлено будет возвращено True
        :param wArg: Добавляемый экземпляр класса Well (скважины)
        :type wArg: Well()
        :rtype: bool
        """
        if not wArg.getID() in self._wellDict.keys():
            self._wellDict[ wArg.getID() ] = wArg
            return True
        else:
            return False

    def getAllWells (self):
        """Выдает весь словарь скважин
        :rtype: dict
        """
        return self._wellDict

    def getWell (self, key):
        """Получить экземпляр скважины по ключу (ID). В случае
        отсутсвии ключа вернет None
        :rtype: Well() or None
        """
        if key in self._wellDict.keys():
            return self._wellDict[key]
        else:
            return None
