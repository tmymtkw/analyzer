from PyQt6.QtWidgets import QWidget, QLabel, QListWidget, QListWidgetItem, QAbstractItemView, QHBoxLayout
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphWidget(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent=parent)
    self.init_ui()
    self.data = None
    self.x_item = None
    self.y_item = None

  def init_ui(self):
    self.x_labels = QListWidget(parent=self)
    self.x_labels.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
    self.x_labels.itemClicked.connect(self.set_x_item)
    self.x_labels.setGeometry(0, 0, 120, 300)

    self.y_labels = QListWidget(parent=self)
    self.y_labels.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
    self.y_labels.itemClicked.connect(self.set_y_item)
    self.y_labels.setGeometry(120, 0, 120, 300)
    # graph_window = QLabel(text="graph", parent=self)
    # graph_window.setGeometry(240, 0, 840, 300)

    self.x_labels.addItem("No labels")
    self.y_labels.addItem("No labels")

    self.fig = plt.figure()
    self.canvas = FigureCanvas(self.fig)
    self.ax = self.fig.add_subplot(1, 1, 1)

    layout = QHBoxLayout()
    layout.addWidget(self.x_labels)
    layout.addWidget(self.y_labels)
    layout.addWidget(self.canvas)
    self.setLayout(layout)


  def read_data(self, file_name):
    self.data = pd.read_csv(file_name)

  def clear(self):
    self.x_labels.clear()
    self.y_labels.clear()

  def insert(self):
    if self.data is None:
      self.x_labels.addItem("No labels")
      self.y_labels.addItem("No labels")
      return
    else:
      self.x_labels.addItem("row")
      self.x_labels.addItems(self.data.columns.values)
      self.y_labels.addItems(self.data.columns.values)

  def set_x_item(self):
    self.x_item = self.x_labels.selectedItems()[0].text()
    self.get_graph()

  def set_y_item(self):
    self.y_item = self.y_labels.selectedItems()[0].text()
    self.get_graph()

  def get_graph(self):
    if not self.x_item or not self.y_item:
      return
    elif self.x_item == "row":
      print("selected row")
      self.ax.cla()
      self.ax.scatter(self.data[self.y_item])
      self.canvas.draw()
      return
    else:
      print(f"plot {self.x_item} - {self.y_item}")
      self.ax.cla()
      self.ax.scatter(self.data[self.x_item], self.data[self.y_item], s=4)
      self.canvas.draw()
