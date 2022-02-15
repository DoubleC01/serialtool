# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import datetime
from time import *
import sys
# import random
import serial,serial.tools.list_ports
import re
import traceback
import sqlite3
import os
import threading
import struct
from functools import partial

# import ctypes
# import win32con
# import win32api

import IconGather
# import GifGather
import PngGather
# import JpgGather

# MainPicturesel = random.randrange(6)
# MainPicture1 = ":mainphoto1.gif"
# MainPicture2 = ":mainphoto2.gif"
# MainPicture3 = ":mainphoto3.gif"
# MainPicture4 = ":mainphoto4.gif"
# MainPicture5 = ":picture.gif"
# MainPicture6 = ":flymoon.gif"
# MainPicturelist = [MainPicture1,MainPicture2,MainPicture3,MainPicture4,MainPicture5,MainPicture6]
# MainPicture = MainPicturelist[MainPicturesel]
Ico = ":feather1.ico"
TitleName = '串口工具2021103001'
# Pic = ":pubu.jpg"

btnsty1 = "QPushButton{background:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123))}\
            QPushButton:hover{background:qlineargradient(x1:1, y1:1, x2:0, y2:0,stop:0 rgb(255,170,50),stop:0.5 rgb(127,170,127), stop: 1 rgb(192,253,123));}"
btnsty2 = "QPushButton{background:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 rgb(255,85,127),stop:0.5 rgb(255,85,0), stop: 1 rgb(255,177,0))}\
            QPushButton:hover{background:qlineargradient(x1:1, y1:1, x2:0, y2:0,stop:0 rgb(255,85,127),stop:0.5 rgb(255,85,0), stop: 1 rgb(255,177,0))}"

djdata=sqlite3.connect('SerialTool.db')        #连接到数据库,如果数据库不存在，那它就会被创建
cursor=djdata.cursor()                      # 获取cursor

cursor.execute(
                '''
                create table if not exists
                table_serial_conf(
                portname   text,
                portvalue   text
                )'''
               )# 数据表不存在时创建数据表

init_serial_conf=[
            ("SerialPort",""),
            ("SerialBurd","2400"),
            ("SerialByte","8"),
            ("SerialStop","1"),
            ("SerialParity","E"),
            ("ShowTimeFlag","1"),
            ("ShowHintFlag","1"),
            ("ShowSendFlag","1"),
            ("ShowReceiveFlag","1"),
            ("ShowSendMarkFlag","1"),
            ("ShowSendMark",">>>"),
            ("ShowReceiveMarkFlag","1"),
            ("ShowReceiveMark","<<<"),
            ("ShowHistoryFlag","0"),
            ("ShowWatchFlag","1"),
            ("ShowReplyFlag","0"),
            ("HexSendFlag","1"),
            ("HexShowFlag","1"),
            ("Check","无校验"),
            ("ReceiveDelayFlag","0"),
            ("ReceiveDelayTime","0"),
            ("OffSetFlag","0"),
            ("OffSet","15"),
            ("EntryFlag","0"),
            ("GuideFlag","0"),
            ("Guide",""),
            ("EndFlag","0"),
            ("End",""),
            ("AutoTime","1000"),
            ("AutoCountFlag","0"),
            ("AutoCount","0"),
            ("Send",""),
            ("Path",""),
          ]

##search_title=cursor.fetchall()
for i in init_serial_conf:
    count = 0
    search_title=cursor.execute("select portname from table_serial_conf")              #查找title这一列
    for j in search_title:
        if i[0] == j[0]:
            count += 1
    if count == 0:
        cursor.execute('insert into table_serial_conf values(?,?)',i)

djdata.commit()                         #一定要commit，不然上面的创建数据表的语句就白写了
djdata.close()                          #执行完成之后养成关闭数据库连接的好习惯


djdata=sqlite3.connect('SerialTool.db') 
cursor = djdata.cursor()
cursor.execute("select * from table_serial_conf") # where name = (?)",(jzqjm,) 
search_serial_conf=cursor.fetchall()
djdata.commit()   #同样记得要commit哦
djdata.close()

def 配置数据查找(tabledata,dataname,name,nametype,defaultdata):
    try:
        success = 0
        data = defaultdata
        if len(tabledata) > 0:
            for i in tabledata:
                if i[0] == dataname:
                    success = 1
                    break
            if success == 1:
                data = i[1]
        if nametype == 'combobox':
            name.setCurrentText(data)
        elif nametype == 'entry':
            name.setText(data)
        elif nametype == 'textedit':
            name.append(data)
        elif nametype == 'spinbox':
                name.setValue(int(data))
        elif nametype == 'check':
            name.setChecked(True) if data == 'True' or data == '1' else name.setChecked(False)
    except:
        pass

def 路径查找(tabledata,dataname,defaultdata):
    success = 0
    data = defaultdata
    if len(tabledata) > 0:
        for i in tabledata:
            if i[0] == dataname:
                success = 1
                break
        if success == 1:
            data = i[1]
    return data

def handlerAdaptor(fun,*kw,**kwds):
    return lambda event,fun=fun,kw=kw,kwds=kwds: fun(event, *kw,**kwds)

sendcount = 0
receivecount = 0
sendcount1 = 0
receivecount1 = 0

re_digits = re.compile(r'(\d+)') 

def emb_numbers(s):
    pieces=re_digits.split(s) 
    pieces[1::2]=map(int,pieces[1::2])     
    return pieces

def p_list():
    port_list= list(serial.tools.list_ports.comports())     #不能写在函数外面，每次都得执行
    plist0=[]
    for i in range(0,len(port_list)):
        plist_0 = list(port_list[i])
        plist0.append(str(plist_0[0]))
    return plist0

ser=serial.Serial()

def 获取串口列表(self):
    self.Serial_SerialComboBox.addItems(sorted(p_list(),key=emb_numbers))

