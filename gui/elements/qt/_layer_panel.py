from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ._layer_list import QtLayerList
from ._layer_buttons import QtLayerButtons


class QtLayerPanel(QWidget):
    def __init__(self, layers):
        super().__init__()

        layout = QVBoxLayout()
        self.layersList = QtLayerList(layers)
        self.layersButtons = QtLayerButtons(layers)
        layout.addWidget(self.layersList)
        layout.addWidget(self.layersButtons)
        self.setLayout(layout)
