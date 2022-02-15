# -*- coding: utf-8 -*-

from GUI import *

class LogInWindow(QWidget):
    def __init__(self):
        super(LogInWindow,self).__init__()
        self.LogInWindowFrame = QWidget(MainWindow.MainWindowCenter)
        self.LogInWindowFrame.show()
        self.LogInWindowFrame.setStyleSheet("background:rgb(111,111,111)")
        
        #设置登陆界面布局
        self.LogInWindowHbox = QHBoxLayout()
        # self.LogInWindowHbox = QGridLayout()
        self.LogInWindowHbox.setSizeConstraint(QLayout.SetMinAndMaxSize)
        # self.LogInWindowHbox.addStretch(1)
        self.LogInWindowHbox.setSpacing(0)
        self.LogInWindowHbox.setContentsMargins(0, 0, 0, 0)#边沿为0
        self.LogInWindowHbox.addWidget(self.LogInWindowFrame)
        # MainWindowCenter.setLayout(self.LogInWindowHbox)