def 刷新串口列表(self):
    currentPort = self.Serial_SerialComboBox.currentText()
    self.Serial_SerialComboBox.clear()
    showhintdataflag = self.Serial_ShowHintCheckBox.isChecked()
    port=sorted(p_list(),key=emb_numbers)
    self.Serial_SerialComboBox.addItems(port)
    if len(port):
        if showhintdataflag == 1:
            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'你的电脑共找到'+str(len(port)) + '个串口：'+str(port),'textColor':'Black'})
        if self.Serial_OpenBtn.text() == "打开串口":
            self.Serial_SerialComboBox.setCurrentIndex(0)
            串口(self)
        else:
            if not currentPort in port:
                self.Serial_SerialComboBox.setCurrentIndex(0)
                串口(self)
            else:
                self.Serial_SerialComboBox.setCurrentText(currentPort)
    else:
        if self.Serial_OpenBtn.text() == "关闭串口":
            self.ms.PushButtonSignal.emit(self.Serial_OpenBtn,{'text':"打开串口",'icon':self.Openico,'styleSheet':btnsty2})
        if showhintdataflag == 1:
            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'没找到串口！！！！！！！','textColor':'Red'})


def 切换串口参数刷新(self):
    try:
        ser.baudrate=int(self.Serial_BuadComboBox.currentText())
        ser.bytesize=int(self.Serial_ByteComboBox.currentText())
        ser.stopbits=float(self.Serial_StopComboBox.currentText())
        ser.parity=self.Serial_ParityComboBox.currentText()
    except Exception as e:
        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
        

flag=1

def 切换串口号刷新(self):
    global flag
    flag=1
    showhintdataflag = self.Serial_ShowHintCheckBox.isChecked()
    try:
        ser.close()
        port = ser.port
        if port != None:
            if ser.isOpen():
                ts = '关闭失败'
                color = 'Red'
            else:
                self.ms.PushButtonSignal.emit(self.Serial_OpenBtn,{'text':"打开串口",'icon':self.Openico,'styleSheet':btnsty2})
                ts = '关闭成功'
                color = 'Green'
            if showhintdataflag == 1:
                self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':ser.port+ts,'textColor':color})
        ser.port = self.Serial_SerialComboBox.currentText()
        串口(self)
    except Exception as e:
        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
    flag=0
    
def 串口(self):
    global flag
    flag=1
    showhintdataflag = self.Serial_ShowHintCheckBox.isChecked()
    try:
        if not self.Serial_SerialComboBox.currentText() == '':
            if self.Serial_OpenBtn.text() == "关闭串口":
                try:
                    ser.close()
                    if showhintdataflag == 1:
                        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'已关闭'+ser.port,'textColor':'Green'})
                except Exception as e:
                    self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
                    if showhintdataflag == 1:
                        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':ser.port+'串口异常！！！！！！！！','textColor':'Red'})
                self.ms.PushButtonSignal.emit(self.Serial_OpenBtn,{'text':"打开串口",'icon':self.Openico,'styleSheet':btnsty2})
            else:
                try:
                    ser.port=self.Serial_SerialComboBox.currentText()
                    ser.baudrate=int(self.Serial_BuadComboBox.currentText())
                    ser.bytesize=int(self.Serial_ByteComboBox.currentText())
                    ser.stopbits=float(self.Serial_StopComboBox.currentText())
                    ser.parity=self.Serial_ParityComboBox.currentText()
                    ser.timeout = 1
                    ser.open()
                    self.ms.PushButtonSignal.emit(self.Serial_OpenBtn,{'text':"关闭串口",'icon':self.Closeico,'styleSheet':btnsty1})
                    if showhintdataflag == 1:
                        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'已打开'+ser.port,'textColor':'Green'})
                except Exception as e:
                    self.ms.PushButtonSignal.emit(self.Serial_OpenBtn,{'text':"打开串口",'icon':self.Openico,'styleSheet':btnsty2})
                    self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
                    if showhintdataflag == 1:
                        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':ser.port+'串口异常,打开失败！！！！！！！！','textColor':'Red'})
        else:
            try:
                self.ms.PushButtonSignal.emit(self.Serial_OpenBtn,{'text':"打开串口",'icon':self.Openico,'styleSheet':btnsty2})
                if showhintdataflag == 1:
                    self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'空串口！！！','textColor':'Red'})
            except Exception as e:
                self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
    except Exception as e:
        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
        
    flag=0

def 清发送接收(self,cleartype):
    global sendcount,receivecount,sendcount1,receivecount1
    if cleartype == '发送数':
        sendcount = 0
        self.SendCount_SendCountLineEdit.setText('0')
    elif cleartype == '发送帧':
        sendcount1 = 0
        self.SendCount_SendFrameLineEdit.setText('0')
    elif cleartype == '接收数':
        receivecount = 0
        self.SendCount_ReceiveCountLineEdit.setText('0')
    elif cleartype == '接收帧':
        receivecount1 = 0
        self.SendCount_ReceiveFrameLineEdit.setText('0')

def 时间(self):
    if self.Serial_ShowTimeCheckBox.isChecked() == 1:
        # showtime = strftime("%Y/%m/%d %H:%M:%S ")
        showtime = datetime.datetime.now().strftime("[%H:%M:%S.%f]")[:-4]+'] '
    else:
        showtime = ''
    return showtime

def 发送标志(self):
    if self.Serial_ShowSendFlagCheckBox.isChecked() == 1:
        f = self.Serial_ShowSendFlagLineEdit.text().strip('\n')
    else:
        f = ''
    return f

def 接收标志(self):
    if self.Serial_ShowReveiveFlagCheckBox.isChecked() == 1:
        f = self.Serial_ShowReceiveFlagLineEdit.text().strip('\n')
    else:
        f = ''
    return f

def 接收延时时间(self):
    if self.SendFun_ReceiveDelayCheckBox.isChecked() == 1:
        a = self.SendFun_ReceiveDelaySpinBox.value()
        f = int(a)
        if f > 50000 or f < 1:
            f = 16
    else:
        f = 16
    return f

