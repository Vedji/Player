import sys, os
import shutil
from GUIplayer import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QWidget, QMainWindow
from PyQt5.QtCore import Qt
import pygame
from pygame import mixer
mixer.init()


class MyWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            file = open(str(os.getcwd()) + 'dir.txt', 'r')
            file = file.read()
            if file != '':
                self.lineEdit.setText(file)
            file.close()
        except:
            pass
        
        try:
            file1 = open(str(os.getcwd()) + 'Papka1.txt', 'r')
            file1 = file1.read()
            self.lineEdit_2.setText(file1)       
            file1.close()
        except:
            pass
        
        try:
            file2 = open(str(os.getcwd()) + 'Papka2.txt', 'r')
            file2 = file2.read()
            self.lineEdit_5.setText(file2)               
            file2.close()
        except:
            pass
        
        try:
            file3 = open(str(os.getcwd()) + 'Papka3.txt', 'r')
            file3 = file3.read()
            self.lineEdit_7.setText(file3)
            file3.close()
        except:
            pass
        
        self.pushButton.clicked.connect(self.scandisk)
        self.listWidget.currentTextChanged.connect(self.getfiles)
        self.listWidget_2.currentTextChanged.connect(self.playmusic)
        self.pushButton_2.clicked.connect(self.playmusic)
        self.pushButton_3.clicked.connect(self.stopmusic)
        self.pushButton_4.clicked.connect(self.pausemusic)
        self.pushButton_5.clicked.connect(self.unpausemusic)
        self.pushButton_6.clicked.connect(self.previousmusic)
        self.pushButton_7.clicked.connect(self.nextmusic)
        self.pushButton_8.clicked.connect(self.papka1)
        self.pushButton_9.clicked.connect(self.hot_key_1)
        self.pushButton_10.clicked.connect(self.papka2)
        self.pushButton_11.clicked.connect(self.hot_key_2)
        self.pushButton_12.clicked.connect(self.papka3)
        self.pushButton_13.clicked.connect(self.hot_key_3)
        self.pushButton_14.clicked.connect(self.re)
        
        self.songs = []
        self.flag = 0
        self.stolb = 1
        self.re_music = False
        self.flajok = 0  # for previous and next
        self.itemflag = 0  # for stop and play music
        self.stolb = 0  # for playmusic
        self.selitem = None               
        self.flag = 0

        self.scandisk()
        
        self.HoKe = None
        self.HoKe1 = None
        self.HoKe2 = None
        
    def scandisk(self):
        mas = [] 
        mas2 = []
        papka = str(self.lineEdit.text())
        file = open(os.getcwd() + 'dir.txt', 'w')
        file.write(papka)
        file.close()
            
        for rootdir, dirs, files in os.walk(str(papka)):
            for file in files:       
                if (file.split('.')[-1]) == 'mp3':
                    #add file names 
                    mas.append(os.path.join(rootdir, file))
                    #add file paths
                    mas2.append(os.path.join(rootdir, file).split('\\')[-2])
        #delete duplicates
        mas2 = dict(zip(mas2, mas2)).values()
        self.mp3 = mas
        self.listWidget.clear()
        for x in mas2:
            self.listWidget.addItem(x.strip())
        
    def getfiles(self):
        self.flag = 1
        self.songs = []
        self.listWidget_2.clear()
        papkaname = self.listWidget.currentItem().text()
        for x in self.mp3:
            mp3 = x.split('\\')[-2]
            if papkaname == mp3.strip():
                self.songs.append(x)
                self.listWidget_2.addItem(x.split('\\')[-1])
        self.listWidget_2.setFocus()
        self.flag = 0     
        
    def playmusic(self):
        if self.flag == 0 and self.stolb == 0:
            if self.itemflag == 0:
                self.selitem = self.listWidget_2.currentRow()
                put = self.songs[self.selitem]
                mixer.music.stop()
                mixer.music.load(put)
                if self.re_music is False:
                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                elif self.re_music == 1:
                    mixer.music.set_volume(0.7)
                    mixer.music.play(2)
                elif self.re_music == -1:
                    mixer.music.set_volume(0.7)
                    mixer.music.play(-1)
                self.flajok = 1
                
            else:
                if self.selitem == self.listWidget_2.currentRow():
                    put = self.songs[self.selitem]
                    mixer.music.stop()
                    mixer.music.load(put)
                    if self.re_music is False:
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                    elif self.re_music == 1:
                        mixer.music.set_volume(0.7)
                        mixer.music.play(2)
                    elif self.re_music == -1:
                        mixer.music.set_volume(0.7)
                        mixer.music.play(-1)
                    self.flajok = 1             
                    self.itemflag = 0
                    
                else:
                    put = self.songs[self.selitem]
                    mixer.music.stop()
                    mixer.music.load(put)
                    if self.re_music is False:
                        mixer.music.set_volume(0.7)
                        mixer.music.play()
                    elif self.re_music == 1:
                        mixer.music.set_volume(0.7)
                        mixer.music.play(2)
                    elif self.re_music == -1:
                        mixer.music.set_volume(0.7)
                        mixer.music.play(-1)
                    self.flajok = 1
                    self.itemflag = 0           
            name_mp3 = put.split('\\')[-1]
            self.label_13.setText(name_mp3)
        
    def stopmusic(self):
        mixer.music.stop()
        self.itemflag = 1
    
    def pausemusic(self):
        mixer.music.pause()
        
    def unpausemusic(self):
        mixer.music.unpause()
    
    def previousmusic(self):
        if self.flajok == 1:
            mixer.music.stop()
            if self.selitem - 1 < 0:
                self.selitem = len(self.songs) - 1
            else:
                self.selitem = self.selitem - 1
            put = self.songs[self.selitem]
            mixer.music.stop()
            mixer.music.load(put)
            if self.re_music is False:
                mixer.music.set_volume(0.7)
                mixer.music.play()
            elif self.re_music == 1:
                mixer.music.set_volume(0.7)
                mixer.music.play(2)
            elif self.re_music == -1:
                mixer.music.set_volume(0.7)
                mixer.music.play(-1)
            name_mp3 = put.split('\\')[-1]
            self.label_13.setText(name_mp3)
            
    def nextmusic(self):
        if self.flajok == 1:
            mixer.music.stop()
            if self.selitem + 1 == len(self.songs):
                self.selitem = 0
            else:
                self.selitem = self.selitem + 1
            put=self.songs[self.selitem]
            mixer.music.stop()
            mixer.music.load(put)
            if self.re_music is False:
                mixer.music.set_volume(0.7)
                mixer.music.play()
            elif self.re_music == 1:
                mixer.music.set_volume(0.7)
                mixer.music.play(2)
            elif self.re_music == -1:
                mixer.music.set_volume(0.7)
                mixer.music.play(-1)
            name_mp3 = put.split('\\')[-1]
            self.label_13.setText(name_mp3)
            
    def re(self):
        if self.re_music is False:
            self.pushButton_14.setText("Повтор 1X")
            self.re_music = 1
        elif self.re_music == 1:
            self.pushButton_14.setText("Повтор ∞")
            self.re_music = -1
        elif self.re_music == -1:
            self.pushButton_14.setText("Повтор отк.")
            self.re_music = False
            
    def papka1(self):
        papka1 = str(self.lineEdit_2.text()).strip()
        file = open('Papka1.txt', 'w')
        file.write(papka1)
        file.close()
        
    def hot_key_1(self):
        i, okBtnPressed = QInputDialog.getItem(
            self, "Выберите горячую клавишу", "Выберите горячую клавишу",
            ("ctrl+alt+1", "ctrl+alt+2", "ctrl+alt+3"),
            0,
            False)
        if okBtnPressed:
            self.HoKe = i
            self.pushButton_9.setText(i)
    
    def papka2(self):
        papka2 = str(self.lineEdit_5.text()).strip()
        file = open('Papka2.txt', 'w')
        file.write(papka2)
        file.close()
        
    def hot_key_2(self):
        i, okBtnPressed = QInputDialog.getItem(
            self, "Выберите горячую клавишу", "Выберите горячую клавишу",
            ("ctrl+alt+1", "ctrl+alt+2", "ctrl+alt+3"),
            1,
            False)
        if okBtnPressed:
            self.HoKe1 = i
            self.pushButton_11.setText(i)
            
    def papka3(self):
        papka3 = str(self.lineEdit_7.text()).strip()
        file = open('Papka3.txt', 'w')
        file.write(papka3)
        file.close()
        
    def hot_key_3(self):
        i, okBtnPressed = QInputDialog.getItem(
            self, "Выберите горячую клавишу", "Выберите горячую клавишу",
            ("ctrl+alt+1", "ctrl+alt+2", "ctrl+alt+3"),
            2,
            False)
        if okBtnPressed:
            self.HoKe2 = i
            self.pushButton_13.setText(i)
            
    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.AltModifier + Qt.ControlModifier):
            if self.HoKe == 'ctrl+alt+1' and self.HoKe1 != 'ctrl+alt+1' and self.HoKe2 != 'ctrl+alt+1':
                if event.key() == Qt.Key_1:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_2.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe == 'ctrl+alt+1':
                print('Error: hotkey ctrl+alt+1 is fixed')
            if self.HoKe == 'ctrl+alt+2' and self.HoKe1 != 'ctrl+alt+2' and self.HoKe2 != 'ctrl+alt+2':
                if event.key() == Qt.Key_2:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_2.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe == 'ctrl+alt+2':
                print('Error: hotkey ctrl+alt+2 is fixed')
            if self.HoKe == 'ctrl+alt+3' and self.HoKe1 != 'ctrl+alt+3' and self.HoKe2 != 'ctrl+alt+3' :
                if event.key() == Qt.Key_3:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_2.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)  
            elif self.HoKe == 'ctrl+alt+3':
                print('Error: hotkey ctrl+alt+3 is fixed')  

            if self.HoKe1 == 'ctrl+alt+1' and self.HoKe != 'ctrl+alt+1' and self.HoKe2 != 'ctrl+alt+1':
                if event.key() == Qt.Key_1:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_5.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe1 == 'ctrl+alt+1':
                print('Error: hotkey ctrl+alt+1 is fixed')
            if self.HoKe1 == 'ctrl+alt+2' and self.HoKe != 'ctrl+alt+2' and self.HoKe2 != 'ctrl+alt+2':
                if event.key() == Qt.Key_2:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_5.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe1 == 'ctrl+alt+2':
                print('Error: hotkey ctrl+alt+2 is fixed')
            if self.HoKe1 == 'ctrl+alt+3' and self.HoKe != 'ctrl+alt+3' and self.HoKe2 != 'ctrl+alt+3':
                if event.key() == Qt.Key_3:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_5.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe1 == 'ctrl+alt+3':
                print('Error: hotkey ctrl+alt+3 is fixed')                       

            if self.HoKe2 == 'ctrl+alt+1' and self.HoKe != 'ctrl+alt+1' and self.HoKe1 != 'ctrl+alt+1':
                if event.key() == Qt.Key_1:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_7.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe2 == 'ctrl+alt+1':
                print('Error: hotkey ctrl+alt+1 is fixed')   
                
            if self.HoKe2 == 'ctrl+alt+2' and self.HoKe != 'ctrl+alt+2' and self.HoKe1 != 'ctrl+alt+2':
                if event.key() == Qt.Key_2:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_7.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe2 == 'ctrl+alt+2':
                print('Error: hotkey ctrl+alt+2 is fixed')     
                
            if self.HoKe2 == 'ctrl+alt+3' and self.HoKe != 'ctrl+alt+3' and self.HoKe1 != 'ctrl+alt+3':
                if event.key() == Qt.Key_3:
                    try:
                        shutil.copy(self.songs[self.selitem], str(self.lineEdit_7.text()).strip())
                    except Exception as e:
                        print(e.__class__.__name__)
            elif self.HoKe2 == 'ctrl+alt+3':
                print('Error: hotkey ctrl+alt+3 is fixed') 
                
            if event.key() == Qt.Key_S:
                self.playmusic()
            if event.key() == Qt.Key_T:
                self.stopmusic()
            if event.key() == Qt.Key_P:
                self.pausemusic()
            if event.key() == Qt.Key_U:
                self.unpausemusic()
            if event.key() == Qt.Key_Z:
                self.previousmusic()
            if event.key() == Qt.Key_X:
                self.nextmusic()
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
