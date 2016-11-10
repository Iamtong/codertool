# -*- coding: utf-8 -*-

"""
Module implementing codertool.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import urllib, urllib.parse, urllib.request, time, re, cgi, datetime
from Ui_codertool import Ui_codertool


class codertool(QMainWindow, Ui_codertool):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(codertool, self).__init__(parent)
        self.setupUi(self)
        self.getNowtime()
    #初始化信息
    def getNowtime(self):
        now_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
        now_timestamp = str(int(time.time()))
        self.dateTime3.setText(now_date)
        self.timestamp2.setText(now_timestamp)
        return
    @pyqtSlot()
    def on_push_timetodate_clicked(self):
        #QMessageBox.information(self, '测试', '测试')
        from_timestamp = self.timestamp2.text().strip()
        #QMessageBox.information(self, '测试', from_timestamp)
        #判断值是否为空，并且必须为数字
        if from_timestamp=='':
            QMessageBox.information(self, '提示', '请填写时间戳！')
            return
        regx = re.compile(r"^[0-9]{10}$");
        if regx.match( from_timestamp)==None:
            QMessageBox.information(self, '提示', '必须填写10位数字！')
            return
        #QMessageBox.information(self, '提示', from_timestamp)
        todatetime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(from_timestamp)))
        #QMessageBox.information(self, '提示', todatetime)
        self.dateTime2.setText(todatetime)
        #raise NotImplementedError
        return 
    
    @pyqtSlot()
    def on_push_datetotime_clicked(self):
        """
        Slot documentation goes here.
        """
        from_datetime = self.dateTime3.text().strip()
        if from_datetime=='':
            QMessageBox.information(self, '提示', '请填写日期格式！')
            return
        regx = re.compile(r"^[0-9]{4}\-[0-1][0-9]\-[0-3][0-9] [0-1][0-9]:[0-5][0-9]:[0-5][0-9]$");
        if regx.match( from_datetime)==None:
            QMessageBox.information(self, '提示', '必须填写2015-11-12 12:12:12格式的时间！')
            return
        date_tmp=datetime.datetime.strptime(str(from_datetime),"%Y-%m-%d %H:%M:%S")
        to_timestamp = str(int(time.mktime(date_tmp.timetuple())))
        self.timestamp3.setText(to_timestamp)
        return



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    dlg = codertool()
    dlg.show()
    sys.exit(app.exec_())