def 附加引导符(self):
    if self.SendFun_GuideCheckBox.isChecked() == 1:
        f = self.SendFun_GuideLineEdit.text().replace(' ','').strip()
    else:
        f = ''
    if self.SendFun_HexSendCheckBox.isChecked() == 0:
        f=hexShow(f)
    return f

def 附加结束符(self):
    if self.SendFun_EndCheckBox.isChecked() == 1:
        f = self.SendFun_EndLineEdit.text().replace(' ','').strip()
    else:
        f = ''
    if self.SendFun_HexSendCheckBox.isChecked() == 0:
        f=hexShow(f)
    return f

def 自动发送命令线程(self):
    if self.SendFun_AutoCheckBox.isChecked()==1:
        ra=threading.Thread(target=自动发送命令,args=(self,))
        ra.setDaemon(True)
        ra.start()

def 循环发送命令线程(self):
    if self.Histroy_AutoCheckBox.isChecked() == 1:
        rc=threading.Thread(target=循环发送命令,args=(self,))
        rc.setDaemon(True)
        rc.start()

def 自动发送命令(self):
    try:
        # 循环发送.deselect()
        self.ms.CheckBoxSignal.emit(self.Histroy_AutoCheckBox,{'checkState':'unCheck'})
        self.ms.CheckBoxSignal.emit(self.SendFun_CountCheckBox,{'checkState':'','state':0})
        self.ms.SpinBoxSignal.emit(self.SendFun_CountSpinBox,{'state':0})
        if self.SendFun_CountCheckBox.isChecked() == 1:
            sendtimes = self.SendFun_CountSpinBox.value()
            if sendtimes != '':
                sendtimes = int(sendtimes)
            else:
                sendtimes = 1
        else:
            sendtimes = 1
        sendtimestemp = 0
        remain = sendtimes                      
        self.ms.LabelSignal.emit(self.SendFun_CountUnitLabel,{'text':str(remain)})
        while self.SendFun_AutoCheckBox.isChecked() == True:
            if self.Serial_OpenBtn.text()=='关闭串口':
                if self.SendFun_CountCheckBox.isChecked() == 1:
                    if sendtimestemp >= sendtimes:
                        self.ms.CheckBoxSignal.emit(self.SendFun_AutoCheckBox,{'checkState':'unCheck'})
                        break
                try:
                    f = int(self.SendFun_AutoSpinBox.value())
                except:
                    f = 1000
                if f < 10 :
                    f = 10
                # if f > 100:
                t = f//10
                # else:
                    # t = f
                发送命令(self,-1)
                if self.SendFun_CountCheckBox.isChecked() == 1:
                    sendtimestemp += 1
                    remain -= 1
                    self.ms.LabelSignal.emit(self.SendFun_CountUnitLabel,{'text':str(remain)})
                for i in range(t):
                    try:
                        if self.SendFun_AutoCheckBox.isChecked() == 1 and ser.isOpen() and self.Serial_OpenBtn.text()=='关闭串口' and sendtimestemp < sendtimes:
                            # if f <= 100:
                            #     delay(0.001)
                            # else:
                            sleep(0.01)
                        else:
                            self.ms.CheckBoxSignal.emit(self.SendFun_AutoCheckBox,{'checkState':'unCheck'})
                            break
                    except Exception as e:     
                        # self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
                        sleep(0.01)
            else:
                self.ms.CheckBoxSignal.emit(self.SendFun_AutoCheckBox,{'checkState':'unCheck'})
                self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'请先打开串口！！！！！！！！！！！！','textColor':'Red'})
                break
    except Exception as e:
        pass
        # self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
    self.ms.CheckBoxSignal.emit(self.SendFun_CountCheckBox,{'state':1})
    self.ms.SpinBoxSignal.emit(self.SendFun_CountSpinBox,{'state':1})

def 循环发送命令(self):
    try:
        self.ms.CheckBoxSignal.emit(self.SendFun_AutoCheckBox,{'checkState':'unCheck'})
        while self.Histroy_AutoCheckBox.isChecked() == 1:
            try:
                autoList = []
                for i in range(500):
                    if self.Histroy_AutoCheckBox.isChecked() == 1 and self.Histroy_Frame_SendCheckBox[i].isChecked() == 1:
                        if self.Histroy_Frame_SendTextEdit[i].toPlainText().replace(' ','').strip() != '':
                            autoList.append(i)
                        else:
                            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':str(i+1).zfill(3)+'发送框为空！！！！！！！！！！！！','textColor':'Red'})

                if len(autoList) > 0:
                    for i in autoList:
                        try:
                            if self.Histroy_AutoCheckBox.isChecked() == 1:
                                if self.Histroy_Frame_SendCheckBox[i].isChecked() == 1:
                                    try:
                                        f = self.Histroy_AutoSpinBox.value()
                                    except:
                                        f = 1000
                                    if f < 10:
                                        f= 10
                                    # if f > 100:
                                    t = f//10
                                    # else:
                                    #     t = f
                                    发送命令(self,i)
                                    for i in range(t):
                                        if self.Histroy_AutoCheckBox.isChecked() == 1 and ser.isOpen() and self.Serial_OpenBtn.text()=='关闭串口':
                                            # if f <= 10:
                                            #     delay(0.001)
                                            # else:
                                            sleep(0.01)
                                        else:
                                            self.ms.CheckBoxSignal.emit(self.Histroy_AutoCheckBox,{'checkState':'unCheck'})
                                            break
                                else:
                                    sleep(0.001)
                        except:
                            sleep(0.001)
                else:
                    sleep(0.01)
            except:
                sleep(0.01)
    except Exception as e:
        pass
        
