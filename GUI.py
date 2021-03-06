# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Public import *

# QLineEdit[echoMode='2'] {lineedit-password-character: 9679;}\
# QLineEdit:read-only {background: lightblue;}\

class MySignals(QObject):
    LineEditSignal = Signal(object,dict)
    TextEditSignal = Signal(object,dict)
    PushButtonSignal = Signal(object,dict)
    LabelSignal = Signal(object,dict)
    CheckBoxSignal = Signal(object,dict)
    SpinBoxSignal = Signal(object,dict)

class Test(QWidget):
    def initUI(self,MainWindow):
        self.setWindowTitle(TitleName)
        self.resize(800,400)
        
        self.setStyleSheet("QPushButton{background:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123));\
                                        border:1px groove gray;\
                                        border-radius:3px;\
                                        border-style:outset;\
                                        font:14px;\
                                        padding:1px 3px 1px 3px;\
                                        color:white} \
                            QPushButton:pressed{border:2px solid gray} \
                            QPushButton:hover{background:qlineargradient(x1:1, y1:1, x2:0, y2:0,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123));}\
                            QTextEdit{font:12px;}\
                            QTextEdit:hover {background-color: #c5ecc8;}\
                            QLineEdit {width: 60px;}\
                            QLineEdit:hover {background-color: #c5ecc8;}\
                            QCheckBox:hover {background-color: #c5ecc8;}\
                            QSpinBox:hover {background-color: #c5ecc8;}\
                            QComboBox:hover {background-color: #c5ecc8;}\
                            QStatusBar{background:qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgb(105,170,105),stop:0.5 rgb(127,127,127),stop:1 rgb(192,150,150));}\
                            ")
                            # background-image: url(':pubu.jpg');\
                            # QPushButton:flat {border:2px solid red;}
                            # QPushButton:open{background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}\
                            # QPushButton::menu-indicator {image:url(:/images/close.png);image:none; subcontrol-origin:padding; subcontrol-position:bottom right;}\
                            # QPushButton::menu-indicator:pressed,QPushButton::menu-indicator:open {position:relative; top:4px; left:4px; }

        # self.layout = QVBoxLayout()
        # self.layout.setSpacing(0)
        # self.layout.setContentsMargins(0, 0, 0, 0)

        # Color = QAction(QPixmap(":color_swatch.png"),'Color',self)
        # Color.triggered.connect(self.GetColor)
        # self.ToolBar = self.addToolBar('Color')
        # self.ToolBar.addAction(Color)

        self.statusBar=QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar_ShowLabel = QLabel('???????????????')
        self.statusBar_ShowLabel.setAlignment(Qt.AlignCenter)
        self.statusBar_TimeLabel = QLabel(strftime("%Y/%m/%d %H:%M:%S"))
        self.test_time = QTimer()
        self.test_time.timeout.connect(self.time_convert)
        self.test_time.start(1000)
        # self.StatusBar = self.statusBar()
        # # self.setWindowFlags(Qt.FramelessWindowHint) #?????????
        # # self.setAttribute(Qt.WA_TranslucentBackground) #????????????


        #??????????????????
        self.MainWindowCenter = QWidget()
        self.setCentralWidget(self.MainWindowCenter)
        self.MainGridLayout = QGridLayout(self.MainWindowCenter)
        self.MainGridLayout.setSpacing(0)
        self.MainGridLayout.setContentsMargins(0, 0, 0, 0)#?????????0
        
        self.Openico = QPixmap(":xiao 494.png")
        self.Closeico = QPixmap(":xiao 491.png")

        self.ms = MySignals() 
        self.ms.LineEditSignal.connect(self.LineEditDo)
        self.ms.TextEditSignal.connect(self.TextEditDo)
        self.ms.PushButtonSignal.connect(self.PushButtonDo)
        self.ms.LabelSignal.connect(self.LabelDo)
        self.ms.CheckBoxSignal.connect(self.CheckBoxDo)
        self.ms.SpinBoxSignal.connect(self.SpinBoxDo)

        self.setWindowIcon(QPixmap(Ico))

        # self.WinIcon(MainWindow)
        # self.BackDrop()
        # self.LogInWindow(MainWindow)
        self. BaseWin()
        self.show()
        self.WinCenter()

    def time_convert(self):
        timeStr = strftime("%Y/%m/%d %H:%M:%S")
        self.statusBar_TimeLabel.setText(timeStr)

    def GetColor(self):
        color = QColorDialog.getColor()
        # if color.isValid():
        #     print(color.name())
            # palette = self.label.palette()
            # palette.setColor(QPalette.Background, color)
            # self.label.setPalette(palette)

    def WinIcon(self):
        #????????????
        # MainWindowIcon = QIcon()
        # MainWindowIcon.addPixmap(QPixmap(Ico), QIcon.Normal,QIcon.Off)
        self.setWindowIcon(QPixmap(Ico))

    def WinCenter(self):
        # #????????????
        MainWindowScreen=QApplication.primaryScreen().geometry()
        MainWindowSize=self.geometry()
        self.move((MainWindowScreen.width() - MainWindowSize.width()) / 2,(MainWindowScreen.height() - MainWindowSize.height()) / 2)
        # self.setStyleSheet("background:rgb(255,0,255)")

    # def BackDrop(self):
    #     #????????????label
    #     self.MainWindowBackDropLabel = QLabel(self.MainWindowCenter)
    #     self.MainWindowBackDropGif = QMovie(MainPicture)
    #     self.MainWindowBackDropLabel.setMovie(self.MainWindowBackDropGif)
    #     # self.MainWindowBackDropLabel.setPixmap(QPixmap(Pic))
    #     self.MainWindowBackDropLabel.setScaledContents(True)
    #     self.MainWindowBackDropGif.start()

    def BaseWin(self):
        self.BaseWinFrame = QWidget(self.MainWindowCenter)
        self.BaseWinGrid = QGridLayout(self.BaseWinFrame)
        self.MainGridLayout.addWidget(self.BaseWinFrame)

        self.ReceiveHBox = QHBoxLayout()
        self.WatchVBox = QVBoxLayout()
        self.SendFunGrid = QGridLayout()
        self.SendHBox = QHBoxLayout()
        self.SerialVBox = QVBoxLayout()
        self.SendFunRightGrid = QGridLayout()
        self.SendConGrid = QGridLayout()
        # self.SendCountGrid = QGridLayout()
        self.HistroyVBox = QVBoxLayout()

        self.BaseWinGrid.addLayout(self.ReceiveHBox,0,0,1,1)
        self.BaseWinGrid.addLayout(self.WatchVBox,0,1,1,1)
        self.BaseWinGrid.addLayout(self.SendFunGrid,1,0,1,2)
        self.BaseWinGrid.addLayout(self.SendHBox,2,0,1,2)
        self.BaseWinGrid.addLayout(self.SerialVBox,0,2,1,1)
        self.BaseWinGrid.addLayout(self.SendFunRightGrid,1,2,1,1)
        self.BaseWinGrid.addLayout(self.SendConGrid,2,2,1,1)
        # self.BaseWinGrid.addLayout(self.SendCountGrid,3,0,1,2)
        self.BaseWinGrid.addLayout(self.HistroyVBox,0,3,3,1)

        self.BaseWinGrid.setColumnStretch(0,1)
        # self.BaseWinGrid.setColumnStretch(1,1)
        # self.BaseWinGrid.setColumnStretch(2,1)
        # self.BaseWinGrid.setColumnStretch(3,2)

        self.BaseWinGrid.setRowStretch(0,8)
        # # self.BaseWinGrid.setRowStretch(1,1)
        self.BaseWinGrid.setRowStretch(2,1)
        # # self.BaseWinGrid.setRowStretch(3,1)

        self.Receive_TextEdit = QTextEdit()
        # self.Receive_textBrowser.setStyleSheet(u"background-color: #61cfa7;")
        self.ReceiveHBox.addWidget(self.Receive_TextEdit)
        
        self.Serial_Form = QFormLayout()
        self.Serial_Grid1 = QGridLayout()
        self.Serial_Grid2 = QGridLayout()
        self.Serial_VSpacer = QSpacerItem(40, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.SerialVBox.addLayout(self.Serial_Form,0)
        self.SerialVBox.addLayout(self.Serial_Grid1,0)
        self.SerialVBox.addLayout(self.Serial_Grid2,0)
        self.SerialVBox.addItem(self.Serial_VSpacer)
        
        self.Send_TextEdit = QTextEdit()
        self.SendHBox.addWidget(self.Send_TextEdit)



        self.Serial_SerialNameLabel = QLabel('?????????')
        self.Serial_SerialComboBox = QComboBox()
        # self.Serial_SerialComboBox.setEditable(1)
        self.Serial_BuadNameLabel = QLabel('?????????')
        self.Serial_BuadComboBox = QComboBox()
        self.Serial_BuadComboBox.addItems(["300","600","1200","2400","4800","9600","14400","19200","38400","43000","57600","76800","115200", "230400", "460800", "500000",
                 "576000", "921600", "1000000", "1152000", "1500000", "2000000", "2500000",
                 "3000000", "3500000", "4000000"])
        self.Serial_ByteNameLabel = QLabel('?????????')
        self.Serial_ByteComboBox = QComboBox()
        self.Serial_ByteComboBox.addItems(["5","6","7","8"])
        self.Serial_StopNameLabel = QLabel('?????????')
        self.Serial_StopComboBox = QComboBox()
        self.Serial_StopComboBox.addItems(["1","1.5","2"])
        self.Serial_ParityNameLabel = QLabel('?????????')
        self.Serial_ParityComboBox = QComboBox()
        self.Serial_ParityComboBox.addItems(["E","N","O","M","S"])
        self.Serial_Form.addRow(self.Serial_SerialNameLabel,self.Serial_SerialComboBox,)
        self.Serial_Form.addRow(self.Serial_BuadNameLabel,self.Serial_BuadComboBox)
        self.Serial_Form.addRow(self.Serial_ByteNameLabel,self.Serial_ByteComboBox)
        self.Serial_Form.addRow(self.Serial_StopNameLabel,self.Serial_StopComboBox)
        self.Serial_Form.addRow(self.Serial_ParityNameLabel,self.Serial_ParityComboBox)
        
        self.Serial_RefreshBtn = QPushButton('????????????')
        self.Serial_OpenBtn = QPushButton(self.Openico,'????????????')
        self.Serial_Grid1.addWidget(self.Serial_RefreshBtn,0,0)
        self.Serial_Grid1.addWidget(self.Serial_OpenBtn,0,1)
        
        self.Serial_ShowTimeCheckBox = QCheckBox('????????????')
        self.Serial_ShowHintCheckBox = QCheckBox('????????????')
        self.Serial_ShowSendCheckBox = QCheckBox('????????????')
        self.Serial_ShowReceiveCheckBox = QCheckBox('????????????')
        self.Serial_ShowSendFlagCheckBox = QCheckBox('????????????')
        self.Serial_ShowSendFlagLineEdit = QLineEdit('-->')
        # self.Serial_ShowSendFlagLineEdit.setFixedWidth(70)
        # self.Serial_ShowSendFlagLineEdit = QComboBox()
        self.Serial_ShowReveiveFlagCheckBox = QCheckBox('????????????')
        self.Serial_ShowReceiveFlagLineEdit = QLineEdit('<--')
        # self.Serial_ShowReceiveFlagLineEdit.setFixedWidth(70)
        self.Serial_ShowSendHistroyCheckBox = QCheckBox('????????????')
        self.Serial_ShowWatchCheckBox = QCheckBox('????????????')
        self.Serial_ShowReplyCheckBox = QCheckBox('????????????')
        self.Serial_ShowAutoReplyCheckBox = QCheckBox('????????????')
        self.FlowViewBtn = QPushButton('????????????')

        # self.Serial_Grid2.setColumnStretch(0,1)
        # self.Serial_Grid2.setColumnStretch(1,5)
        self.Serial_Grid2.addWidget(self.Serial_ShowTimeCheckBox,0,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowHintCheckBox,1,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowSendCheckBox,2,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowReceiveCheckBox,3,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowSendFlagCheckBox,4,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowSendFlagLineEdit,4,1)
        self.Serial_Grid2.addWidget(self.Serial_ShowReveiveFlagCheckBox,5,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowReceiveFlagLineEdit,5,1)
        self.Serial_Grid2.addWidget(self.Serial_ShowSendHistroyCheckBox,6,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowWatchCheckBox,7,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowReplyCheckBox,8,0)
        self.Serial_Grid2.addWidget(self.Serial_ShowAutoReplyCheckBox,9,0)
        self.Serial_Grid2.addWidget(self.FlowViewBtn,10,0)


        self.Serial_SendBtn = QPushButton('??????')
        self.Serial_SaveBtn = QPushButton('????????????')
        self.Serial_ClearSendBtn = QPushButton('????????????')
        self.Serial_ClearReceiveBtn = QPushButton('????????????')
        self.SendConGrid.addWidget(self.Serial_SendBtn,0,0)
        self.SendConGrid.addWidget(self.Serial_SaveBtn,0,1)
        self.SendConGrid.addWidget(self.Serial_ClearSendBtn,1,0)
        self.SendConGrid.addWidget(self.Serial_ClearReceiveBtn,1,1)

        self.SendFun_HexShowCheckBox = QCheckBox('Hex??????')
        self.SendFun_HexSendCheckBox = QCheckBox('Hex??????')
        self.SendFun_OffsetCheckBox = QCheckBox('?????????')
        self.SendFun_OffsetSpinBox = QSpinBox()
        self.SendFun_OffsetSpinBox.setRange(0,1000)  
        self.SendFun_ReceiveDelayCheckBox = QCheckBox('????????????')
        self.SendFun_ReceiveDelaySpinBox = QSpinBox()
        self.SendFun_ReceiveDelaySpinBox.setRange(0,5000)
        self.SendFun_ReceiveDelayUnitLabel = QLabel('*10ms')
        self.SendFun_GuideCheckBox = QCheckBox('?????????')
        self.SendFun_GuideLineEdit = QLineEdit('')
        self.SendFun_EndCheckBox = QCheckBox('?????????')
        self.SendFun_EndLineEdit = QLineEdit('')
        self.SendFun_EntryEndCheckBox = QCheckBox('????????????')
        self.SendFun_CheckLabel = QLabel('??????')
        self.SendFun_CheckComboBox = QComboBox()
        self.SendFun_CheckComboBox.addItems(["?????????","????????????","CRC-IBML??????","CRC-IBMH??????","????????????","CRC-CCITTXModemL","CRC-CCITTXModemH","CRC-CCITT0xFFFFL","CRC-CCITT0xFFFFH","CRC-CCITT0x1D0FL","CRC-CCITT0x1D0FH","CRC-CCITTKermitL","CRC-CCITTKermitH"])
        self.SendFunGrid.addWidget(self.SendFun_HexShowCheckBox,0,0)
        self.SendFunGrid.addWidget(self.SendFun_HexSendCheckBox,1,0)
        self.SendFunGrid.addWidget(self.SendFun_CheckLabel,0,1)
        self.SendFunGrid.addWidget(self.SendFun_CheckComboBox,0,2,1,3)
        self.SendFunGrid.addWidget(self.SendFun_ReceiveDelayCheckBox,1,1,1,2)
        self.SendFunGrid.addWidget(self.SendFun_ReceiveDelaySpinBox,1,3)
        self.SendFunGrid.addWidget(self.SendFun_ReceiveDelayUnitLabel,1,4)
        self.SendFunGrid.addWidget(self.SendFun_OffsetCheckBox,0,5,1,1)
        self.SendFunGrid.addWidget(self.SendFun_OffsetSpinBox,0,6,1,1)
        self.SendFunGrid.addWidget(self.SendFun_EntryEndCheckBox,1,5,1,2)
        self.SendFunGrid.addWidget(self.SendFun_GuideCheckBox,0,7,1,1)
        self.SendFunGrid.addWidget(self.SendFun_GuideLineEdit,0,8,1,1)
        self.SendFunGrid.addWidget(self.SendFun_EndCheckBox,1,7,1,1)
        self.SendFunGrid.addWidget(self.SendFun_EndLineEdit,1,8,1,1)
        # self.SendFunGrid.setColumnStretch(3,1)
        # self.SendFunGrid.setColumnStretch(4,0)
        self.SendFun_HSpacer = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.SendFunGrid.addItem(self.SendFun_HSpacer,0,11,1,1)

        self.SendFun_AutoCheckBox = QCheckBox('??????')
        self.SendFun_AutoSpinBox = QSpinBox()
        self.SendFun_AutoSpinBox.setRange(1,500000)
        self.SendFun_AutoUnitLabel = QLabel('ms')
        self.SendFun_CountCheckBox = QCheckBox('??????')
        self.SendFun_CountSpinBox = QSpinBox()
        self.SendFun_CountSpinBox.setRange(1,50000)
        self.SendFun_CountUnitLabel = QLabel('')
        self.SendFunRightGrid.addWidget(self.SendFun_AutoCheckBox,0,0,1,1)
        self.SendFunRightGrid.addWidget(self.SendFun_AutoSpinBox,0,1,1,1)
        self.SendFunRightGrid.addWidget(self.SendFun_AutoUnitLabel,0,2,1,1)
        self.SendFunRightGrid.addWidget(self.SendFun_CountCheckBox,1,0,1,1)
        self.SendFunRightGrid.addWidget(self.SendFun_CountSpinBox,1,1,1,1)
        self.SendFunRightGrid.addWidget(self.SendFun_CountUnitLabel,1,2,1,1)

        self.SendCount_SendCountLineEdit = QLineEdit('')
        self.SendCount_SendCountLineEdit.setReadOnly(True)
        self.SendCount_SendCountLineEdit.setText('0')
        self.SendCount_SendCountClearBtn = QPushButton('????????????')
        self.SendCount_SendFrameLineEdit = QLineEdit('')
        self.SendCount_SendFrameLineEdit.setText('0')
        self.SendCount_SendFrameLineEdit.setReadOnly(True)
        self.SendCount_SendFrameClearBtn = QPushButton('????????????')
        self.SendCount_ReceiveCountLineEdit = QLineEdit('')
        self.SendCount_ReceiveCountLineEdit.setReadOnly(True)
        self.SendCount_ReceiveCountLineEdit.setText('0')
        self.SendCount_ReceiveCountClearBtn = QPushButton('????????????')
        self.SendCount_ReceiveFrameLineEdit = QLineEdit('')
        self.SendCount_ReceiveFrameLineEdit.setReadOnly(True)
        self.SendCount_ReceiveFrameLineEdit.setText('0')
        self.SendCount_ReceiveFrameClearBtn = QPushButton('????????????')
        # self.SendCountGrid.addWidget(self.SendCount_SendCountLineEdit,0,0,1,1)
        # self.SendCountGrid.addWidget(self.SendCount_SendCountClearBtn,0,1,1,1)
        # self.SendCountGrid.addWidget(self.SendCount_SendFrameLineEdit,0,2,1,1)
        # self.SendCountGrid.addWidget(self.SendCount_SendFrameClearBtn,0,3,1,1)
        # self.SendCountGrid.addWidget(self.SendCount_ReceiveCountLineEdit,0,4,1,1)
        # self.SendCountGrid.addWidget(self.SendCount_ReceiveCountClearBtn,0,5,1,1)
        # self.SendCountGrid.addWidget(self.SendCount_ReceiveFrameLineEdit,0,6,1,1)
        # self.SendCountGrid.addWidget(self.SendCount_ReceiveFrameClearBtn,0,7,1,1)
        # self.SendCount_HSpacer = QSpacerItem(100, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.SendCountGrid.addItem(self.SendCount_HSpacer,0,9,1,1)
        
        self.statusBar.addWidget(self.SendCount_SendCountLineEdit,1)
        self.statusBar.addWidget(self.SendCount_SendCountClearBtn,0)
        self.statusBar.addWidget(self.SendCount_SendFrameLineEdit,1)
        self.statusBar.addWidget(self.SendCount_SendFrameClearBtn,0)
        self.statusBar.addWidget(self.SendCount_ReceiveCountLineEdit,1)
        self.statusBar.addWidget(self.SendCount_ReceiveCountClearBtn,0)
        self.statusBar.addWidget(self.SendCount_ReceiveFrameLineEdit,1)
        self.statusBar.addWidget(self.SendCount_ReceiveFrameClearBtn,0)
        self.statusBar.addWidget(self.statusBar_ShowLabel,10)
        self.statusBar.addWidget(self.statusBar_TimeLabel,0)

        self.Watch_Frame = QFrame()
        self.Watch_FrameVBox = QVBoxLayout()
        self.Watch_FrameVBox.setContentsMargins(0,0,0,0)
        self.Watch_Frame.setLayout(self.Watch_FrameVBox)
        self.WatchVBox.addWidget(self.Watch_Frame)

        self.Watch_LineEdit = []
        for i in range(15):
            self.Watch_LineEdit.append('')
            self.Watch_LineEdit[i] = QLineEdit('')
            self.Watch_FrameVBox.addWidget(self.Watch_LineEdit[i])
        self.Watch_SetBtn = QPushButton('??????')
        self.Watch_FrameVBox.addWidget(self.Watch_SetBtn)

        # self.Watch_Main = QWidget(self.MainWindowCenter)

        # self.Watch_VSpacer = QSpacerItem(30, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.Watch_FrameVBox.addItem(self.Watch_VSpacer)

        self.Serial_OpenBtn.setStyleSheet(btnsty2)
        ??????????????????(self)

        ??????????????????(search_serial_conf,'SerialPort',self.Serial_SerialComboBox,'combobox','')
        ??????????????????(search_serial_conf,'SerialBurd',self.Serial_BuadComboBox,'combobox','2400')
        ??????????????????(search_serial_conf,'SerialByte',self.Serial_ByteComboBox,'combobox','8')
        ??????????????????(search_serial_conf,'SerialStop',self.Serial_StopComboBox,'combobox','1')
        ??????????????????(search_serial_conf,'SerialParity',self.Serial_ParityComboBox,'combobox','E')
        ??????????????????(search_serial_conf,'ShowTimeFlag',self.Serial_ShowTimeCheckBox,'check','1')
        ??????????????????(search_serial_conf,'ShowHintFlag',self.Serial_ShowHintCheckBox,'check','1')
        ??????????????????(search_serial_conf,'ShowSendFlag',self.Serial_ShowSendCheckBox,'check','1')
        ??????????????????(search_serial_conf,'ShowReceiveFlag',self.Serial_ShowReceiveCheckBox,'check','1')
        ??????????????????(search_serial_conf,'ShowSendMarkFlag',self.Serial_ShowSendFlagCheckBox,'check','1')
        ??????????????????(search_serial_conf,'ShowSendMark',self.Serial_ShowSendFlagLineEdit,'entry','>>>')
        ??????????????????(search_serial_conf,'ShowReceiveMarkFlag',self.Serial_ShowReveiveFlagCheckBox,'check','1')
        ??????????????????(search_serial_conf,'ShowReceiveMark',self.Serial_ShowReceiveFlagLineEdit,'entry','<<<')
        ??????????????????(search_serial_conf,'ShowHistoryFlag',self.Serial_ShowSendHistroyCheckBox,'check','0')
        ??????????????????(search_serial_conf,'ShowWatchFlag',self.Serial_ShowWatchCheckBox,'check','1')
        ??????????????????(search_serial_conf,'ShowReplyFlag',self.Serial_ShowReplyCheckBox,'check','0')
        ??????????????????(search_serial_conf,'HexShowFlag',self.SendFun_HexShowCheckBox,'check','1')
        ??????????????????(search_serial_conf,'HexSendFlag',self.SendFun_HexSendCheckBox,'check','1')
        ??????????????????(search_serial_conf,'Check',self.SendFun_CheckComboBox,'combobox','?????????')
        ??????????????????(search_serial_conf,'ReceiveDelayFlag',self.SendFun_ReceiveDelayCheckBox,'check','0')
        ??????????????????(search_serial_conf,'ReceiveDelayTime',self.SendFun_ReceiveDelaySpinBox,'spinbox','2')
        ??????????????????(search_serial_conf,'OffSetFlag',self.SendFun_OffsetCheckBox,'check','0')
        ??????????????????(search_serial_conf,'OffSet',self.SendFun_OffsetSpinBox,'spinbox','0')
        ??????????????????(search_serial_conf,'EntryFlag',self.SendFun_EntryEndCheckBox,'check','0')
        ??????????????????(search_serial_conf,'GuideFlag',self.SendFun_GuideCheckBox,'check','0')
        ??????????????????(search_serial_conf,'Guide',self.SendFun_GuideLineEdit,'entry','1')
        ??????????????????(search_serial_conf,'EndFlag',self.SendFun_EndCheckBox,'check','0')
        ??????????????????(search_serial_conf,'End',self.SendFun_EndLineEdit,'entry','')
        ??????????????????(search_serial_conf,'AutoTime',self.SendFun_AutoSpinBox,'spinbox','1000')
        ??????????????????(search_serial_conf,'AutoCountFlag',self.SendFun_CountCheckBox,'check','1')
        ??????????????????(search_serial_conf,'AutoCount',self.SendFun_CountSpinBox,'spinbox','0')
        ??????????????????(search_serial_conf,'Send',self.Send_TextEdit,'textedit','')
        ??????????????????(search_serial_conf,'ShowAutoReplyFlag',self.Serial_ShowAutoReplyCheckBox,'check','0')
        # ??????????????????(search_serial_conf,'ShowCcDataFlag',self.Serial_ShowCcDataCheckBox,'check','0')
        # ??????????????????(search_serial_conf,'ShowCcData',self.Serial_ShowCcDataLineEdit,'entry','    ')

        self.Serial_RefreshBtn.clicked.connect(lambda:??????????????????(self))
        self.Serial_OpenBtn.clicked.connect(lambda:??????(self))
        self.Serial_ClearReceiveBtn.clicked.connect(lambda:??????(self.Receive_TextEdit))
        self.Serial_ClearSendBtn.clicked.connect(lambda:??????(self.Send_TextEdit))
        self.Serial_SaveBtn.clicked.connect(lambda:??????(self))
        self.Serial_SerialComboBox.textActivated.connect(lambda:?????????????????????(self))
        self.Serial_BuadComboBox.textActivated.connect(lambda:????????????????????????(self))
        self.Serial_ByteComboBox.textActivated.connect(lambda:????????????????????????(self))
        self.Serial_StopComboBox.textActivated.connect(lambda:????????????????????????(self))
        self.Serial_ParityComboBox.textActivated.connect(lambda:????????????????????????(self))
        ??????(self)

        self.ShowWatch()
        self.HistroyFace()
        self.ReplyFace()
        self.ShowHistroy()
        self.ShowReply()

        self.SetMainwindow = SetMain()
        self.FlowViewWindow = FlowViewWidget()

        self.SendFun_AutoCheckBox.stateChanged.connect(lambda:????????????????????????(self))
        self.Histroy_AutoCheckBox.stateChanged.connect(lambda:????????????????????????(self))
        self.Serial_SendBtn.clicked.connect(lambda:????????????(self,-1))
        self.Serial_ShowWatchCheckBox.stateChanged.connect(lambda:self.ShowWatch())
        self.Serial_ShowSendHistroyCheckBox.stateChanged.connect(lambda:self.ShowHistroy())
        self.Serial_ShowReplyCheckBox.stateChanged.connect(lambda:self.ShowReply())

        self.SendCount_SendCountClearBtn.clicked.connect(lambda:???????????????(self,'?????????'))
        self.SendCount_SendFrameClearBtn.clicked.connect(lambda:???????????????(self,'?????????'))
        self.SendCount_ReceiveCountClearBtn.clicked.connect(lambda:???????????????(self,'?????????'))
        self.SendCount_ReceiveFrameClearBtn.clicked.connect(lambda:???????????????(self,'?????????'))

        self.Watch_SetBtn.clicked.connect(lambda:self.ShowSetMainWindow())
        self.FlowViewBtn.clicked.connect(lambda:self.ShowFlowViewWindow())

        self.Path = ????????????(search_serial_conf,'Path','')

        r=threading.Thread(target=????????????,args=(self,))
        r.setDaemon(True)
        r.start()

    def HistroyFace(self):
        self.Histroy_MainFrame = QFrame()
        self.Histroy_MainVBOX = QVBoxLayout(self.Histroy_MainFrame)
        self.Histroy_MainVBOX.setContentsMargins(0,0,0,0)

        self.Histroy_TopVBOX = QVBoxLayout()
        self.Histroy_BottomHBOX = QHBoxLayout()

        self.Histroy_ScrollArea = QScrollArea()

        self.Histroy_Frame = QFrame()
        # self.Histroy_Frame.setStyleSheet(u"background-color: #61cfa7;")
        # self.Histroy_ScrollArea.setMinimumSize(800,800)

        self.Histroy_Frame_VBOX = QVBoxLayout()
        self.Histroy_Frame.setLayout(self.Histroy_Frame_VBOX)

        self.Histroy_Frame_HBOX = []
        self.Histroy_Frame_SendBtn = []
        self.Histroy_Frame_SendTextEdit = []
        self.Histroy_Frame_SendCheckBox = []
        self.Histroy_Frame_SendLabel = []
        self.Histroy_Frame_SendLineEdit = []
        for i in range(500):
            self.Histroy_Frame_HBOX.append('')
            self.Histroy_Frame_SendBtn.append('')
            self.Histroy_Frame_SendTextEdit.append('')
            self.Histroy_Frame_SendCheckBox.append('')
            self.Histroy_Frame_SendLabel.append('')
            self.Histroy_Frame_SendLineEdit.append('')
            self.Histroy_Frame_HBOX[i] = QHBoxLayout()
            self.Histroy_Frame_SendBtn[i] = QPushButton('<')
            # self.Histroy_Frame_SendBtn[i].setMinimumSize(QSize(20, 20))
            # self.Histroy_Frame_SendBtn[i].setMaximumSize(QSize(20, 20))
            # # self.Histroy_Frame_SendBtn[i].setContentsMargins(0,0,0,0)
            # self.Histroy_Frame_SendBtn[i].setFont([10])
            self.Histroy_Frame_SendTextEdit[i] = QTextEdit()
            self.Histroy_Frame_SendTextEdit[i].setMinimumSize(QSize(520, 25))
            self.Histroy_Frame_SendTextEdit[i].setMaximumSize(QSize(1677215, 25))
            self.Histroy_Frame_SendCheckBox[i] = QCheckBox()
            self.Histroy_Frame_SendLabel[i] = QLabel('??????'+str(i+1).zfill(3)+':')
            self.Histroy_Frame_SendLineEdit[i] = QLineEdit()

            self.Histroy_Frame_HBOX[i].addWidget(self.Histroy_Frame_SendBtn[i])
            self.Histroy_Frame_HBOX[i].addWidget(self.Histroy_Frame_SendTextEdit[i])
            self.Histroy_Frame_HBOX[i].addWidget(self.Histroy_Frame_SendCheckBox[i])
            self.Histroy_Frame_HBOX[i].addWidget(self.Histroy_Frame_SendLabel[i])
            self.Histroy_Frame_HBOX[i].addWidget(self.Histroy_Frame_SendLineEdit[i])

            self.Histroy_Frame_HBOX[i].setStretch(1,8)
            self.Histroy_Frame_HBOX[i].setStretch(4,2)

            self.Histroy_Frame_VBOX.addLayout(self.Histroy_Frame_HBOX[i])

            ??????????????????(search_serial_conf,'HistroySend'+str(i+1),self.Histroy_Frame_SendTextEdit[i],'textedit','')
            ??????????????????(search_serial_conf,'HistroyCheck'+str(i+1),self.Histroy_Frame_SendCheckBox[i],'check','0')
            ??????????????????(search_serial_conf,'HistroyText'+str(i+1),self.Histroy_Frame_SendLineEdit[i],'entry','')

            self.Histroy_Frame_SendBtn[i].clicked.connect(partial(????????????,self,i))

        # self.Histroy_Frame_VSpacer = QSpacerItem(0, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.Histroy_Frame_VBOX.addItem(self.Histroy_Frame_VSpacer)

        self.Histroy_ScrollArea.setWidget(self.Histroy_Frame)
        self.Histroy_TopVBOX.addWidget(self.Histroy_ScrollArea)

        self.Histroy_AutoCheckBox = QCheckBox('????????????')
        self.Histroy_AutoSpinBox = QSpinBox()
        self.Histroy_AutoSpinBox.setRange(1,500000)
        self.Histroy_AutoLabel = QLabel('ms')
        self.Histroy_BottomHBOX.addWidget(self.Histroy_AutoCheckBox)
        self.Histroy_BottomHBOX.addWidget(self.Histroy_AutoSpinBox)
        self.Histroy_BottomHBOX.addWidget(self.Histroy_AutoLabel)

        self.Histroy_Frame_VSpacer = QSpacerItem(600, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.Histroy_BottomHBOX.addItem(self.Histroy_Frame_VSpacer)

        self.Histroy_MainVBOX.addLayout(self.Histroy_TopVBOX)
        self.Histroy_MainVBOX.setStretch(0,1)
        self.Histroy_MainVBOX.addLayout(self.Histroy_BottomHBOX)

        self.HistroyVBox.addWidget(self.Histroy_MainFrame)

    def ReplyFace(self):
        self.Reply_MainFrame = QFrame()
        self.Reply_MainVBOX = QVBoxLayout(self.Reply_MainFrame)
        self.Reply_MainVBOX.setContentsMargins(0,0,0,0)

        self.Reply_TopVBOX = QVBoxLayout()
        self.Reply_BottomHBOX = QHBoxLayout()

        self.Reply_ScrollArea = QScrollArea()

        self.Reply_Frame = QFrame()
        self.Reply_ScrollArea.setMinimumSize(800,800)

        self.Reply_Frame_Grid = QGridLayout()
        self.Reply_Frame.setLayout(self.Reply_Frame_Grid)

        self.Reply_V3ReadAddCheckBox = QCheckBox('V3?????????')
        self.Reply_V3ReadAddLineEdit = QLineEdit('')
        self.Reply_V3ReadAddLineEdit.setInputMask(">hhhhhhhhhhhhhh")

        self.Reply_V5CheckBox = QCheckBox('V5')

        self.Reply_V3WriteAddCheckBox = QCheckBox('V3?????????')
        self.Reply_V3WriteAddLineEdit = QLineEdit()
        self.Reply_V3WriteAddLineEdit.setInputMask(">HHHHHHHHHHHHHH")
        self.Reply_V3WriteTimeCheckBox = QCheckBox('V3?????????')
        self.Reply_V3WriteDataCheckBox = QCheckBox('V3?????????')
        self.Reply_V3ReadAllDataCheckBox = QCheckBox('V3???????????????')

        self.Reply_V3AccountHeatLabel = QLabel('???????????????')
        self.Reply_V3AccountHeatDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3AccountHeatDoubleSpinBox.setRange(0,999999.99)
        self.Reply_V3AccountHeatComboBox = QComboBox()
        self.Reply_V3AccountHeatComboBox.addItems(['kWh','MWh'])

        self.Reply_V3TotalHeatLabel = QLabel('????????????')
        self.Reply_V3TotalHeatDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3TotalHeatDoubleSpinBox.setRange(0,999999.99)
        self.Reply_V3TotalHeatComboBox = QComboBox()
        self.Reply_V3TotalHeatComboBox.addItems(['kWh','MWh'])

        self.Reply_V3TotalFlowLabel = QLabel('????????????')
        self.Reply_V3TotalFlowDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3TotalFlowDoubleSpinBox.setRange(0,999999.99)
        self.Reply_V3TotalFlowUnitLabel = QLabel('m??')

        self.Reply_V3AccountColdLabel = QLabel('???????????????')
        self.Reply_V3AccountColdDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3AccountColdDoubleSpinBox.setRange(0,999999.99)
        self.Reply_V3AccountColdComboBox = QComboBox()
        self.Reply_V3AccountColdComboBox.addItems(['kWh','MWh'])

        self.Reply_V3TotalColdLabel = QLabel('????????????')
        self.Reply_V3TotalColdDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3TotalColdDoubleSpinBox.setRange(0,999999.99)
        self.Reply_V3TotalColdComboBox = QComboBox()
        self.Reply_V3TotalColdComboBox.addItems(['kWh','MWh'])

        self.Reply_V3PowerLabel = QLabel('??????')
        self.Reply_V3PowerDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3PowerDoubleSpinBox.setRange(0,999999.99)
        self.Reply_V3PowerComboBox = QComboBox()
        self.Reply_V3PowerComboBox.addItems(['kW','MW'])

        self.Reply_V3TotalFlowRateLabel = QLabel('??????')
        self.Reply_V3TotalFlowRateDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3TotalFlowRateDoubleSpinBox.setRange(0,9999.9999)
        self.Reply_V3TotalFlowRateUnitLabel = QLabel('m??/h')

        self.Reply_V3TotalWorkTimeLabel = QLabel('????????????')
        self.Reply_V3TotalWorkTimeSpinBox = QSpinBox()
        self.Reply_V3TotalWorkTimeSpinBox.setRange(0,99999999)
        self.Reply_V3TotalWorkTimeUnitLabel = QLabel('h')

        self.Reply_V3TotalAlarmTimeLabel = QLabel('????????????')
        self.Reply_V3TotalAlarmTimeSpinBox = QSpinBox()
        self.Reply_V3TotalAlarmTimeSpinBox.setRange(0,99999999)
        self.Reply_V3TotalAlarmTimeUnitLabel = QLabel('h')

        self.Reply_V3TotalInTempLabel = QLabel('????????????')
        self.Reply_V3TotalInTempDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3TotalInTempDoubleSpinBox.setRange(0.00,150.00)
        self.Reply_V3TotalInTempUnitLabel = QLabel('???')

        self.Reply_V3TotalOutTempLabel = QLabel('????????????')
        self.Reply_V3TotalOutTempDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3TotalOutTempDoubleSpinBox.setRange(-50.00,150.00)
        self.Reply_V3TotalOutTempUnitLabel = QLabel('???')

        self.Reply_V3TotalAccountFlowLabel = QLabel('????????????')
        self.Reply_V3TotalAccountFlowDoubleSpinBox = QDoubleSpinBox()
        self.Reply_V3TotalAccountFlowDoubleSpinBox.setRange(0,999999.99)
        self.Reply_V3TotalAccountFlowUnitLabel = QLabel('m??')

        self.Reply_V3InstallTypeLabel = QLabel('????????????')
        self.Reply_V3InstallTypeComboBox = QComboBox()
        self.Reply_V3InstallTypeComboBox.addItems(['??????','??????'])

        self.Reply_V3FlowDriectionLabel = QLabel('????????????')
        self.Reply_V3FlowDriectionComboBox = QComboBox()
        self.Reply_V3FlowDriectionComboBox.addItems(['??????','??????'])

        self.Reply_V3VoltageLabel = QLabel('????????????')
        self.Reply_V3VoltageComboBox = QComboBox()
        self.Reply_V3VoltageComboBox.addItems(["??????","??????"])

        self.Reply_V3TempDifLabel = QLabel('??????')
        self.Reply_V3TempDifComboBox = QComboBox()
        self.Reply_V3TempDifComboBox.addItems(["???>???","???>???"])

        self.Reply_V3BlankPipeLabel = QLabel('??????')
        self.Reply_V3BlankPipeComboBox = QComboBox()
        self.Reply_V3BlankPipeComboBox.addItems(["??????","??????"])

        self.Reply_V3TempErrorLabel = QLabel('????????????')
        self.Reply_V3TempErrorComboBox = QComboBox()
        self.Reply_V3TempErrorComboBox.addItems(["??????","??????"])

        self.Reply_V3TimeLabel = QLabel('??????')
        self.Reply_V3TimeDateEdit=QDateTimeEdit(QDateTime.currentDateTime())
        self.Reply_V3TimeDateEdit.setDisplayFormat('yyyy-MM-dd dddd HH:mm:ss')
        self.Reply_V3TimeDateEdit.setCalendarPopup(True)
        
        self.Reply_Frame_Grid.addWidget(self.Reply_V3ReadAddCheckBox,0,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3ReadAddLineEdit,0,1,1,2)
        self.Reply_Frame_Grid.addWidget(self.Reply_V5CheckBox,0,3)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3WriteAddCheckBox,1,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3WriteAddLineEdit,1,1,1,2)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3WriteTimeCheckBox,2,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3WriteDataCheckBox,3,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3ReadAllDataCheckBox,4,0,1,2)

        self.Reply_Frame_Grid.addWidget(self.Reply_V3AccountHeatLabel,5,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3AccountHeatDoubleSpinBox,5,1)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3AccountHeatComboBox,5,2)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalHeatLabel,5,3)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalHeatDoubleSpinBox,5,4)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalHeatComboBox,5,5)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalFlowLabel,5,6)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalFlowDoubleSpinBox,5,7)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalFlowUnitLabel,5,8)

        self.Reply_Frame_Grid.addWidget(self.Reply_V3AccountColdLabel,6,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3AccountColdDoubleSpinBox,6,1)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3AccountColdComboBox,6,2)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalColdLabel,6,3)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalColdDoubleSpinBox,6,4)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalColdComboBox,6,5)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3PowerLabel,6,6)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3PowerDoubleSpinBox,6,7)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3PowerComboBox,6,8)

        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalFlowRateLabel,7,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalFlowRateDoubleSpinBox,7,1)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalFlowRateUnitLabel,7,2)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalWorkTimeLabel,7,3)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalWorkTimeSpinBox,7,4)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalWorkTimeUnitLabel,7,5)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalAlarmTimeLabel,7,6)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalAlarmTimeSpinBox,7,7)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalAlarmTimeUnitLabel,7,8)

        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalInTempLabel,8,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalInTempDoubleSpinBox,8,1)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalInTempUnitLabel,8,2)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalOutTempLabel,8,3)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalOutTempDoubleSpinBox,8,4)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalOutTempUnitLabel,8,5)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalAccountFlowLabel,8,6)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalAccountFlowDoubleSpinBox,8,7)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TotalAccountFlowUnitLabel,8,8)

        self.Reply_Frame_Grid.addWidget(self.Reply_V3InstallTypeLabel,9,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3InstallTypeComboBox,9,1)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3FlowDriectionLabel,9,3)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3FlowDriectionComboBox,9,4)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3VoltageLabel,9,6)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3VoltageComboBox,9,7)

        self.Reply_Frame_Grid.addWidget(self.Reply_V3TempDifLabel,10,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TempDifComboBox,10,1)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3BlankPipeLabel,10,3)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3BlankPipeComboBox,10,4)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TempErrorLabel,10,6)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TempErrorComboBox,10,7)

        self.Reply_Frame_Grid.addWidget(self.Reply_V3TimeLabel,11,0)
        self.Reply_Frame_Grid.addWidget(self.Reply_V3TimeDateEdit,11,1,1,3)

        # self.Reply_Frame_VSpacer = QSpacerItem(0, 600, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.Reply_Frame_Grid.addItem(self.Reply_Frame_VSpacer)

        self.Reply_ScrollArea.setWidget(self.Reply_Frame)
        self.Reply_TopVBOX.addWidget(self.Reply_ScrollArea)

        self.Reply_SelReplyCheckBox = QCheckBox('????????????')
        self.Reply_BottomHBOX.addWidget(self.Reply_SelReplyCheckBox)

        self.Reply_Frame_VSpacer = QSpacerItem(600, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.Reply_BottomHBOX.addItem(self.Reply_Frame_VSpacer)

        self.Reply_MainVBOX.addLayout(self.Reply_TopVBOX)
        self.Reply_MainVBOX.addLayout(self.Reply_BottomHBOX)

        self.HistroyVBox.addWidget(self.Reply_MainFrame)

    def ShowSetMainWindow(self):
        pos = self.Watch_SetBtn.geometry()
        pos1 = self.Watch_Frame.geometry()
        pos2 = self.geometry()
        x = pos.x()+pos1.x()+pos2.x()
        y = pos.y()+pos1.y()+pos2.y()
        self.SetMainwindow.showSetMain(x,y)

    def ShowFlowViewWindow(self):
        pos = self.FlowViewBtn.geometry()
        pos1 = self.Watch_Frame.geometry()
        pos2 = self.geometry()
        x = pos.x()+pos1.x()+pos2.x()
        y = pos.y()+pos1.y()+pos2.y()
        self.FlowViewWindow.showFlowView(x,y)

    def ShowHistroy(self):
        if self.Serial_ShowSendHistroyCheckBox.isChecked() == 1:
            self.Serial_ShowReplyCheckBox.setCheckState(Qt.Unchecked)
            # self.Histroy_MainFrame.show()
            self.Histroy_MainFrame.setVisible(True)
        else:
            # self.BaseWinGrid.setSizeConstraint(self.setMinimumSize())
            # self.Histroy_MainFrame.hide()
            self.Histroy_MainFrame.setVisible(False)
            # pos = self.geometry()
            # width = pos.width()
            # height = pos.height()
            # width1 = self.Histroy_MainFrame.width()
            # self.setGeometry(pos.x(),pos.y(),width-width1,height)
            # self.resize(self.minimumSizeHint())
            # self.adjustSize()
            # self.resize(800,400)

    def ShowReply(self):
        if self.Serial_ShowReplyCheckBox.isChecked() == 1:
            self.Serial_ShowSendHistroyCheckBox.setCheckState(Qt.Unchecked)
            self.Reply_MainFrame.show()
        else:
            self.Reply_MainFrame.hide()

    def ShowWatch(self):
        if self.Serial_ShowWatchCheckBox.isChecked() == 1:
            self.Watch_Frame.show()
        else:
            self.Watch_Frame.hide()

    def SpinBoxDo(self,ui,dict):
        if 'state' in dict:
            ui.setEnabled(dict['state'])

    def CheckBoxDo(self,ui,dict):
        if 'checkState' in dict:
            if dict['checkState'] == 'check':
                ui.setCheckState(Qt.Checked)
            elif dict['checkState'] == 'unCheck':
                ui.setCheckState(Qt.Unchecked)
        if 'state' in dict:
            ui.setEnabled(dict['state'])

    def LabelDo(self,ui,dict):
        if 'text' in dict:
            ui.setText(dict['text'])

    def LineEditDo(self,ui,dict):
        if 'text' in dict:
            ui.setText(dict['text'])
    
    def TextEditDo(self,ui,dict):
        bar = ui.verticalScrollBar()
        oldpos = ui.verticalScrollBar().sliderPosition()
        # oldcursor = ui.textCursor().position()
        oldcursor = ui.textCursor()
        if oldpos == bar.maximum():
            scroll = 1
        else:
            scroll = 0
            # ui.verticalScrollBar().maximum()
        ui.moveCursor(QTextCursor.End)
        if 'textColor' in dict:
            ui.setTextColor(dict['textColor'])
        else:
            ui.setTextColor('Black')
        if dict['insertType'] == 'append':
            ui.append(dict['text'])
        elif dict['insertType'] == 'insertPlainText':
            ui.insertPlainText(dict['text'])
        ui.setTextCursor(oldcursor)
        if scroll == 1:
            bar.setValue(bar.maximum())
        else:
            bar.setValue(oldpos)
        # bar.rangeChanged.connect(lambda x,y: bar.setValue(y)) 

    def PushButtonDo(self,ui,dict):
        ui.setText(dict['text'])
        ui.setIcon(dict['icon'])
        ui.setStyleSheet(dict['styleSheet'])

    # def paintEvent(self,event):
    #     self.MainWindowBackDropLabel.resize(self.MainWindowCenter.width(),self.MainWindowCenter.height())#-self.StatusBar.height()
    
    def save(self):
        djdata=sqlite3.connect('SerialTool.db') 
        cursor = djdata.cursor()
        try:
            SerialPort = self.Serial_SerialComboBox.currentText()
            SerialBurd = self.Serial_BuadComboBox.currentText()
            SerialByte = self.Serial_ByteComboBox.currentText()
            SerialStop = self.Serial_StopComboBox.currentText()
            SerialParity = self.Serial_ParityComboBox.currentText()
            ShowTimeFlag = str(self.Serial_ShowTimeCheckBox.isChecked())
            ShowHintFlag = str(self.Serial_ShowHintCheckBox.isChecked())
            ShowSendFlag = str(self.Serial_ShowSendCheckBox.isChecked())
            ShowReceiveFlag = str(self.Serial_ShowReceiveCheckBox.isChecked())
            ShowSendMarkFlag = str(self.Serial_ShowSendFlagCheckBox.isChecked())
            ShowSendMark = self.Serial_ShowSendFlagLineEdit.text()
            ShowReceiveMarkFlag = str(self.Serial_ShowReveiveFlagCheckBox.isChecked())
            ShowReceiveMark = self.Serial_ShowReceiveFlagLineEdit.text()
            ShowHistoryFlag = str(self.Serial_ShowSendHistroyCheckBox.isChecked())
            ShowWatchFlag = str(self.Serial_ShowWatchCheckBox.isChecked())
            ShowAutoReplyFlag = str(self.Serial_ShowAutoReplyCheckBox.isChecked())
            ShowReplyFlag = str(self.Serial_ShowReplyCheckBox.isChecked())
            HexSendFlag = str(self.SendFun_HexSendCheckBox.isChecked())
            HexShowFlag = str(self.SendFun_HexShowCheckBox.isChecked())
            Check = self.SendFun_CheckComboBox.currentText()
            ReceiveDelayFlag = str(self.SendFun_ReceiveDelayCheckBox.isChecked())
            ReceiveDelayTime = str(self.SendFun_ReceiveDelaySpinBox.value())
            OffSetFlag = str(self.SendFun_OffsetCheckBox.isChecked())
            OffSet = str(self.SendFun_OffsetSpinBox.value())
            EntryFlag = str(self.SendFun_EntryEndCheckBox.isChecked())
            GuideFlag = str(self.SendFun_GuideCheckBox.isChecked())
            Guide = self.SendFun_GuideLineEdit.text()
            EndFlag = str(self.SendFun_EndCheckBox.isChecked())
            End = self.SendFun_EndLineEdit.text()
            AutoTime = str(self.SendFun_AutoSpinBox.value())
            AutoCountFlag = str(self.SendFun_CountCheckBox.isChecked())
            AutoCount = str(self.SendFun_CountSpinBox.value())
            Send = self.Send_TextEdit.toPlainText()

            watch = []
            for i in range(15):
                a = str(self.SetMainwindow.WatchSet_Offset_SpinBox[i].value())
                watch.append(('WatchOffset'+str(i+1),a))
                a = self.SetMainwindow.WatchSet_DataType_ComboBox[i].currentText()
                watch.append(('WatchDataType'+str(i+1),a))
                a = self.SetMainwindow.WatchSet_CalType_ComboBox[i].currentText()
                watch.append(('WatchCalType'+str(i+1),a))

            histroy = []
            for i in range(500):
                a = self.Histroy_Frame_SendTextEdit[i].toPlainText()
                histroy.append(('HistroySend'+str(i+1),a))
                a = str(self.Histroy_Frame_SendCheckBox[i].isChecked())
                histroy.append(('HistroyCheck'+str(i+1),a))
                a = self.Histroy_Frame_SendLineEdit[i].text()
                histroy.append(('HistroyText'+str(i+1),a))

            init_save = [
                            ("SerialPort",SerialPort),
                            ("SerialBurd",SerialBurd),
                            ("SerialByte",SerialByte),
                            ("SerialStop",SerialStop),
                            ("SerialParity",SerialParity),
                            ("ShowTimeFlag",ShowTimeFlag),
                            ("ShowHintFlag",ShowHintFlag),
                            ("ShowSendFlag",ShowSendFlag),
                            ("ShowReceiveFlag",ShowReceiveFlag),
                            ("ShowSendMarkFlag",ShowSendMarkFlag),
                            ("ShowSendMark",ShowSendMark),
                            ("ShowReceiveMarkFlag",ShowReceiveMarkFlag),
                            ("ShowReceiveMark",ShowReceiveMark),
                            ("ShowHistoryFlag",ShowHistoryFlag),
                            ("ShowWatchFlag",ShowWatchFlag),
                            ("ShowReplyFlag",ShowReplyFlag),
                            ("ShowAutoReplyFlag",ShowAutoReplyFlag),
                            ("HexSendFlag",HexSendFlag),
                            ("HexShowFlag",HexShowFlag),
                            ("Check",Check),
                            ("ReceiveDelayFlag",ReceiveDelayFlag),
                            ("ReceiveDelayTime",ReceiveDelayTime),
                            ("OffSetFlag",OffSetFlag),
                            ("OffSet",OffSet),
                            ("EntryFlag",EntryFlag),
                            ("GuideFlag",GuideFlag),
                            ("Guide",Guide),
                            ("EndFlag",EndFlag),
                            ("End",End),
                            ("AutoTime",AutoTime),
                            ("AutoCountFlag",AutoCountFlag),
                            ("AutoCount",AutoCount),
                            ("Send",Send),
                            ("Path",self.Path),
                        ]
            init_save += (watch)
            init_save += (histroy)

            for i in range(len(init_save)):
                cursor.execute("select * from table_serial_conf where portname = (?) " ,(init_save[i][0],))#limit?????????????????????????????? limit %d,1"%i
                search_line=cursor.fetchall()
                if search_line != []:
                    if init_save[i][0] == search_line[0][0]:
                        cursor.execute("update table_serial_conf set portvalue=(?) where portname =(?)",(init_save[i][1],init_save[i][0]))              #????????????
                    else:
                        cursor.execute("update table_serial_conf set portname=(?),portvalue=(?) where rowid in(select rowid from table_serial_conf limit %d,1)"%i,(init_save[i][0],init_save[i][1]))              #????????????
                else:
                    cursor.execute('insert into table_serial_conf values(?,?)',(init_save[i][0],init_save[i][1]))

        except Exception as e:
            self.Receive_TextEdit.append(traceback.format_exc()+'\n')
            

        djdata.commit()   #???????????????commit???
        djdata.close()

    def closeEvent(self, event):
        # message???????????????
        # Are you sure to quit???????????????????
        # QMessageBox.Yes | QMessageBox.No??????????????????
        # QMessageBox.No?????????????????????NO???
        # reply = QMessageBox.question(self, 'Message',
        #                                 "Are you sure to quit?",
        #                                 QMessageBox.Yes |
        #                                 QMessageBox.No,
        #                                 QMessageBox.No)
        # # ????????????????????????????????????
        # if reply == QMessageBox.Yes:
        #     self.save()
        #     event.accept()
        # else:
        #     event.ignore()
        self.save()
        self.SetMainwindow.close()

    def mousePressEvent(self,event):
        self.SetMainwindow.hideSetMain()

class MainWindow(QMainWindow,Test):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI(self)

class SetMain(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(600,500)   
        self.setWindowIcon(QPixmap(Ico))
        self.setWindowTitle('??????')   

        self.setStyleSheet("QPushButton{background:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123));\
                                        border:1px groove gray;\
                                        border-radius:3px;\
                                        border-style:outset;\
                                        font:14px;\
                                        padding:1px 3px 1px 3px;\
                                        color:white} \
                            QPushButton:pressed{border:2px solid gray} \
                            QPushButton:hover{background:qlineargradient(x1:1, y1:1, x2:0, y2:0,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123));}\
                            QTextEdit:hover {background-color: #8cddb9;}\
                            QLineEdit {width: 60px;}\
                            QLineEdit:hover {background-color: #8cddb9;}\
                            QCheckBox:hover {background-color: #8cddb9;}\
                            QSpinBox:hover {background-color: #8cddb9;}\
                            QComboBox:hover {background-color: #8cddb9;}\
                            ")
                            # background-image: url(':pubu.jpg');\
                            # QPushButton:flat {border:2px solid red;}
                            # QPushButton:open{background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}\
                            # QPushButton::menu-indicator {image:url(:/images/close.png);image:none; subcontrol-origin:padding; subcontrol-position:bottom right;}\
                            # QPushButton::menu-indicator:pressed,QPushButton::menu-indicator:open {position:relative; top:4px; left:4px; }

        #??????????????????
        # self.MainWindowCenter = QWidget()
        self.MainGridLayout = QVBoxLayout(self)
        self.MainGridLayout.setSpacing(0)
        self.MainGridLayout.setContentsMargins(0, 0, 0, 0)#?????????0

        self.MainGridLayout1 = QGridLayout()
        self.MainGridLayout1.setSpacing(5)
        self.MainGridLayout1.setContentsMargins(10, 10, 10, 10)#?????????0

        self.MainGridLayout2 = QHBoxLayout()
        self.MainGridLayout2.setSpacing(0)
        self.MainGridLayout2.setContentsMargins(10, 0, 10, 10)#?????????0
        self.MainGridLayout.addLayout(self.MainGridLayout1)
        self.MainGridLayout.addLayout(self.MainGridLayout2)

        self.WatchSet_Offset_Label = []
        self.WatchSet_Offset_SpinBox = []
        self.WatchSet_DataType_Label = []
        self.WatchSet_DataType_ComboBox = []
        self.WatchSet_CalType_Label = []
        self.WatchSet_CalType_ComboBox = []
        self.WatchSet_FormLayout1 = []
        self.WatchSet_FormLayout2 = []
        self.WatchSet_FormLayout3 = []
        for i in range(15):
            self.WatchSet_Offset_Label.append('')
            self.WatchSet_Offset_SpinBox.append('')
            self.WatchSet_DataType_Label.append('')
            self.WatchSet_DataType_ComboBox.append('')
            self.WatchSet_CalType_Label.append('')
            self.WatchSet_CalType_ComboBox.append('')
            self.WatchSet_FormLayout1.append('')
            self.WatchSet_FormLayout2.append('')
            self.WatchSet_FormLayout3.append('')
            self.WatchSet_Offset_Label[i] = QLabel('??????:')
            self.WatchSet_DataType_Label[i] = QLabel('????????????:')
            self.WatchSet_CalType_Label[i] = QLabel('????????????:')
            self.WatchSet_Offset_SpinBox[i] = QSpinBox()
            self.WatchSet_Offset_SpinBox[i].setRange(0,1000)
            self.WatchSet_DataType_ComboBox[i] = QComboBox()
            self.WatchSet_DataType_ComboBox[i].addItems(["UINT8","UINT16","UINT32","INT8","INT16","INT32","BIN8","BIN16","FLOAT","CHAR"])
            self.WatchSet_CalType_ComboBox[i] = QComboBox()
            
            self.WatchSet_FormLayout1[i] = QFormLayout()
            self.WatchSet_FormLayout2[i] = QFormLayout()
            self.WatchSet_FormLayout3[i] = QFormLayout()

            self.WatchSet_FormLayout1[i].addRow(self.WatchSet_Offset_Label[i],self.WatchSet_Offset_SpinBox[i],)
            self.WatchSet_FormLayout2[i].addRow(self.WatchSet_DataType_Label[i],self.WatchSet_DataType_ComboBox[i],)
            self.WatchSet_FormLayout3[i].addRow(self.WatchSet_CalType_Label[i],self.WatchSet_CalType_ComboBox[i],)
            
            self.MainGridLayout1.addLayout(self.WatchSet_FormLayout1[i],i,0)
            self.MainGridLayout1.addLayout(self.WatchSet_FormLayout2[i],i,1)
            self.MainGridLayout1.addLayout(self.WatchSet_FormLayout3[i],i,2)

            ??????????????????(search_serial_conf,'WatchOffset'+str(i+1),self.WatchSet_Offset_SpinBox[i],'spinbox','0')
            ??????????????????(search_serial_conf,'WatchDataType'+str(i+1),self.WatchSet_DataType_ComboBox[i],'combobox','1')

            self.??????????????????(i,'')

            # self.WatchSet_DataType_ComboBox[i].textActivated.connect(handlerAdaptor(self.??????????????????,index = i))
            self.WatchSet_DataType_ComboBox[i].textActivated.connect(partial(self.??????????????????,i))

        self.Watch_ConfirmBtn = QPushButton('??????',self)
        self.MainGridLayout2.addWidget(self.Watch_ConfirmBtn)

        self.Watch_ConfirmBtn.clicked.connect(lambda:self.hideSetMain())

    def ??????????????????(self,index,event):
        self.WatchSet_CalType_ComboBox[index].clear()
        dataType = self.WatchSet_DataType_ComboBox[index].currentText()
        if dataType == 'UINT8' or dataType == 'INT8' or dataType =='CHAR' or dataType == 'BIN8':
            self.WatchSet_CalType_ComboBox[index].addItems(["NONE"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText("NONE")
        elif dataType=='UINT16' or dataType=='INT16' or dataType=='BIN16':
            self.WatchSet_CalType_ComboBox[index].addItems(["12","21"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText('21')
        elif dataType=='UINT32' or dataType=='INT32':
            self.WatchSet_CalType_ComboBox[index].addItems(["1234","4321","3412","2143"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText('3412')
        elif dataType=='FLOAT':
            self.WatchSet_CalType_ComboBox[index].addItems(["1234","4321","3412","2143"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText('4321')

    def showSetMain(self,x,y):
        if self.isVisible():#???????????????????????? is not None????????????????????????
            self.hide()
        else:
            self.show()
        self.move(x-self.width()-5,y-self.height())

    def hideSetMain(self):
        self.hide()

    def closeEvent(self, event):
        self.hideSetMain()

class FlowViewWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(600,500)   
        self.setWindowIcon(QPixmap(Ico))
        self.setWindowTitle('????????????')   

        self.setStyleSheet("QPushButton{background:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123));\
                                        border:1px groove gray;\
                                        border-radius:3px;\
                                        border-style:outset;\
                                        font:14px;\
                                        padding:1px 3px 1px 3px;\
                                        color:white} \
                            QPushButton:pressed{border:2px solid gray} \
                            QPushButton:hover{background:qlineargradient(x1:1, y1:1, x2:0, y2:0,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123));}\
                            QTextEdit:hover {background-color: #8cddb9;}\
                            QLineEdit {width: 60px;}\
                            QLineEdit:hover {background-color: #8cddb9;}\
                            QCheckBox:hover {background-color: #8cddb9;}\
                            QSpinBox:hover {background-color: #8cddb9;}\
                            QComboBox:hover {background-color: #8cddb9;}\
                            ")
                            # background-image: url(':pubu.jpg');\
                            # QPushButton:flat {border:2px solid red;}
                            # QPushButton:open{background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}\
                            # QPushButton::menu-indicator {image:url(:/images/close.png);image:none; subcontrol-origin:padding; subcontrol-position:bottom right;}\
                            # QPushButton::menu-indicator:pressed,QPushButton::menu-indicator:open {position:relative; top:4px; left:4px; }

        #??????????????????
        # self.MainWindowCenter = QWidget()
        self.MainGridLayout = QVBoxLayout(self)
        self.MainGridLayout.setSpacing(0)
        self.MainGridLayout.setContentsMargins(0, 0, 0, 0)#?????????0

        self.MainGridLayout1 = QGridLayout()
        self.MainGridLayout1.setSpacing(5)
        self.MainGridLayout1.setContentsMargins(10, 10, 10, 10)#?????????0

        self.MainGridLayout2 = QHBoxLayout()
        self.MainGridLayout2.setSpacing(0)
        self.MainGridLayout2.setContentsMargins(10, 0, 10, 10)#?????????0
        self.MainGridLayout.addLayout(self.MainGridLayout1)
        self.MainGridLayout.addLayout(self.MainGridLayout2)

        self.WatchSet_Offset_Label = []
        self.WatchSet_Offset_SpinBox = []
        self.WatchSet_DataType_Label = []
        self.WatchSet_DataType_ComboBox = []
        self.WatchSet_CalType_Label = []
        self.WatchSet_CalType_ComboBox = []
        self.WatchSet_FormLayout1 = []
        self.WatchSet_FormLayout2 = []
        self.WatchSet_FormLayout3 = []
        for i in range(15):
            self.WatchSet_Offset_Label.append('')
            self.WatchSet_Offset_SpinBox.append('')
            self.WatchSet_DataType_Label.append('')
            self.WatchSet_DataType_ComboBox.append('')
            self.WatchSet_CalType_Label.append('')
            self.WatchSet_CalType_ComboBox.append('')
            self.WatchSet_FormLayout1.append('')
            self.WatchSet_FormLayout2.append('')
            self.WatchSet_FormLayout3.append('')
            self.WatchSet_Offset_Label[i] = QLabel('??????:')
            self.WatchSet_DataType_Label[i] = QLabel('????????????:')
            self.WatchSet_CalType_Label[i] = QLabel('????????????:')
            self.WatchSet_Offset_SpinBox[i] = QSpinBox()
            self.WatchSet_Offset_SpinBox[i].setRange(0,1000)
            self.WatchSet_DataType_ComboBox[i] = QComboBox()
            self.WatchSet_DataType_ComboBox[i].addItems(["UINT8","UINT16","UINT32","INT8","INT16","INT32","BIN8","BIN16","FLOAT","CHAR"])
            self.WatchSet_CalType_ComboBox[i] = QComboBox()
            
            self.WatchSet_FormLayout1[i] = QFormLayout()
            self.WatchSet_FormLayout2[i] = QFormLayout()
            self.WatchSet_FormLayout3[i] = QFormLayout()

            self.WatchSet_FormLayout1[i].addRow(self.WatchSet_Offset_Label[i],self.WatchSet_Offset_SpinBox[i],)
            self.WatchSet_FormLayout2[i].addRow(self.WatchSet_DataType_Label[i],self.WatchSet_DataType_ComboBox[i],)
            self.WatchSet_FormLayout3[i].addRow(self.WatchSet_CalType_Label[i],self.WatchSet_CalType_ComboBox[i],)
            
            self.MainGridLayout1.addLayout(self.WatchSet_FormLayout1[i],i,0)
            self.MainGridLayout1.addLayout(self.WatchSet_FormLayout2[i],i,1)
            self.MainGridLayout1.addLayout(self.WatchSet_FormLayout3[i],i,2)

            ??????????????????(search_serial_conf,'WatchOffset'+str(i+1),self.WatchSet_Offset_SpinBox[i],'spinbox','0')
            ??????????????????(search_serial_conf,'WatchDataType'+str(i+1),self.WatchSet_DataType_ComboBox[i],'combobox','1')

            self.??????????????????(i,'')

            # self.WatchSet_DataType_ComboBox[i].textActivated.connect(handlerAdaptor(self.??????????????????,index = i))
            self.WatchSet_DataType_ComboBox[i].textActivated.connect(partial(self.??????????????????,i))

        self.Watch_ConfirmBtn = QPushButton('??????',self)
        self.MainGridLayout2.addWidget(self.Watch_ConfirmBtn)

        self.Watch_ConfirmBtn.clicked.connect(lambda:self.hideSetMain())

    def ??????????????????(self,index,event):
        self.WatchSet_CalType_ComboBox[index].clear()
        dataType = self.WatchSet_DataType_ComboBox[index].currentText()
        if dataType == 'UINT8' or dataType == 'INT8' or dataType =='CHAR' or dataType == 'BIN8':
            self.WatchSet_CalType_ComboBox[index].addItems(["NONE"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText("NONE")
        elif dataType=='UINT16' or dataType=='INT16' or dataType=='BIN16':
            self.WatchSet_CalType_ComboBox[index].addItems(["12","21"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText('21')
        elif dataType=='UINT32' or dataType=='INT32':
            self.WatchSet_CalType_ComboBox[index].addItems(["1234","4321","3412","2143"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText('3412')
        elif dataType=='FLOAT':
            self.WatchSet_CalType_ComboBox[index].addItems(["1234","4321","3412","2143"])
            self.WatchSet_CalType_ComboBox[index].setCurrentText('4321')

    def showFlowView(self,x,y):
        if self.isVisible():#???????????????????????? is not None????????????????????????
            self.hide()
        else:
            self.show()
        self.move(x-self.width()-5,y-self.height())

    def hideFlowView(self):
        self.hide()

    def closeEvent(self, event):
        self.hideFlowView()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    sys.exit(app.exec())
