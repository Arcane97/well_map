#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
        QGraphicsScene, QGraphicsView, QComboBox, QSpinBox,
        QGraphicsItem, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsBlurEffect)
from PyQt5 import QtCore, QtGui
from pointsEdit_ui_with_grid_layout import Ui_Form 
from owe_model import OWEModel

""" Класс с сигналами
"""
class SignalsModelView (QtCore.QObject):
    # сигнал для отправки типа границы
    signalChangeBorderType = QtCore.pyqtSignal(str, name = 'signalChangeBorderType') ######################################### разобраться с сигналами
    # сигнал для отрисовки безграничной оьласти
    signalAreaLimitless = QtCore.pyqtSignal(name = 'signalAreaLimitless')
    # сигнал для отправки ширины
    signalWidthArea = QtCore.pyqtSignal(int, name = 'signalWidthArea')
    # сигнал для отправки ширины
    signalWidthHeightArea = QtCore.pyqtSignal(int, int, name = 'signalWidthHeightArea')

    signalValueArea = QtCore.pyqtSignal(name = 'signalValueArea')

    # испускаем сигнал для отправки типа границы
    def emitSignalGetBorderType (self, typeBorder):
        self.signalChangeBorderType.emit(typeBorder)
    # испускаем сигнал для отрисовки безграничной оласти
    def emitSignalDrawAreaLimitless (self):
        self.signalAreaLimitless.emit()
    # испускаем игнал для отправки ширины
    def emitSignalGetWidthArea (self, widthArea):
        self.signalWidthArea.emit(widthArea)
    # испускаем игнал для отправки высоты
    def emitSignalGetWidthHeightArea (self, widthArea, heightArea):
        self.signalWidthHeightArea.emit(widthArea, heightArea)

    def emitSignalValueArea (self):
        self.signalValueArea.emit()


""" Класс ViewWell
    Создает эллипс (визуализацию скважины) 
"""
class ViewWell (QGraphicsEllipseItem):
    def __init__(self, parent=None):
        super().__init__(QtCore.QRectF(), parent)
        self.coords = None #QtCore.QEvent()

    def getEllipse (self): 
        """ Формирование эллипса
        """
        # заливка
        self.setBrush(QtCore.Qt.red)
        # эллипс возможно перемещать
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        # радус эллипса
        ellipseRadius   = QtCore.QPointF(10, 10)
        # начальная координата отрисовки эллипса
        ellipseTLCoords = self.coords - ellipseRadius
        # конечная координата отрисовки эллипса
        ellipseBRCoords = self.coords + ellipseRadius
        # задание координат эллипса
        coordEllipse    = QtCore.QRectF(ellipseTLCoords, ellipseBRCoords)
        # отрисовка эллипса
        self.setRect(coordEllipse)
        self.setSpanAngle(5760)

    def setCoords (self, coords):
        """ Получение координат эллипса
        """
        self.coords = coords