def 发送命令(self,index):
    global sendcount,sendcount1
    showsenddataflag = self.Serial_ShowSendCheckBox.isChecked()
    showhintdataflag = self.Serial_ShowHintCheckBox.isChecked()
    try:
        if ser.isOpen():
            try:
                cmd = ''
                if index == -1:
                    cmdget=self.Send_TextEdit.toPlainText().replace(' ','').strip()
                else:
                    cmdget=self.Histroy_Frame_SendTextEdit[int(index)].toPlainText().replace(' ','').strip()
                if self.SendFun_HexSendCheckBox.isChecked() == 0:
                    if self.SendFun_EndCheckBox.isChecked() == 1:
                        cmdget += '\n\r'
                    cmdget=hexShow(cmdget)
                if not cmdget == '':
                    if self.SendFun_OffsetCheckBox.isChecked() == 1:
                        offset = self.SendFun_OffsetSpinBox.value()
                        if len(cmdget)>2*int(offset):
                            cmd=cmdget[2*int(offset):]
                        else:
                            if showhintdataflag == 1:
                                self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'检验起始位超出发送长度，请检查！！！','textColor':'Red'})
                            cmd = ''
                    else:
                        cmd=cmdget
                else:
                    if showhintdataflag == 1:
                        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'发送框为空！！！！！！！！！！！！','textColor':'Red'})
                if cmd !='':
                    try:
                        b=bytes.fromhex(cmd) #字符串：h 0@，hex:68 20 30 40
                    except:
                        if showhintdataflag == 1:
                            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'发送框发送命令错误！！！！！！！！！！！！','textColor':'Red'})
                    else:
                        try:
                            checkmod = self.SendFun_CheckComboBox.currentText()
                            guide = 附加引导符(self)
                            end = 附加结束符(self)
                            if checkmod == '求和校验':
                                d="%s%s%s%s"%(guide,cmdget,' '+uchar_checksum(b),end)
                            elif checkmod == 'CRC-IBMH校验':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16(b,0),end)
                            elif checkmod == 'CRC-IBML校验':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16(b,1),end)
                            elif checkmod == '异或校验':
                                d="%s%s%s%s"%(guide,cmdget,' '+xor(b),end)
                            elif checkmod == 'CRC-CCITTXModemL':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccittxmodem(b,1),end)
                            elif checkmod == 'CRC-CCITTXModemH':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccittxmodem(b,0),end)
                            elif checkmod == 'CRC-CCITT0xFFFFL':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccittffff(b,1),end)
                            elif checkmod == 'CRC-CCITT0xFFFFH':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccittffff(b,0),end)
                            elif checkmod == 'CRC-CCITT0x1D0FL':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccitt1d0f(b,1),end)
                            elif checkmod == 'CRC-CCITT0x1D0FH':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccitt1d0f(b,0),end)
                            elif checkmod == 'CRC-CCITTKermitL':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccittkermit(b,1),end)
                            elif checkmod == 'CRC-CCITTKermitH':
                                d="%s%s%s%s"%(guide,cmdget,' '+crc16ccittkermit(b,0),end)
                            else:
                                d="%s%s%s"%(guide,cmdget,end)
                        except:
                            pass
                        else:
                            try:
                                b=bytes.fromhex(d)
                            except:
                                if showhintdataflag == 1:
                                    self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'发送框发送命令错误！！！！！！！！！！！！','textColor':'Red'})
                            else:
                                try:
                                    ser.flushOutput()
                                    ser.flushInput()
                                    ser.write(b)
                                except:
                                    pass
                                else:
                                    try:
                                        if self.SendFun_HexShowCheckBox.isChecked()==1:
                                            senddata = ByteToHex(b)
                                        else:
                                            senddata = bytetostr(b)
                                        if showsenddataflag == 1:
                                            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':时间(self)+发送标志(self),'textColor':'Blue'})
                                            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'insertPlainText','text':senddata,'textColor':'Black'})
                                        sendcount += len(b)
                                        self.ms.LineEditSignal.emit(self.SendCount_SendCountLineEdit,{'text':str(sendcount)})
                                        sendcount1 += 1
                                        self.ms.LineEditSignal.emit(self.SendCount_SendFrameLineEdit,{'text':str(sendcount1)})
                                    except Exception as e:
                                        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
            except:
                pass
        else:
            try:
                if not self.Serial_SerialComboBox.currentText() == '':
                    hintdata = self.Serial_SerialComboBox.currentText()+'未打开,请先打开串口！！！！！！！！！！！！\n'
                else:
                    hintdata = '串口未打开,请先打开串口！！！！！！！！！！！！\n'
                if showhintdataflag == 1:
                    self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':时间(self)+hintdata,'textColor':'Red'})
            except:
                pass
    except:
            pass
        
