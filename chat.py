#!/usr/bin/env python

import sys
import time

from telnetlib import Telnet


from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction
from threading import Thread, Lock

from lyachat_window import Ui_LYAChatWindow


class TelnetThread(Thread):
    do_disconnect = False
    connected = False
    thread_started = False
    on4kst = Telnet()

    def __init__(self):
        Thread.__init__(self)
        self.telnet_username = ""
        self.telnet_password = ""
        self.telnet_chat_id = 2
        self.telnet_hostname = "www.on4kst.info"
        self.telnet_port = 23000

    def set_credentials(self, username, password, chat_id):
        self.telnet_username = username
        self.telnet_password = password
        self.telnet_chat_id = chat_id

    def run(self):
        self.thread_started = True
        self.on4kst.open(self.telnet_hostname,self.telnet_port)
        try:
            self.on4kst.read_until(b"Login:")
            self.on4kst.write(self.telnet_username + b"\n")
            self.on4kst.read_until(b"Password:")
            self.on4kst.write(self.telnet_password + b"\n")
            response = self.on4kst.expect(b"Your choice           :", 1)
            if response[0] < 0:
                print('Login not accepted')
                raise RuntimeError("Unable to login")
        
            else:
                print('Login accepted! Woohoo')
                self.connected = True
                self.on4kst.write(str(self.telnet_chat_id) + b"\n") 
        except:
            return False
        return True

    def stop(self):
        self.do_disconnect = True
        self.started = False


class MainWindow(QMainWindow, Ui_LYAChatWindow):
    tt = TelnetThread()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setupActions()

    def setupActions(self):
        self.connect.clicked.connect(self.start_telnet_thread)
        self.disconnect.clicked.connect(self.stop_telnet_thread)

    def start_telnet_thread(self):
        self.tt.set_credentials(self.username.text(), self.password.text(), 2)
        self.textEdit.append(
            "Connecting to " + self.tt.telnet_hostname + " as " + self.username.text()
        )
        if not self.tt.thread_started:
            self.tt.start()
            time.sleep(1)
        if self.tt.connected:
            while True:
                self.textEdit.append(self.tt.update())
                print('Polling loop')
                time.sleep(1)

    def stop_telnet_thread(self):
        self.tt.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
