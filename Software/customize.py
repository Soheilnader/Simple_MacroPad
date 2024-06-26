import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QFileDialog
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
import qdarktheme

import configparser

import main


class CustomizeWindow(QWidget):
    apply_signal = pyqtSignal()     #for apply_button from customize window

    def __init__(self, button_index):
        super().__init__()
        uic.loadUi('customize.ui', self)
        self.button_select = ("Button_%d" % button_index)
        self.button_name = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                            10: '0', 11: 'A', 12: 'B'}

        self.setWindowTitle("Customize")
        self.setFixedSize(430, 340)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.init_config()
        self.set_enable_disable()





        self.radio_none.setChecked(self.str_to_bool(self.config[self.button_select]['None']))
        self.radio_key.setChecked(self.str_to_bool(self.config[self.button_select]['Key']))
        self.radio_text.setChecked(self.str_to_bool(self.config[self.button_select]['Text']))
        self.radio_audio.setChecked(self.str_to_bool(self.config[self.button_select]['Audio']))
        self.radio_exe.setChecked(self.str_to_bool(self.config[self.button_select]['Exe']))

        self.combo_1.setCurrentText(self.config[self.button_select]['key_item1'])
        self.combo_2.setCurrentText(self.config[self.button_select]['key_item2'])
        self.combo_3.setCurrentText(self.config[self.button_select]['key_item3'])

        self.combo_1.setEnabled(self.str_to_bool(self.config[self.button_select]['Key']))
        self.combo_2.setEnabled(self.str_to_bool(self.config[self.button_select]['Key']))
        self.combo_3.setEnabled(self.str_to_bool(self.config[self.button_select]['Key']))
        self.entry_text.setEnabled(self.str_to_bool(self.config[self.button_select]['Text']))
        self.entry_audio.setEnabled(self.str_to_bool(self.config[self.button_select]['Audio']))
        self.browse_audio.setEnabled(self.str_to_bool(self.config[self.button_select]['Audio']))
        self.entry_exe.setEnabled(self.str_to_bool(self.config[self.button_select]['Exe']))
        self.browse_exe.setEnabled(self.str_to_bool(self.config[self.button_select]['Exe']))

        # self.show()
        self.button_cancel.clicked.connect(self.dialog_close)
        self.button_apply.clicked.connect(self.apply_settings)
        self.button_back_color.clicked.connect(self.button_back_color_clicked)
        self.button_font_color.clicked.connect(self.button_font_color_clicked)
        self.button_hover_color.clicked.connect(self.button_hover_color_clicked)
        self.button_back_default.clicked.connect(self.button_back_color_default_clicked)
        self.button_font_default.clicked.connect(self.button_font_color_default_clicked)
        self.button_hover_default.clicked.connect(self.button_hover_color_default_clicked)

        self.radio_none.toggled.connect(self.radio_clicked)
        self.radio_key.toggled.connect(self.radio_clicked)
        self.radio_text.toggled.connect(self.radio_clicked)
        self.radio_audio.toggled.connect(self.radio_clicked)
        self.radio_exe.toggled.connect(self.radio_clicked)

        self.browse_audio.clicked.connect(self.browse_audio_clicked)
        self.browse_exe.clicked.connect(self.browse_exe_clicked)

        self.button_preview.setText(self.button_name[button_index])

    def init_config(self):
        self.config = configparser.ConfigParser()

        try:
            with open(r"config.ini", "r") as configfile:
                self.config.read('config.ini')
                self.path_audio = self.config[self.button_select]['audio_path']
                self.entry_audio.setText(self.path_audio)
                self.path_exe = self.config[self.button_select]['exe_path']
                self.entry_exe.setText(self.path_exe)
                self.text_string = self.config[self.button_select]['text_string']
                self.entry_text.setText(self.text_string)
                self.back_color = self.config[self.button_select]['color_background']
                self.font_color = self.config[self.button_select]['color_font']
                self.hover_color = self.config[self.button_select]['color_hover']
                self.entry_back_color.setText(self.back_color)
                self.entry_font_color.setText(self.font_color)
                self.entry_hover_color.setText(self.hover_color)
                self.button_preview.setStyleSheet("QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" %(self.back_color, self.font_color, self.hover_color))

        except:
            for i in range(1, 13):
                self.config['Button_%d' % i] = {'color_background': '#202124',
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
                self.config.write(configfile)
        print(self.config[self.button_select]['Audio'])

    def str_to_bool(self, text):
        if text == 'True':
            return True
        else:
            return False

    def radio_clicked(self):
        self.set_enable_disable()

    def apply_settings(self):
        print("apply")
        self.config.set(self.button_select, 'color_background', self.back_color)
        self.config.set(self.button_select, 'color_font', self.font_color)
        self.config.set(self.button_select, 'color_hover', self.hover_color)
        self.config.set(self.button_select, 'None', str(self.radio_none.isChecked()))
        self.config.set(self.button_select, 'Key', str(self.radio_key.isChecked()))
        self.config.set(self.button_select, 'Key_item1', self.combo_1.currentText())
        self.config.set(self.button_select, 'Key_item2', self.combo_2.currentText())
        self.config.set(self.button_select, 'Key_item3', self.combo_3.currentText())
        self.config.set(self.button_select, 'Text', str(self.radio_text.isChecked()))
        self.config.set(self.button_select, 'text_string', self.entry_text.text())
        self.config.set(self.button_select, 'Audio', str(self.radio_audio.isChecked()))
        self.config.set(self.button_select, 'audio_path', self.path_audio)
        self.config.set(self.button_select, 'Exe', str(self.radio_exe.isChecked()))
        self.config.set(self.button_select, 'exe_path', self.path_exe)

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

        self.apply_signal.emit()    #for apply_button from customize window

    def set_enable_disable(self):
        self.combo_1.setEnabled(self.radio_key.isChecked())
        self.combo_2.setEnabled(self.radio_key.isChecked())
        self.combo_3.setEnabled(self.radio_key.isChecked())

        self.entry_text.setEnabled(self.radio_text.isChecked())

        self.entry_audio.setEnabled(self.radio_audio.isChecked())
        self.browse_audio.setEnabled(self.radio_audio.isChecked())

        self.entry_exe.setEnabled(self.radio_exe.isChecked())
        self.browse_exe.setEnabled(self.radio_exe.isChecked())

    def browse_audio_clicked(self):
        self.path_audio = QFileDialog.getOpenFileName(self, "Open File", "", "Audio Files (*.mp3)")[0]
        try:
            print(self.path_audio)
            self.entry_audio.setText(self.path_audio)
        except:
            print("Error")

    def browse_exe_clicked(self):
        self.path_exe = QFileDialog.getOpenFileName(self, "Open File", "", "Executable Files (*.exe)")[0]
        try:
            print(self.path_exe)
            self.entry_exe.setText(self.path_exe)

        except:
            print("Error")

    def button_back_color_clicked(self):
        self.back_color = QtWidgets.QColorDialog.getColor().name()
        print(self.back_color)
        self.entry_back_color.setText(self.back_color)
        self.button_preview.setStyleSheet("QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (self.back_color, self.font_color, self.hover_color))

    def button_font_color_clicked(self):
        self.font_color = QtWidgets.QColorDialog.getColor().name()
        print(self.font_color)
        self.entry_font_color.setText(self.font_color)
        self.button_preview.setStyleSheet("QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (self.back_color, self.font_color, self.hover_color))

    def button_hover_color_clicked(self):
        self.hover_color = QtWidgets.QColorDialog.getColor().name()
        print(self.hover_color)
        self.entry_hover_color.setText(self.hover_color)
        self.button_preview.setStyleSheet("QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (self.back_color, self.font_color, self.hover_color))

    def button_back_color_default_clicked(self):
        self.back_color = '#202124'
        print(self.back_color)
        self.entry_back_color.setText(self.back_color)
        self.button_preview.setStyleSheet("QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (self.back_color, self.font_color, self.hover_color))

    def button_font_color_default_clicked(self):
        self.font_color = '#8ab4f7'
        print(self.font_color)
        self.entry_font_color.setText(self.font_color)
        self.button_preview.setStyleSheet("QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (self.back_color, self.font_color, self.hover_color))

    def button_hover_color_default_clicked(self):
        self.hover_color = '#272e3b'
        print(self.hover_color)
        self.entry_hover_color.setText(self.hover_color)
        self.button_preview.setStyleSheet("QPushButton {background-color: %s; color: %s;} QPushButton:hover {background-color: %s}" % (self.back_color, self.font_color, self.hover_color))

    def dialog_close(self):
        # main.MainWindow.setDisabled(False)
        self.destroy()