def 观察数据(self,data, byteorder='little',byteorder1='big'):
    j=0
    result = ''
    if self.Serial_ShowWatchCheckBox.isChecked() == 1:
        length = len(data)
        for i in range(15):
            try:
                j = int(self.SetMainwindow.WatchSet_Offset_SpinBox[i].value())
            except:
                j = 0
            if j>=0:
                result = ''
                dataType = self.SetMainwindow.WatchSet_DataType_ComboBox[i].currentText()
                calType = self.SetMainwindow.WatchSet_CalType_ComboBox[i].currentText()
                if dataType=='UINT8':
                    if j<(len(data)):
                        try:
                            result = str(int.from_bytes(data[j:j+1], byteorder, signed=False))
                        except:
                            result = ''
                elif dataType=='UINT16':
                    if j<(len(data)-1):
                        if calType=='21':
                            try:
                                result = str(int.from_bytes(data[j:j+2], byteorder, signed=False))
                            except:
                                result = ''
                        elif calType=='12':
                            try:
                                result = str(int.from_bytes(data[j:j+2], byteorder1, signed=False))
                            except:
                                result = ''
                elif dataType=='UINT32':
                    if j<(len(data)-3):
                        if calType=='4321':
                            try:
                                result = str(int.from_bytes(data[j:j+4], byteorder, signed=False))
                            except:
                                result = ''
                        elif calType=='1234':
                            try:
                                result = str(int.from_bytes(data[j:j+4], byteorder1, signed=False))
                            except:
                                result = ''
                        elif calType=='3412':
                            try:
                                result = str(int.from_bytes(data[j+2:j+4]+data[j:j+2], byteorder1, signed=False))
                            except:
                                result = ''
                        elif calType=='2143':
                            try:
                                result = str(int.from_bytes(data[j+2:j+4]+data[j:j+2], byteorder, signed=False))
                            except:
                                result = ''
                elif dataType=='INT8':
                    if j<(len(data)):
                        try:
                            result = str(int.from_bytes(data[j:j+1], byteorder, signed=True))
                        except:
                            result = ''
                elif dataType=='INT16':
                    if j<(len(data)-1):
                        if calType=='21':
                            try:
                                result = str(int.from_bytes(data[j:j+2], byteorder, signed=True))
                            except:
                                result = ''
                        elif calType=='12':
                            try:
                                result = str(int.from_bytes(data[j:j+2], byteorder1, signed=True))
                            except:
                                result = ''
                elif dataType=='INT32':
                    if j<(len(data)-3):
                        if calType=='4321':
                            try:
                                result = str(int.from_bytes(data[j:j+4], byteorder, signed=True))
                            except:
                                result = ''
                        elif calType=='1234':
                            try:
                                result = str(int.from_bytes(data[j:j+4], byteorder1, signed=True))
                            except:
                                result = ''
                        elif calType=='3412':
                            try:
                                result = str(int.from_bytes(data[j+2:j+4]+data[j:j+2], byteorder1, signed=True))
                            except:
                                result = ''
                        elif calType=='2143':
                            try:
                                result = str(int.from_bytes(data[j+2:j+4]+data[j:j+2], byteorder, signed=True))
                            except:
                                result = ''
                elif dataType=='FLOAT':
                    if j<(len(data)-3):
                        if calType=='4321':
                            try:
                                result = str(struct.unpack('!f',data[j:j+4][::-1])[0])
                            except:
                                result = ''
                        elif calType=='1234':
                            try:
                                result = str(struct.unpack('!f',data[j:j+4])[0])
                            except:
                                result = ''
                        elif calType=='3412':
                            try:
                                result = str(struct.unpack('!f',data[j+2:j+3]+data[j+3:j+4]+data[j:j+1]+data[j+1:j+2])[0])
                            except:
                                result = ''
                        elif calType=='2143':
                            try:
                                result = str(struct.unpack('!f',data[j+1:j+2]+data[j:j+1]+data[j+3:j+4]+data[j+2:j+3])[0])
                            except:
                                result = ''
                elif dataType=='CHAR':
                    if j<(len(data)):
                        try:
                            result = ByteToHex(data)[3*j:3*j+2]
                        except:
                            result = ''
                elif dataType=='BIN8':
                    if j<(len(data)):
                        try:
                            result = bin(int.from_bytes(data[j:j+1], byteorder1, signed=False)).replace('0b','').zfill(8)   #8位自动补0
                        except:
                            result = ''
                elif dataType=='BIN16':
                    if j<(len(data)-1):
                        if calType=='21':
                            try:
                                result = bin(int.from_bytes(data[j+1:j+2], byteorder1, signed=False)).replace('0b','').zfill(8)+'\n'+bin(int.from_bytes(data[j:j+1], byteorder1, signed=False)).replace('0b','').zfill(8)
                            except:
                                result = ''
                        elif calType=='12':
                            try:
                                result = bin(int.from_bytes(data[j:j+1], byteorder1, signed=False)).replace('0b','').zfill(8)+'\n'+bin(int.from_bytes(data[j+1:j+2], byteorder1, signed=False)).replace('0b','').zfill(8)
                            except:
                                result = ''  
                self.ms.LineEditSignal.emit(self.Watch_LineEdit[i],{'text':str(result)})

def 接收命令(self):
    global receivecount,flag,receivecount1
    while (True):
        showreceivedataflag = self.Serial_ShowReceiveCheckBox.isChecked()
        showhintdataflag = self.Serial_ShowHintCheckBox.isChecked()
        seeflag = self.Serial_ShowWatchCheckBox.isChecked()
        try:
            if self.Serial_OpenBtn.text() == "关闭串口":
                if ser.isOpen():
                    time = 0
                    if ser.inWaiting():
                        try:
                            if showreceivedataflag == 1:
                                showtimeandreceive = 时间(self)+接收标志(self)
                                self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':时间(self)+接收标志(self),'textColor':'Brown'})
                            t=接收延时时间(self)
                            b = b''
                            while time < t:
                                t=接收延时时间(self)
                                a = b''
                                n=ser.inWaiting()
                                if n > 0:
                                    a = ser.read(n)
                                    b += a
                                    receivecount += len(a)
                                    self.ms.LineEditSignal.emit(self.SendCount_ReceiveCountLineEdit,{'text':str(receivecount)})
                                    if showreceivedataflag == 1:
                                        try:
                                            if self.SendFun_HexShowCheckBox.isChecked()==1:
                                                if len(b) > len(a):
                                                    self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'insertPlainText','text':' '+ByteToHex(a),'textColor':'Black'})
                                                else:
                                                    self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'insertPlainText','text':ByteToHex(a),'textColor':'Black'})
                                            else:
                                                self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'insertPlainText','text':bytetostr(a),'textColor':'Black'})
                                        except:
                                            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'接收的信息错误！！！！！！！！！！！！','textColor':'Red'})
                                    time = 0
                                else:
                                    time += 1
                                if time >= t:
                                    # if showreceivedataflag == 1:
                                        # self.Receive_TextEdit.insertPlainText('\n')
                                        # self.ms.TextEditSignal.emit(self.Receive_TextEdit,'insertPlainText','\n')
                                    if self.Serial_ShowAutoReplyCheckBox.isChecked() == 1 or self.Reply_SelReplyCheckBox.isChecked() == 1 :
                                        ra=threading.Thread(target=自动回复cmd,args=(self,b,))
                                        ra.setDaemon(True)
                                        ra.start()
                                    if seeflag == 1:
                                        观察数据(self,b)
                                    receivecount1 += 1
                                    self.ms.LineEditSignal.emit(self.SendCount_ReceiveFrameLineEdit,{'text':str(receivecount1)})

                                # delay(0.001)
                                sleep(0.01)
                        except Exception as e:
                            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
                            sleep(0.01)
                            break
        except Exception as e:
            if flag==0:
                try:
                    if self.Serial_OpenBtn.text() == "关闭串口":
                        ser.close()
                        self.ms.PushButtonSignal.emit(self.Serial_OpenBtn,{'text':"打开串口",'icon':self.Openico,'styleSheet':btnsty2})
                        if showhintdataflag == 1:
                            self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':'串口异常已关闭！！！','textColor':'Red'})
                except Exception as e:
                    pass
        sleep(0.01)

