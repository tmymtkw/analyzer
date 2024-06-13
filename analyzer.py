import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from widgets import FileWidget, GraphWidget

class Analyzer(QWidget):
  def __init__(self):
    super().__init__()
    self.h = 720
    self.w = 1080
    self.setWindowTitle('analyzer') # ウィンドウのタイトル
    self.setGeometry(100,100,1080,720) # ウィンドウの位置と大きさ

    self.create_widgets()

    self.data = None

  def create_widgets(self):
    self.close_button = QPushButton(text="close", parent=self)
    self.close_button.setGeometry(980, 30, 70, 30)
    self.close_button.clicked.connect(self.close)

    self.analyze_button = QPushButton(text="analyze", parent=self)
    self.analyze_button.setGeometry(700, 30, 70, 30)
    self.analyze_button.clicked.connect(self.analyze)

    self.file_widget = FileWidget(parent=self)
    self.file_widget.setGeometry(0, 0, 500, 150)

    self.graph_widget = GraphWidget(parent=self)
    self.graph_widget.setGeometry(0, 150, 1080, 570)

  def analyze(self):
    file_name = self.file_widget.get_file_name()
    if not file_name:
      return
    
    self.graph_widget.read_data(file_name)
    self.set_list()

  def set_list(self):
    self.graph_widget.clear()
    self.graph_widget.insert()
    return

def main():
  qAp = QApplication(sys.argv)
  analyzer = Analyzer()
  analyzer.show()
  qAp.exec()

if __name__ == "__main__":
   main()