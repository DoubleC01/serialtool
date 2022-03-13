import sys
# import platform

from Public import *

from GUI import *

# class MainWindow(QMainWindow):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # print(QStyleFactory.keys())
    # app.setStyle(QStyleFactory.create("Fusion"))
    app.setStyle("Fusion")
    window = MainWindow()
    sys.exit(app.exec_())