def 自动回复cmd(self,receive):
    selreplysuccess = 0
    if self.Reply_SelReplyCheckBox.isChecked() == 1:
        checksuccess = 0
        if self.Reply_V3ReadAddCheckBox.isChecked() == 1 or self.Reply_V3WriteAddCheckBox.isChecked() == 1\
             or self.Reply_V3WriteTimeCheckBox.isChecked() == 1 or self.Reply_V3ReadAllDataCheckBox.isChecked() == 1 or self.Reply_V3WriteDataCheckBox.isChecked() == 1:
            j=0
            for i in range(len(receive)):
                if ByteToHex(receive[i:i+1]) == 'FE':
                    j=i+1
                else:
                    break
            receive = receive[j:]
            ralllength = len(receive)
            if ralllength >= 16:
                rlength = int.from_bytes(receive[10:11], 'little', signed=False)             #接收的数据长度解析
                callength = rlength + 13            #1起始+1表类型+7表地址+1控制码+1数据长度+1个校验和+1个结束符
                if ralllength == callength:            #总接收长度正确
                    startcount = 0
                    endcount = startcount + 1
                    rstart = ByteToHexNoSpace(receive[startcount:endcount])
                    if rstart == '68':
                        startcount = endcount
                        endcount = startcount + 1
                        rdevicetype = ByteToHexNoSpace(receive[startcount:endcount])
                        if rdevicetype == '20' or rdevicetype == '10':
                            startcount = endcount
                            endcount = startcount + 7
                            radd = ByteToHexNoSpace(receive[startcount:endcount])
                            startcount = endcount
                            endcount = startcount + 1
                            rcontrolcode =ByteToHexNoSpace(receive[startcount:endcount])
                            a1 = int(rcontrolcode,16)
                            a2 = a1 + 0x80
                            calcontrolcode = format(a2,'x').zfill(2).upper()
                            startcount = endcount
                            endcount = startcount + 1
                            rlengthshow = ByteToHexNoSpace(receive[startcount:endcount])
                            rlength = int.from_bytes(receive[startcount:endcount], 'little', signed=False)
                            callength = ralllength- startcount - 3
                            callengthshow = format(callength,'x').zfill(2).upper()
                            if rlength == callength:
                                startcount = endcount
                                endcount = startcount + 2
                                rDI = ByteToHexNoSpace(receive[startcount:endcount])
                                startcount = endcount
                                endcount = startcount + 1
                                rsr = ByteToHexNoSpace(receive[startcount:endcount])
                                startcount = endcount
                                endcount = startcount + (rlength - 3)    #DI2个，sr 1个,数据开始位置
                                startcount = endcount
                                endcount = startcount + 1
                                data = receive[startcount:endcount]
                                rcheck = ByteToHexNoSpace(receive[startcount:endcount])
                                calcheck = uchar_checksum(receive[:-2])
                                if rcheck == calcheck:
                                    startcount = endcount
                                    endcount = startcount + 1
                                    rend = ByteToHexNoSpace(receive[startcount:endcount])
                                    if rend == '16':
                                        checksuccess = 1
            if checksuccess == 1:
                senddata = {
                    'guide' : 'FEFEFE',
                    'start' : '68',
                    'devicetype' : rdevicetype,
                    'add' : '',
                    'controlcode' : calcontrolcode,
                    'datalength' : '03',
                    'DI' : rDI,
                    'sr' :rsr,
                    'data' : '',
                    'check' : '',
                    'end' : '16',
                }
                if rDI == '0A81' and rcontrolcode == '03' and rlengthshow == '03':
                    if self.Reply_V3ReadAddCheckBox.isChecked() == 1:
                        selreplysuccess = 1
                        if self.Reply_V3ReadAddLineEdit.text() != '':
                            senddata['add']=self.Reply_V3ReadAddLineEdit.text().upper().zfill(14)
                        else:
                            senddata['add']='00'*7
                if rDI == '18A0' and rcontrolcode == '15' and rlengthshow == '0A':
                    if self.Reply_V3WriteAddCheckBox.isChecked() == 1:
                        selreplysuccess = 1
                        if self.Reply_V3WriteAddLineEdit.text() != '':
                            senddata['add']=self.Reply_V3WriteAddLineEdit.text().upper().zfill(14)
                        else:
                            senddata['add']='00'*7
                if rcontrolcode == '04':
                    if rDI == '15A0' and  rlengthshow == '0A':
                        if self.Reply_V3WriteTimeCheckBox.isChecked() == 1:
                            selreplysuccess = 1
                            senddata['add']=radd
                    else:
                        if self.Reply_V3WriteDataCheckBox.isChecked() == 1:
                            selreplysuccess = 1
                            senddata['add']=radd
                if (rDI == '2190' or rDI == '1F90') and rcontrolcode == '01' and rlengthshow == '03':
                    if self.Reply_V3ReadAllDataCheckBox.isChecked() == 1:
                        selreplysuccess = 1
                        senddata['add']=radd
                        if rdevicetype == '20':
                            if self.Reply_V5CheckBox.isChecked() == 1 and rDI == '1F90':
                                a1 = int(self.Reply_V3TotalColdDoubleSpinBox.value()*100)
                            else:
                                a1 = int(self.Reply_V3AccountHeatDoubleSpinBox.value()*100)
                            a1 = str(a1).zfill(8)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            a14 = a1[6:8]
                            a2 = self.Reply_V3AccountHeatComboBox.currentText()
                            if a2 == 'kWh':
                                a21 = '05'
                            else:
                                a21 = '08'
                            senddata['data'] += a14+a13+a12+a11+a21
                            a1 = int(self.Reply_V3TotalHeatDoubleSpinBox.value()*100)
                            a1 = str(a1).zfill(8)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            a14 = a1[6:8]
                            a2 = self.Reply_V3TotalHeatComboBox.currentText()
                            if a2 == 'kWh':
                                a21 = '05'
                            else:
                                a21 = '08'
                            senddata['data'] += a14+a13+a12+a11+a21
                            a1 = int(self.Reply_V3PowerDoubleSpinBox.value()*100)
                            a1 = str(a1).zfill(8)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            a14 = a1[6:8]
                            a2 = self.Reply_V3PowerComboBox.currentText()
                            if a2 == 'kW':
                                a21 = '17'
                            else:
                                a21 = '1A'
                            senddata['data'] += a14+a13+a12+a11+a21
                            a1 = int(self.Reply_V3TotalFlowRateDoubleSpinBox.value()*10000)
                            a1 = str(a1).zfill(8)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            a14 = a1[6:8]
                            a21 = '35'
                            senddata['data'] += a14+a13+a12+a11+a21
                        a1 = int(self.Reply_V3TotalFlowDoubleSpinBox.value()*100)
                        a1 = str(a1).zfill(8)
                        a11 = a1[:2]
                        a12 = a1[2:4]
                        a13 = a1[4:6]
                        a14 = a1[6:8]
                        a21 = '2C'
                        senddata['data'] += a14+a13+a12+a11+a21
                        if rdevicetype == '10':
                            a1 = int(self.Reply_V3TotalAccountFlowDoubleSpinBox.value()*100)
                            a1 = str(a1).zfill(8)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            a14 = a1[6:8]
                            a21 = '2C'
                            senddata['data'] += a14+a13+a12+a11+a21
                        if rdevicetype == '20':
                            a1 = int(self.Reply_V3TotalInTempDoubleSpinBox.value()*100)
                            a1 = str(a1).zfill(6)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            senddata['data'] += a13+a12+a11
                            a1 = int(self.Reply_V3TotalOutTempDoubleSpinBox.value()*100)
                            a1 = str(a1).zfill(6)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            senddata['data'] += a13+a12+a11
                            a1 = int(self.Reply_V3TotalWorkTimeSpinBox.value())
                            a1 = str(a1).zfill(6)
                            a11 = a1[:2]
                            a12 = a1[2:4]
                            a13 = a1[4:6]
                            senddata['data'] += a13+a12+a11
                        date = self.Reply_V3TimeDateEdit.date()
                        time = self.Reply_V3TimeDateEdit.time()
                        year=str(QDate.year(date)).zfill(4).upper()
                        mon=str(QDate.month(date)).zfill(2).upper()
                        day=str(QDate.day(date)).zfill(2).upper()
                        hour=str(QTime.hour(time)).zfill(2).upper()
                        mini=str(QTime.minute(time)).zfill(2).upper()
                        sec=str(QTime.second(time)).zfill(2).upper()
                        year=year[2:].zfill(2).upper()+year[:2].zfill(2).upper()
                        senddata['data'] += sec+mini+hour+day+mon+year
                        if rdevicetype == '20':
                            if rDI == '2190':
                                a1 = int(self.Reply_V3AccountColdDoubleSpinBox.value()*100)
                                a1 = str(a1).zfill(8)
                                a11 = a1[:2]
                                a12 = a1[2:4]
                                a13 = a1[4:6]
                                a14 = a1[6:8]
                                a2 = self.Reply_V3AccountColdComboBox.currentText()
                                if a2 == 'kWh':
                                    a21 = '05'
                                else:
                                    a21 = '08'
                                senddata['data'] += a14+a13+a12+a11+a21
                                a1 = int(self.Reply_V3TotalColdDoubleSpinBox.value()*100)
                                a1 = str(a1).zfill(8)
                                a11 = a1[:2]
                                a12 = a1[2:4]
                                a13 = a1[4:6]
                                a14 = a1[6:8]
                                a2 = self.Reply_V3TotalColdComboBox.currentText()
                                if a2 == 'kWh':
                                    a21 = '05'
                                else:
                                    a21 = '08'
                                senddata['data'] += a14+a13+a12+a11+a21
                                a1 = int(self.Reply_V3TotalAlarmTimeSpinBox.value())
                                a1 = str(a1).zfill(6)
                                a11 = a1[:2]
                                a12 = a1[2:4]
                                a13 = a1[4:6]
                                senddata['data'] += a13+a12+a11
                        a1 = self.Reply_V3InstallTypeComboBox.currentIndex()
                        a2 = self.Reply_V3FlowDriectionComboBox.currentIndex()
                        a3 = self.Reply_V3VoltageComboBox.currentIndex()
                        a4 = self.Reply_V3TempDifComboBox.currentIndex()
                        a5 = self.Reply_V3BlankPipeComboBox.currentIndex()
                        a6 = self.Reply_V3TempErrorComboBox.currentIndex()
                        data = (a1 << 0)
                        data += (a2 << 1)
                        data += (a3 << 2)
                        data += (a4 << 4)
                        data += (a5 << 5)
                        data += (a6 << 6)
                        data1 = format(data&0xFF,'x').zfill(2).upper()
                        senddata['data'] += data1+'00'
                if selreplysuccess == 1:
                    length = len(senddata['data'])//2+3
                    length1 = format(length&0xFF,'x').zfill(2).upper()
                    senddata['datalength'] = length1
                    if self.Reply_V5CheckBox.isChecked() == 1:
                        senddata['devicetype'] = '25'
                    cmdtemp = senddata['start']+senddata['devicetype']+senddata['add']+senddata['controlcode']+senddata['datalength']+senddata['DI']+senddata['sr']+senddata['data']
                    cstemp=bytes.fromhex(cmdtemp)
                    cs = uchar_checksum(cstemp)
                    cmd = "%s%s%s%s"%(senddata['guide'],cmdtemp,cs,senddata['end'])
                    回复命令(self,cmd)

    if self.Serial_ShowAutoReplyCheckBox.isChecked() == 1:
        if selreplysuccess == 0:
            发送命令(self,-1)

