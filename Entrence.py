# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Entrence.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from decimal import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from exam import *
from examination import *
from RealCalculate import  *
from PyQt5.Qt import *
import datetime
import random

class Entrence(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Entrence,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(440, 190, 93, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(270, 100, 101, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 130, 92, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 190, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 220, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 280, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 70, 91, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 380, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(440, 160, 93, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 160, 121, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 420, 371, 81))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 420, 121, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 220, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 280, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 250, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 280, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(61, 40, 121, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 40, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 310, 72, 15))
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(440, 310, 93, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 360, 261, 16))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2.clicked.connect(self.findgrade)
        self.pushButton.clicked.connect(self.entry)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(7.jpg);}")
    def findgrade(self):
        self.getname()
        dict1={}
        t = open("name.txt", 'r+')
        list_name = t.readlines()
        #print(list_name)
        name = ''.join(list_name)
        if name == '':
            name = '游客'
        f = open("name_grades.txt", "r+")
        listgrade = f.readlines()
        listgrades = [i.split(":") for i in listgrade]
        #print(listgrades)
        for i in listgrades:
            if i[0] not in dict1:
                dict1[i[0]] = i[1]
            else:
                dict1[i[0]] = dict1[i[0]] + i[1]

        if (name + '成绩为') in dict1:
            self.textEdit.append(name+'同学过去的测试成绩为：\n'+dict1[name + '成绩为'])
        else:
            self.textEdit.append(name + '同学'+'未参加过测试')

    def jump(self):
        textwindow.show()
        MainWindow.close()
    def getname(self):
        name = self.lineEdit_5.text()
        f = open("name.txt", "r+")
        f.truncate()
        f.write(name)
        f.close()
    def entry(self):
        self.SignalCheck()
        if self.questionnum()!=10:
            res_5 = QMessageBox.about(self, "提醒", "三种类型的题目总数必须为10")
        else:
            self.jump()
            self.getname()
            self.SignalCheck()
            self.Signalget()

    def SignalCheck(self):
        print(6)
        f = open("signal.txt", "r+")
        if self.checkBox.isChecked():
            f.write('1' + '\n')
        else:
            f.write('0' + '\n')

        if self.checkBox_2.isChecked():
            f.write('1' + '\n')
        else:
            f.write('0' + '\n')
        text = self.comboBox_2.currentText()
        f.write(text + '\n')
        text2 = self.comboBox.currentText()
        f.write(text2 + '\n')
        text3 = self.lineEdit.text()
        f.write(text3 + '\n')
        text4 = self.lineEdit_3.text()
        f.write(text4 + '\n')
        text5 = self.lineEdit_4.text()
        f.write(text5 + '\n')
        text6=self.comboBox_3.currentText()
        f.write(text6+'\n')
        f.close()

    def Signalget(self):

        f = open("signal.txt", "r")
        list_signal = f.readlines()
        list_newsignal = [i.replace('\n', '') for i in list_signal]
        list_newsignal = ["0" if i == "" else i for i in list_newsignal]
        print(list_newsignal)
        decimal_num = int(list_newsignal[0])
        print(decimal_num)
        Ifinclude = int(list_newsignal[1])
        print(type(Ifinclude))
        scope = int(list_newsignal[2])
        variable_num = int(list_newsignal[3])
        choose_num = int(list_newsignal[4])
        judge_num = int(list_newsignal[5])
        blank_num =int(list_newsignal[6])
        difficulty_num = int(list_newsignal[7])
        if difficulty_num == 1:
            k = ['+', '-']
        elif difficulty_num == 2:
            k = ['+', '-', '*', '/', '+', '+', '+', '-', '+', '-', '-']
        list_int = []
        list_intafloat = []
        if scope == 10:
            for i in range(11):
                list_int.append(i)
            for i in range(100):
                if i < 60:
                    list_intafloat.append(random.randint(0, 10))
                else:
                    list_intafloat.append(round((random.uniform(0, 10)), 1))
        elif scope == 100:
            for i in range(100):
                if i < 70:
                    list_int.append(random.randint(0, 50))
                list_int.append(random.randint(50, 101))
            for i in range(100):
                if i < 70:
                    list_intafloat.append(random.randint(0, 50))
                else:
                    list_intafloat.append(round((random.uniform(0, 100)), 1))
        elif scope == 1000:
            for i in range(100):
                if i < 70:
                    list_int.append(random.randint(0, 101))
                elif i < 90:
                    list_int.append(random.randint(101, 500))
                else:
                    list_int.append((random.randint(500, 1000)))
            for i in range(50):
                if i < 40:
                    list_intafloat.append(random.randint(0, 101))
                    list_intafloat.append(round(random.uniform(0, 101)))
                elif i < 48:
                    list_intafloat.append(random.randint(101, 500))
                    list_intafloat.append(round(random.uniform(101, 500)))

        t = open("name.txt", "r+")
        list_name = t.readlines()
        name = ''.join(list_name)
        t.close()
        e=open("question.txt","a")
        i = datetime.datetime.now()
        e.write(name+": "+'-'+str(i.year)+'年'+str(i.month)+'月'+str(i.day)+'日 '+str(i.hour)+'时'+str(i.minute)+'分'+'\n')
        e.close()


        Choose(decimal_num,Ifinclude,scope,variable_num,choose_num,judge_num,blank_num,difficulty_num,list_intafloat,list_int,k)
        judge(decimal_num,Ifinclude,scope,variable_num,choose_num,judge_num,blank_num,difficulty_num,list_intafloat,list_int,k)
        blankscalculate(decimal_num,Ifinclude,scope,variable_num,choose_num,judge_num,blank_num,difficulty_num,list_intafloat,list_int,k)
        f.close()
    def questionnum(self):
        sum=0
        f = open("signal.txt", "r")
        list_signal = f.readlines()
        list_newsignal = [i.replace('\n', '') for i in list_signal]
        list_newsignal = ["0" if i == "" else i for i in list_newsignal]
        list_questionnum=[float(i) for i in list_newsignal[4:7]]
        for i in list_questionnum:
            sum=sum+i
        return sum
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "混合运算自测系统"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3"))
        self.comboBox.setItemText(2, _translate("MainWindow", "4"))
        self.checkBox.setText(_translate("MainWindow", "是否带小数"))
        self.checkBox_2.setText(_translate("MainWindow", "是否括号"))
        self.label.setText(_translate("MainWindow", "运算数个数"))
        self.label_2.setText(_translate("MainWindow", "选择题个数"))
        self.label_3.setText(_translate("MainWindow", "判断题个数"))
        self.label_4.setText(_translate("MainWindow", "填写题个数"))
        self.label_5.setText(_translate("MainWindow", "请选择题型"))
        self.pushButton.setText(_translate("MainWindow", "下一步"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "100"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1000"))
        self.label_6.setText(_translate("MainWindow", "多少以内的算术"))
        self.pushButton_2.setText(_translate("MainWindow", "查询以往测试成绩"))
        self.label_7.setText(_translate("MainWindow", "请输入答题者姓名"))
        self.label_8.setText(_translate("MainWindow", "试题难度"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.label_9.setText(_translate("MainWindow", "难度1只有加减法，难度二为四则运算"))
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Entrence()
    textwindow=Examination()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
