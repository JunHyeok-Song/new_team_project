import io
import sys
import folium
from folium import Marker
from PyQt5.QtCore import Qt, QTimer
from PyQt5.Qt import QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGridLayout

from map_fuction import Ui_Mapfuction


class MapFunction(QWidget, Ui_Mapfuction):
    def __init__(self, latitude_, longitude_):
        super().__init__()
        self.setupUi(self)
        self.resize(1000, 1000)
        # self.a = mpmp
        # # self.a.real_map()
        # self.label_1 = QWidget(self)
        # self.laout_ = QVBoxLayout(self.label_1)
        # self.laout_.addWidget(self.a)
        # self.label_1.resize(1000, 1000)
        # self.label_1.show()

        self.map_ = folium.Map(location=[latitude_, longitude_], zoom_start=16)
        Marker(location=[latitude_, longitude_]).add_to(self.map_)
        data = io.BytesIO()
        self.map_.save(data, close_file=False)

        self.webview = QWebEngineView(self)
        self.webview.setHtml(data.getvalue().decode())
        self.gridLayout.addWidget(self.webview)

    # def initself(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapwidget = MapFunction(35.08639259, 128.8811301)
    mapwidget.show()
    sys.exit(app.exec_())