def 回复命令(self,cmd):
    try:
        showsenddataflag = self.Serial_ShowSendCheckBox.isChecked()
        if ser.isOpen():
            b = bytes.fromhex(cmd)
            ser.flushOutput()
            ser.flushInput()
            ser.write(b)
            if showsenddataflag == 1:
                self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':时间(self)+发送标志(self)+ByteToHex(b),'textColor':'Black'})
                
    except Exception as e:
        self.ms.TextEditSignal.emit(self.Receive_TextEdit,{'insertType':'append','text':traceback.format_exc(),'textColor':'Red'})
        
def delay(t):
    starttime = perf_counter()#Python 3.8 已移除 clock() 方法 可以使用 time.perf_counter() 或 time.process_time() 方法替代。
    delaytime = 0
    while (delaytime < t):
        endtime = perf_counter()
        delaytime = endtime - starttime

def 清空(name):
    name.clear()
    # name.setText('')

def 保存(self):
    FileDialog = QFileDialog()
    filename, selectedFilter = FileDialog.getSaveFileName(self, "保存数据",self.Path+'/'+strftime("%Y%m%d%H%M%S")+'.txt','Text Files(*.txt)')
    data = self.Receive_TextEdit.toPlainText()
    if filename:
        with open(filename,"a+",encoding='utf-8') as f1:
            f1.write(data)
        os.startfile(filename)
        self.Path = os.path.dirname(filename)

