# -*- coding: utf-8 -*-

"""
Module implementing codertool.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import urllib, urllib.parse, urllib.request, time, re, cgi
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
    
    @pyqtSlot()
    def on_push_timetodate_clicked(self):
        #QMessageBox.information(self, '测试', '测试')
        from_timestamp = self.timestamp2.text().strip()
        #QMessageBox.information(self, '测试', from_timestamp)
        #判断值是否为空，并且必须为数字
        if from_timestamp=='':
            QMessageBox.information(self, '提示', '请填写时间戳！')
            return
        QMessageBox.information(self, '提示', re.match('^[0-9]+$', from_timestamp));
        if re.match('^[0-9]+$', from_timestamp)==None:
            QMessageBox.information(self, '提示', '必须填写数字！')
            return
        QMessageBox.information(self, '提示', from_timestamp)
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_push_datetotime_clicked(self):
        """
        Slot documentation goes here.
        """
        #raise NotImplementedError


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    dlg = codertool()
    dlg.show()
    sys.exit(app.exec_())
