import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        # Llamamaos al método init de la clase padre
        super().__init__()
        self.setWindowTitle('POO en PySide')
        # self.resize(600, 400)
        # Colocamos los valores de ancho y alto de manera fija
        self.setFixedSize(QSize(600, 400))
        # Creamos algunos componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregamos un menú
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Agregamos algunas opciones al menú
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        # Agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Información de la barra de estado...')
        # Agregamos un botón
        boton = QPushButton('Nuevo Botón')
        # Publicamos el botón en la ventan
        self.setCentralWidget(boton)


if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())
