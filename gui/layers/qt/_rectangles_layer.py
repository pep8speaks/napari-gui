from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QComboBox, QSlider
from collections import Iterable
import numpy as np
from ._base_layer import QtLayer

class QtRectanglesLayer(QtLayer):
    def __init__(self, layer):
        super().__init__(layer)

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        #sld.setInvertedAppearance(True)
        sld.setFixedWidth(75)
        sld.setMinimum(0)
        sld.setMaximum(100)
        sld.setSingleStep(1)
        value = self.layer.size
        if isinstance(value, Iterable):
            if isinstance(value, list):
                value = np.asarray(value)
            value = value.mean()
        sld.setValue(int(value))
        sld.valueChanged[int].connect(lambda value=sld: self.changeSize(value))
        self.grid_layout.addWidget(QLabel('size:'), 3, 0)
        self.grid_layout.addWidget(sld, 3, 1)

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        #sld.setInvertedAppearance(True)
        sld.setFixedWidth(75)
        sld.setMinimum(0)
        sld.setMaximum(100)
        sld.setSingleStep(1)
        value = self.layer.size
        if isinstance(value, Iterable):
            if isinstance(value, list):
                value = np.asarray(value)
            value = value.mean()
        sld.setValue(int(value))
        sld.valueChanged[int].connect(lambda value=sld: self.changeWidth(value))
        self.grid_layout.addWidget(QLabel('width:'), 4, 0)
        self.grid_layout.addWidget(sld, 4, 1)

        face_comboBox = QComboBox()
        colors = self.layer._colors
        for c in colors:
           face_comboBox.addItem(c)
        index = face_comboBox.findText(self.layer.face_color, Qt.MatchFixedString)
        if index >= 0:
           face_comboBox.setCurrentIndex(index)
        face_comboBox.activated[str].connect(lambda text=face_comboBox: self.changeFaceColor(text))
        self.grid_layout.addWidget(QLabel('face_color:'), 5, 0)
        self.grid_layout.addWidget(face_comboBox, 5, 1)

        edge_comboBox = QComboBox()
        colors = self.layer._colors
        for c in colors:
           edge_comboBox.addItem(c)
        index = edge_comboBox.findText(self.layer.edge_color, Qt.MatchFixedString)
        if index >= 0:
           edge_comboBox.setCurrentIndex(index)
        edge_comboBox.activated[str].connect(lambda text=edge_comboBox: self.changeEdgeColor(text))
        self.grid_layout.addWidget(QLabel('edge_color:'), 6, 0)
        self.grid_layout.addWidget(edge_comboBox, 6, 1)

        vertex_comboBox = QComboBox()
        colors = self.layer._colors
        for c in colors:
           vertex_comboBox.addItem(c)
        index = vertex_comboBox.findText(self.layer.vertex_color, Qt.MatchFixedString)
        if index >= 0:
           vertex_comboBox.setCurrentIndex(index)
        vertex_comboBox.activated[str].connect(lambda text=vertex_comboBox: self.changeVertexColor(text))
        self.grid_layout.addWidget(QLabel('vertex_color:'), 7, 0)
        self.grid_layout.addWidget(vertex_comboBox, 7, 1)

        self.setExpanded(False)

    def changeFaceColor(self, text):
        self.layer.face_color = text

    def changeEdgeColor(self, text):
        self.layer.edge_color = text

    def changeVertexColor(self, text):
        self.layer.vertex_color = text

    def changeSize(self, value):
        self.layer.size = value

    def changeWidth(self, value):
        self.layer.edge_width = value