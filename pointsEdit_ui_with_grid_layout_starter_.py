import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
        QGraphicsScene, QGraphicsView, QComboBox, QSpinBox,
        QGraphicsItem, QGraphicsEllipseItem, QGraphicsRectItem)
from PyQt5 import QtCore, QtGui
from pointsEdit_ui_with_grid_layout import Ui_Form 

# from owe_view import GraphicsScene
from owe_model import OWEModel
from owe_view import ViewWell

class GraphicsScene (QGraphicsScene):
    def __init__(self, parent=None):
        super(GraphicsScene, self).__init__(QtCore.QRectF(0, 0, 500, 500), parent)
        # выделенный эллипс
        self._currentEllipseItem = None
        # Начало координат
        self._Xo = 0
        self._Yo = 500

    def drawBackground(self, painter, rect):
        """ Отрисовка области на фоне
        """
        # Изменение начала координат при изменении размера окна 
        self.padding = 10
        self._Xo = rect.left() + self.padding
        self._Yo = rect.bottom() - self.padding

        # Задание координат области
        topLeftX = self._Xo
        topLeftY = rect.top()
        width    = rect.size().width() - self.padding
        height   = rect.size().height() - self.padding

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

    # def drawForeground(self, painter, rect):
    #     """Удаляет передний фон (исправление бага: при создании элипса, в передний фон итема заливается задний фон)
    #     """
    #     self.setForegroundBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

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

            self.setForegroundBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        super(GraphicsScene, self).mouseDoubleClickEvent(event)

    def mouseReleaseEvent (self, event):
        """Реакция на отпускание нажатой ЛКМ
        """
        # print(event.scenePos())
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


        self.setForegroundBrush(QtGui.QBrush(QtCore.Qt.NoBrush))
        super(GraphicsScene, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):

        self.setForegroundBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        super(GraphicsScene, self).mouseMoveEvent(event)

    def keyPressEvent (self, event):
        """Реакция на нажатие клавиши
        """
        # удаление выделенной скважины при нажатии кнопки delete
        if event.key() == 16777223 and self._currentEllipseItem != None:
            self.removeItem(self._currentEllipseItem)

        super(GraphicsScene, self).keyPressEvent(event)


class OWEView (QMainWindow):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Создаем окно GUI
        self.ui = Ui_Form() 
        self.ui.setupUi(self)

        # Подключаем графическую сцену
        self.scene = GraphicsScene()
        self.ui.graphArea.setScene(self.scene)

        # # Подключаем модель
        # self.model = OWEModel()

        # # Подключаем модель к сцене
        # self.scene.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = OWEView()
    win.show()
    sys.exit(app.exec_())
