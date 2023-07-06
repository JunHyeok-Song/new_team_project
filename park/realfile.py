"""Schedule Function
일정표 = id, name, image, pos세부기능 id로 db검색"""
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QFrame, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.uic.properties import QtGui

from addSchedule import AddSchedule_Function
from schedule_function import Ui_Form as adschedule_ui
import testdb


class ScheduleFunction(QWidget, adschedule_ui):
    def __init__(self):
        super().__init__()
        self.setui_intit()
        self.in_widget_function()
        self.pushButton.clicked.connect(self.add_btn)
        self.add_item()
        self.cnt_ = 0
    def setui_intit(self):
        self.setupUi(self)
        self.name_settext("박호현")

    def add_btn(self):
        a = AddSchedule_Function()
        data_value = testdb.DataBaseClass()
        value_list = data_value.main_db(1, "전체")
        a.add_result_function(value_list[f"{self.cnt_}"]["이미지"], value_list[f"{self.cnt_}"]["업체명"], None,
                              value_list[f"{self.cnt_}"]["주소"], value_list[f"{self.cnt_}"]["시군구명"], value_list[f"{self.cnt_}"]["전화번호"])
        self.vlaout.insertWidget(len(self.vlaout) - 1, a)
        self.cnt_ += 1
        if self.cnt_ == len(value_list):
            self.cnt_ = 0

    def add_item(self):
        self.vspacer = QSpacerItem(20, 100, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.vlaout.addItem(self.vspacer)

    def in_widget_function(self):
        """스크롤 위젯 설정"""
        self.vlaout = QVBoxLayout(self)
        widget = QWidget(self)
        widget.setLayout(self.vlaout)
        self.scrollArea.setWidget(widget)

    def name_settext(self, name):
        self.label.setText(name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sub_function = ScheduleFunction()

    sub_function.show()
    app.exec_()
