# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\workspace\opensource\codertool\codertool.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_codertool(object):
    def setupUi(self, codertool):
        codertool.setObjectName("codertool")
        codertool.resize(1019, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/addons.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        codertool.setWindowIcon(icon)
        codertool.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.content = QtWidgets.QWidget(codertool)
        self.content.setEnabled(True)
        self.content.setObjectName("content")
        self.tabWidget = QtWidgets.QTabWidget(self.content)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1001, 581))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.push_timetodate = QtWidgets.QPushButton(self.tab)
        self.push_timetodate.setGeometry(QtCore.QRect(570, 80, 112, 41))
        self.push_timetodate.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.push_timetodate.setObjectName("push_timetodate")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 90, 61, 18))
        self.label.setObjectName("label")
        self.dateTime2 = QtWidgets.QLineEdit(self.tab)
        self.dateTime2.setGeometry(QtCore.QRect(350, 80, 181, 41))
        self.dateTime2.setObjectName("dateTime2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 71, 18))
        self.label_5.setObjectName("label_5")
        self.timestamp3 = QtWidgets.QLineEdit(self.tab)
        self.timestamp3.setGeometry(QtCore.QRect(350, 140, 181, 41))
        self.timestamp3.setObjectName("timestamp3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(320, 150, 21, 18))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(320, 90, 21, 18))
        self.label_4.setObjectName("label_4")
        self.timestamp2 = QtWidgets.QLineEdit(self.tab)
        self.timestamp2.setGeometry(QtCore.QRect(100, 80, 211, 41))
        self.timestamp2.setObjectName("timestamp2")
        self.push_datetotime = QtWidgets.QPushButton(self.tab)
        self.push_datetotime.setGeometry(QtCore.QRect(570, 140, 112, 41))
        self.push_datetotime.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.push_datetotime.setObjectName("push_datetotime")
        self.dateTime3 = QtWidgets.QLineEdit(self.tab)
        self.dateTime3.setGeometry(QtCore.QRect(100, 140, 211, 41))
        self.dateTime3.setObjectName("dateTime3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        codertool.setCentralWidget(self.content)

        self.retranslateUi(codertool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(codertool)

    def retranslateUi(self, codertool):
        _translate = QtCore.QCoreApplication.translate
        codertool.setWindowTitle(_translate("codertool", "coder工具包"))
        self.push_timetodate.setText(_translate("codertool", "转换"))
        self.label.setText(_translate("codertool", "时间戳"))
        self.label_5.setText(_translate("codertool", "日期格式"))
        self.label_6.setText(_translate("codertool", "=》"))
        self.label_4.setText(_translate("codertool", "=》"))
        self.push_datetotime.setText(_translate("codertool", "转换"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("codertool", "时间戳"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("codertool", "json转换"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("codertool", "加密转换"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("codertool", "IP工具"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("codertool", "路由跟踪"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("codertool", "http请求"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("codertool", "单词翻译"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("codertool", "其它"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    codertool = QtWidgets.QMainWindow()
    ui = Ui_codertool()
    ui.setupUi(codertool)
    codertool.show()
    sys.exit(app.exec_())