def uchar_checksum(data, byteorder='little'):
    length = len(data)
    checksum = 0
    result = ''
    for i in range(0, length):
        checksum += int.from_bytes(data[i:i+1], byteorder, signed=False)
        checksum &= 0xFF # 强制截断
        if checksum>=16:
            result=hex(checksum).replace('0x', '')
        else:
            result='0'+hex(checksum).replace('0x', '')
    return result.upper()

def crc16(x, invert):
        a = 0xFFFF
        b = 0xA001
        for byte in x:
            #a ^= ord(byte)
            a ^= byte
            for i in range(8):
                last = a % 2
                a >>= 1
                if last == 1:
                    a ^= b
        a = '%.4x' % a
        s = str(a).upper()
        return s[2:4]+s[0:2] if invert == True else s[0:2]+s[2:4]

def crc16ccittffff(x, invert):
        a = 0xFFFF
        b = 0x1021
        for byte in x:
            #a ^= ord(byte)
            a ^= (byte << 8)
            for i in range(8):
                last = (a & 0x8000)
                a <<= 1
                a &= 0xFFFF
                if last == 0x8000:
                    a ^= b
        a = '%.4x' % a
        s = str(a).upper()
        return s[2:4]+s[0:2] if invert == True else s[0:2]+s[2:4]

def crc16ccitt1d0f(x, invert):
        a = 0x1D0F
        b = 0x1021
        for byte in x:
            #a ^= ord(byte)
            a ^= (byte << 8)
            for i in range(8):
                last = (a & 0x8000)
                a <<= 1
                a &= 0xFFFF
                if last == 0x8000:
                    a ^= b
        a = '%.4x' % a
        s = str(a).upper()
        return s[2:4]+s[0:2] if invert == True else s[0:2]+s[2:4]

def crc16ccittxmodem(x, invert):
        a = 0x0000
        b = 0x1021
        for byte in x:
            #a ^= ord(byte)
            a ^= (byte << 8)
            for i in range(8):
                last = (a & 0x8000)
                a <<= 1
                a &= 0xFFFF
                if last == 0x8000:
                    a ^= b
        a = '%.4x' % a
        s = str(a).upper()
        return s[2:4]+s[0:2] if invert == True else s[0:2]+s[2:4]

def crc16ccittkermit(x, invert):
        a = 0x0000
        b = 0x8408
        for byte in x:
            #a ^= ord(byte)
            a ^= byte
            for i in range(8):
                last = a % 2
                a >>= 1
                if last == 1:
                    a ^= b
        a = '%.4x' % a
        s = str(a).upper()
        return s[2:4]+s[0:2] if invert == True else s[0:2]+s[2:4]

def xor(x):
    a = 0
    for byte in x:
        a ^= byte
    a = '%.2x' % a
    s = str(a).upper()
    return s

def bytetostr(byte):            #非16进制显示
    result = ''
    result=byte.decode ( 'GBK','replace')#'ignore'是忽略错误'replace’是替换错误码
    return result

# 转成16进制的函数
def convert_hex(string):
    res = []
    result = []
    for item in string:
        res.append(item)
    for i in res:
        result.append(hex(i))
    return result

def hexShow(argv):              #转换成单个数的16进制，如11 = 31 31 用于非16进制发送
    result = ''
    hLen = len(argv)
    for i in range(hLen):
        hvol = ord(argv[i])
        hhex = '%02x '%hvol
        result += hhex+' '
    return result

def ByteToHex( bins ):
    return ''.join( [ "%02X " % x for x in bins ] ).strip()

def ByteToHexNoSpace( bins ):
    return ''.join( [ "%02X" % x for x in bins ] ).strip().upper()

def HexToByte( hexStr ):
    return bytes.fromhex(hexStr)