"""Класс GraphicsScene
    Реализует графический вывод для graphArea
"""
class GraphicsScene (QGraphicsScene):
    def __init__(self, parent=None):
        super(GraphicsScene, self).__init__(QtCore.QRectF(0, 0, 500, 500), parent)
        # выделенный эллипс
        self._currentEllipseItem = None
        # Начало координат
        self._Xo = 0
        self._Yo = 500
        # Модель данных
        self.sceneModel = None

    def setModel(self, model):
        """ Соединение с моделью
        """
        self.sceneModel = model

    def scalingArea(self, rect, width, height):
        """Масштабирование значений координат для отрисовки области
        """
        scalX = self._Xo
        if rect.size().height() / height >= rect.size().width() / width:
            # область шириной в сцену
            scalWidth  = rect.size().width() - self.padding
            scalHeight = round(height * scalWidth / width)
            scalY      = self._Yo - scalHeight
        else:
            # область высотой в сцену
            scalHeight = rect.size().height() - self.padding
            scalWidth  = round(width * scalHeight / height)
            scalY      = rect.top()            

        return scalX, scalY, scalWidth, scalHeight

    def drawBackground(self, painter, rect):
        """ Отрисовка области на фоне
        """
        # Изменение начала координат при изменении размера окна 
        self.padding = 10
        self._Xo = rect.left() + self.padding
        self._Yo = rect.bottom() - self.padding

        # Задание координат области
        topLeftX = self._Xo
        if self.sceneModel._borderType == "1":
            # Одна граница
            topLeftY = rect.top()
            width    = rect.size().width() - self.padding
            height   = rect.size().height() - self.padding
        elif self.sceneModel._borderType == "2":
            # Две границы
            topLeftY = rect.top()
            width    = self.sceneModel._borderWidth
            height   = rect.size().height() - self.padding
        else:
            # Четрыре границы
            topLeftX, topLeftY, width, height = self.scalingArea(rect, self.sceneModel._borderWidth, self.sceneModel._borderHeight)

        # Формирование области
        limitedArea = QtCore.QRectF(topLeftX, topLeftY, width, height)
        # Заливка области цветом    
        backgroundBrush = QtGui.QBrush(QtCore.Qt.green)
        # Отрисовка области
        painter.fillRect(limitedArea, backgroundBrush)
        # Задание кисти для отрисовки осей 
        painter.setPen(QtGui.QPen(QtCore.Qt.black))

        # Отрисовка оси x
        painter.drawLine(QtCore.QPointF(self._Xo, self._Yo), QtCore.QPointF(rect.right() - self.padding, self._Yo))
        # Отрисовка оси y
        painter.drawLine(QtCore.QPointF(self._Xo, self._Yo), QtCore.QPointF(self._Xo, rect.top() + self.padding))

    def mouseDoubleClickEvent (self, event):
        """Реакция на двойной клик. Создает скважину
        """
        # if self.itemAt(event.scenePos(), QtGui.QTransform()) is self._rectItem: 
        if True:                       ####################################################### добавить обработку нажания в область
            # Создание итема эллипса (скважины)
            self._currentEllipseItem = ViewWell()
            # Задание координат для эллипса
            self._currentEllipseItem.setCoords(event.scenePos())
            # Формирование итема элипса
            self._currentEllipseItem.getEllipse()

            # добавление итема 
            self.addItem(self._currentEllipseItem)

            # Удаляет передний фон (исправление бага: при создании элипса, в передний фон итема заливается задний фон)
            self.setForegroundBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        super(GraphicsScene, self).mouseDoubleClickEvent(event)

    def mouseReleaseEvent (self, event):
        """Реакция на отпускание нажатой ЛКМ
        """
        # возвращение цвета итема в начальный вариант, т.е. не выделенный
        if (self._currentEllipseItem != None):
            self._currentEllipseItem.setBrush(QtCore.Qt.red)

        # выделение итема элиппса (скважины)
        self._currentEllipseItem = self.itemAt(event.scenePos(), QtGui.QTransform())

        # изменение цвета итема в выделеный вариант, т.е. светлее
        if  self._currentEllipseItem != None:
            # изначальный цвет выделения
            brushColor = QtGui.QColor(self._currentEllipseItem.brush())
            # осветление
            brushColor = brushColor.lighter(150)
            # заливка
            self._currentEllipseItem.setBrush(brushColor)

        # Удаляет передний фон (исправление бага: при создании элипса, в передний фон итема заливается задний фон)
        self.setForegroundBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        super(GraphicsScene, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        """ Реакция на перемещение нажатой ЛКМ
        """
        # Удаляет передний фон (исправление бага: при создании элипса, в передний фон итема заливается задний фон)
        self.setForegroundBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        super(GraphicsScene, self).mouseMoveEvent(event)

    def keyPressEvent (self, event):
        """Реакция на нажатие клавиши
        """
        # удаление выделенной скважины при нажатии кнопки delete
        if event.key() == 16777223 and self._currentEllipseItem != None:
            self.removeItem(self._currentEllipseItem)

        super(GraphicsScene, self).keyPressEvent(event)

"""Класс OWEView
    Посылает сигналы модели для изменения данных
"""
class OWEView (QMainWindow):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Создаем окно GUI
        self.ui = Ui_Form() 
        self.ui.setupUi(self)

        # Подключаем графическую сцену
        self.scene = GraphicsScene(self)
        self.ui.graphArea.setScene(self.scene)

        # Подключаем модель
        self.model = OWEModel()

        # Подключаем модель к сцене
        self.scene.setModel(self.model)

        # Добавим данные с модели на вид
        self.ui.spinWidth.setValue(self.model.getBorderWidth())
        self.ui.spinHeight.setValue(self.model.getBorderHeight())
        self.ui.comboBorder.addItems(["1", "2", "4"])
        self.ui.comboBorder.setCurrentIndex(self.currentBorderIndex())

        # Соединяем сигналы с GUI-объектами
        self.ui.spinWidth.valueChanged.connect(self._onWidthChange)
        self.ui.spinHeight.valueChanged.connect(self._onHeightChange)
        self.ui.comboBorder.currentIndexChanged.connect(self._onBorderChange)

        # добавление класса с сигналами
        self.signalsModelView = SignalsModelView()
        # коннект сигнала смены типа границы
        self.signalsModelView.signalChangeBorderType.connect(self.slotGetBorderType)
        # коннект сигнала отрисовки безграничной области
        self.signalsModelView.signalAreaLimitless.connect(self.scene.update)
        # коннект сигнал оправки значения ширины
        self.signalsModelView.signalWidthArea.connect(self.scene.update)
        # коннект сигнал оправки значения ширины и высоты 
        self.signalsModelView.signalWidthHeightArea.connect(self.scene.update)

    def _onBorderChange (self):
        """Изменяет тип границы
        """
        self.model.setBorderType(self.currentBorderType())
        # испускается сигнал смены типа границы
        self.signalsModelView.emitSignalGetBorderType(self.model.getBorderType())

        # перерисовывается область в зависимости от типа границ
        if self.model.getBorderType() == '1':
            self.signalsModelView.emitSignalDrawAreaLimitless()
        elif self.model.getBorderType() == '2':
            self.signalsModelView.emitSignalGetWidthArea(self.model.getBorderWidth())
        else:
            self.signalsModelView.emitSignalGetWidthHeightArea(self.model.getBorderWidth(), self.model.getBorderHeight())

    def _onWidthChange (self):
        """Обрабатывает изменение ширины
        """
        # изменение ширины в модели
        self.model.setBorderWidth(self.ui.spinWidth.value())

        if self.model.getBorderType() == '2':
            # испускается сигнал оправки значения ширины
            self.signalsModelView.emitSignalGetWidthArea(self.model.getBorderWidth())
            
        else:
            # испускается сигнал оправки значения ширины и высоты 
            self.signalsModelView.emitSignalGetWidthHeightArea(self.model.getBorderWidth(), self.model.getBorderHeight())
            

    def _onHeightChange (self):
        """Обрабатывает изменение высоты 
        """
        # изменение высоты в модели
        self.model.setBorderHeight(self.ui.spinHeight.value())
        # испускается сигнал оправки значения ширины и высоты 
        self.signalsModelView.emitSignalGetWidthHeightArea(self.model.getBorderWidth(), self.model.getBorderHeight())

    def currentBorderIndex (self):
        """Вернуть индекс comboBorder соот-го значению borderType
        :rtype: int or None
        """
        currBorder = self.model.getBorderType()
        if currBorder   == "1":
            return 0
        elif currBorder == "2":
            return 1
        elif currBorder == "4":
            return 2
        else:
            return None

    def currentBorderType (self):
        """Вернуть borderType соот-го значению индекса comboBorder
        :rtype: str or None
        """
        currentInd = self.ui.comboBorder.currentIndex()
        if currentInd   == 0:
            return "1"
        elif currentInd == 1:
            return "2"
        elif currentInd == 2:
            return "4"
        else:
            return None

    @QtCore.pyqtSlot(str)
    def slotGetBorderType (self, borderType):
        """ слот для измения видимости элеметов управления шириной и высотой области
        """
        if borderType == '1':
            self.ui.labelWidth.setVisible(False)
            self.ui.spinWidth.setVisible(False)
            self.ui.labelHeight.setVisible(False)
            self.ui.spinHeight.setVisible(False)
        elif borderType == '2':
            self.ui.labelWidth.setVisible(True)
            self.ui.spinWidth.setVisible(True)
            self.ui.labelHeight.setVisible(False)
            self.ui.spinHeight.setVisible(False)
        else:
            self.ui.labelWidth.setVisible(True)
            self.ui.spinWidth.setVisible(True)
            self.ui.labelHeight.setVisible(True)
            self.ui.spinHeight.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = OWEView()
    win.show()
    sys.exit(app.exec_())
