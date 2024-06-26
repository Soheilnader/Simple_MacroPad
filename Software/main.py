import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import uic, QtCore
import qdarktheme
import serial
import os
import keyboard
import configparser

import serialThread
import customize


class MainWindow(QMainWindow):
    apply_signal = QtCore.pyqtSignal()  #for apply_button from customize window
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Launch Pad")
        self.setFixedSize(450, 450)
        self.init_config()

        self.thread = {}

        self.apply_signal.connect(self.init_config) #for apply_button from customize window


        # Buttons
        self.button_start.clicked.connect(self.start_worker_1)
        self.button_stop.clicked.connect(self.stop_worker_1)
        self.button_exit.clicked.connect(self.app_close)

        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)
        self.button_3.clicked.connect(self.button_3_clicked)
        self.button_4.clicked.connect(self.button_4_clicked)
        self.button_5.clicked.connect(self.button_5_clicked)
        self.button_6.clicked.connect(self.button_6_clicked)
        self.button_7.clicked.connect(self.button_7_clicked)
        self.button_8.clicked.connect(self.button_8_clicked)
        self.button_9.clicked.connect(self.button_9_clicked)
        self.button_A.clicked.connect(self.button_A_clicked)
        self.button_0.clicked.connect(self.button_0_clicked)
        self.button_B.clicked.connect(self.button_B_clicked)

        # Menus
        self.menu_quit.triggered.connect(self.app_close)
        # self.about_quit.triggered.connect(self.app_close)
        self.menu_start.triggered.connect(self.start_worker_1)
        self.menu_stop.triggered.connect(self.stop_worker_1)

        self.action1.triggered.connect(self.button_1_clicked)
        self.action2.triggered.connect(self.button_2_clicked)
        self.action3.triggered.connect(self.button_3_clicked)
        self.action4.triggered.connect(self.button_4_clicked)
        self.action5.triggered.connect(self.button_5_clicked)
        self.action6.triggered.connect(self.button_6_clicked)
        self.action7.triggered.connect(self.button_7_clicked)
        self.action8.triggered.connect(self.button_8_clicked)
        self.action9.triggered.connect(self.button_9_clicked)
        self.actionA.triggered.connect(self.button_A_clicked)
        self.action0.triggered.connect(self.button_0_clicked)
        self.actionB.triggered.connect(self.button_B_clicked)


    def button_1_clicked(self):
        print("1")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(1)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
        # self.setDisabled(True)

    def button_2_clicked(self):
        print("2")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(2)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()

    def button_3_clicked(self):
        print("3")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(3)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_4_clicked(self):
        print("4")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(4)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_5_clicked(self):
        print("5")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(5)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_6_clicked(self):
        print("6")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(6)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_7_clicked(self):
        print("7")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(7)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_8_clicked(self):
        print("8")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(8)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_9_clicked(self):
        print("9")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(9)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_A_clicked(self):
        print("A")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(11)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_0_clicked(self):
        print("0")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(10)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def button_B_clicked(self):
        print("B")
        self.init_config()
        self.secondwindow = customize.CustomizeWindow(12)
        self.secondwindow.apply_signal.connect(self.init_config)    #for apply_button from customize window
        self.secondwindow.show()
    def app_close(self):
        QApplication.quit()

    def init_config(self):
        config = configparser.ConfigParser()
        try:
            with open(r"config.ini", "r") as configfile:
                config.read('config.ini')
        except:
            for i in range(1, 13):
                config['Button_%d' % i] = {'color_background': '#202124',
                                                'color_font': '#8ab4f7',
                                                'color_hover': '#272e3b',
                                                'None': True,
                                                'Key': False,
                                                'Key_item1': 'None',
                                                'Key_item2': 'None',
                                                'Key_item3': 'None',
                                                'Text': False,
                                                'Text_string': '',
                                                'Audio': False,
                                                'Audio_path': '',
                                                'Exe': False,
                                                'Exe_path': ''
                                                }
            with open(r"config.ini", "w") as configfile:
                config.write(configfile)

        self.buttons_style_load(config)

        print(config['Button_1']['Audio'])

    def start_worker_1(self):
        self.thread[1] = serialThread.ThreadClass(index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.button_pressed)


    def stop_worker_1(self):
        try:
            self.thread[1].stop()
        except:
            print("Thread is already stopped!")

    def button_pressed(self, data):
        index = self.sender().index

    def buttons_style_load(self, config):
        self.button_1.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_1']['color_background'], config['Button_1']['color_font'],
            config['Button_1']['color_hover']))
        self.button_2.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_2']['color_background'], config['Button_2']['color_font'],
            config['Button_2']['color_hover']))
        self.button_3.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_3']['color_background'], config['Button_3']['color_font'],
            config['Button_3']['color_hover']))

        self.button_4.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_4']['color_background'], config['Button_4']['color_font'],
            config['Button_4']['color_hover']))
        self.button_5.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_5']['color_background'], config['Button_5']['color_font'],
            config['Button_5']['color_hover']))
        self.button_6.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_6']['color_background'], config['Button_6']['color_font'],
            config['Button_6']['color_hover']))

        self.button_7.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_7']['color_background'], config['Button_7']['color_font'],
            config['Button_7']['color_hover']))
        self.button_8.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_8']['color_background'], config['Button_8']['color_font'],
            config['Button_8']['color_hover']))
        self.button_9.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_9']['color_background'], config['Button_9']['color_font'],
            config['Button_9']['color_hover']))

        self.button_A.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_11']['color_background'], config['Button_11']['color_font'],
            config['Button_11']['color_hover']))
        self.button_0.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_10']['color_background'], config['Button_10']['color_font'],
            config['Button_10']['color_hover']))
        self.button_B.setStyleSheet(
            "QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (
            config['Button_12']['color_background'], config['Button_12']['color_font'],
            config['Button_12']['color_hover']))

    def closeEvent(self, event) -> None:
        print("Close")


if __name__ == '__main__':
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
