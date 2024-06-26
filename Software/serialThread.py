import serial
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5 import uic, QtCore, QtWidgets
import keyboard
import configparser
from main import MainWindow
import os
import pygame

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, index=0):
        super(ThreadClass, self).__init__()
        self.index = index
        #self.is_running = True
        try:
            self.is_running = True
            self.ser = serial.Serial(
                port='COM4',  # replace with the serial port of your device
                baudrate=9600,  # set the baud rate
                timeout=1  # set a timeout value for reading
            )
        except:
            self.is_running = False
            print("Uart Failed!")
            self.show_popup()


        self.config = configparser.ConfigParser()
        try:
            with open(r"config.ini", "r") as configfile:
                self.config.read('config.ini')
        except:
            print("Error")

    def run(self):
        print("Start")
        while True:
            if self.is_running == True:
                data = self.ser.readline().decode().strip()
                if data == '1':
                    self.command('1')
                if data == '2':
                    self.command('2')
                if data == '3':
                    self.command('3')
                if data == '4':
                    self.command('4')
                if data == '5':
                    self.command('5')
                if data == '6':
                    self.command('6')
                if data == '7':
                    self.command('7')
                if data == '8':
                    self.command('8')
                if data == '9':
                    self.command('9')
                if data == '0':
                    self.command('10')
                if data == 'A':
                    self.command('11')
                if data == 'B':
                    self.command('12')
                self.any_signal.emit(data)

    def command(self, num):
        if self.config['Button_%s' %num]['None'] == 'True':
            pass
        elif self.config['Button_%s' %num]['Key'] == 'True':
            if self.config['Button_%s' %num]['Key_item3'] == 'None':
                if self.config['Button_%s' %num]['Key_item2'] == 'None':
                    if self.config['Button_%s' %num]['Key_item1'] == 'None':
                        pass
                    else:
                        keyboard.send(self.config['Button_%s' %num]['Key_item1'].lower())
                else:
                    keyboard.send(self.config['Button_%s' %num]['Key_item1'].lower() + '+' + self.config['Button_%s' %num][
                        'Key_item2'].lower())
            else:
                keyboard.send(self.config['Button_%s' %num]['Key_item1'].lower() + '+' + self.config['Button_%s' %num][
                    'Key_item2'].lower() + '+' + self.config['Button_%s' %num]['Key_item3'].lower())

        elif self.config['Button_%s' %num]['Text'] == 'True':
            keyboard.write(self.config['Button_%s' %num]['text_string'])
        elif self.config['Button_%s' %num]['Audio'] == 'True':
            pygame.init()
            pygame.mixer.music.load(self.config['Button_%s' %num]['audio_path'])
            pygame.mixer.music.play()
        elif self.config['Button_%s' %num]['Exe'] == 'True':
            os.system(self.config['Button_%s' %num]['exe_path'])
        # MainWindow.button_1.animateClick()

    def stop(self):
        self.is_running = False
        print("stop")
        self.ser.close()
        self.terminate()


    def show_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error !")
        msg.setText("Could not connect with UART !\nTry to change options from Settings -> Preferences.")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        #msg.setDefaultButton(QtWidgets.QMessageBox.Retry)
        #msg.setInformativeText("informative text, ya!")

        #msg.setDetailedText("details")
        msg.exec_()