from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QFileDialog

class FileWidget(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent=parent)
    self.init_ui()
    self.file_name = None

  def init_ui(self):
    file_button = QPushButton(text="Select file", parent=self)
    file_button.setGeometry(30, 30, 70, 30)
    file_button.clicked.connect(self.set_file_name)

    self.file_label = QLabel(text="No file selected.", parent=self)
    self.file_label.setGeometry(120, 30, 500, 30)

  def set_file_name(self):
    self.file_name = QFileDialog.getOpenFileName(self, "Open file", "/home",
                                                 filter="CSV file (*.csv)")
    if self.file_name[0] == "":
      return
    self.file_label.setText(self.file_name[0])

  def get_file_name(self):
    if self.file_name == None:
      return None
    else:
      return self.file_name[0]