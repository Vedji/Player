import sys,os, codecs
from myplayer2 import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from pygame import mixer
mixer.init()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        papka=os.getcwd()+'\\dir.txt'
        if(os.path.exists(papka)):
            file=open(u''+papka)
            self.ui.lineEdit.setText(file.read().strip())
            file.close()
            self.mode='mp3'

                             
        self.ui.pushButton.clicked.connect(self.scandisk)
        self.ui.listWidget.currentTextChanged.connect(self.getfiles)
        self.ui.listWidget_2.currentTextChanged.connect(self.playmusic)
        self.ui.pushButton_2.clicked.connect(self.playmusic)
        self.ui.pushButton_3.clicked.connect(self.stopmusic)
        self.ui.pushButton_4.clicked.connect(self.pausemusic)
        self.ui.pushButton_5.clicked.connect(self.unpausemusic)
        self.ui.pushButton_6.clicked.connect(self.previousmusic)
        self.ui.pushButton_7.clicked.connect(self.nextmusic)
        self.songs=[]
        self.flag=0
        self.stolb = 1
        self.scandisk()
   
        
    def scandisk(self): 
        self.mode='mp3'
        mas=[] 
        mas2=[]
        papka=str(self.ui.lineEdit.text()).strip()
        file = codecs.open(u'' + os.getcwd()+'\\dir.txt', "w", "utf-8")
        file.write(papka)
        file.close()
            
        for rootdir, dirs, files in os.walk(str(papka)):
            for file in files:       
                if((file.split('.')[-1])=='mp3'):
                    #добавляем путь до файла
                    mas.append(os.path.join(rootdir, file))
                    #добавляем название папки
                    mas2.append(os.path.join(rootdir, file).split('\\')[-2])
        #удаляем дубли папок
        mas2 = dict(zip(mas2, mas2)).values()
        self.mp3=mas
        self.ui.listWidget.clear()
        for x in mas2:
            self.ui.listWidget.addItem(x.strip())
        
    
    def getfiles(self):
        self.flag = 1
        self.mod ='song'
        self.songs = []
        self.ui.listWidget_2.clear()
        papkaname=self.ui.listWidget.currentItem().text()
        for x in self.mp3:
            mp3 = x.split('\\')[-2]
            if papkaname == mp3.strip():
                self.songs.append(x)
                self.ui.listWidget_2.addItem(x.split('\\')[-1])
        self.ui.listWidget_2.setFocus()
        self.flag = 0
        self.flajok = 0 #для previous и next
        self.itemflag = 0
        self.stolb = 0
        
    def playmusic(self):
        if self.flag == 0 and self.stolb == 0:
            if self.itemflag == 1:
                put = self.songs[self.selitem]
                mixer.music.stop()
                mixer.music.load(u''+ put)
                mixer.music.play()
                self.flajok = 1
                self.itemflag = 0
            else:
                self.selitem = self.ui.listWidget_2.currentRow()
                put = self.songs[self.selitem]
                mixer.music.stop()
                mixer.music.load(u''+ put)
                mixer.music.play()
                self.flajok = 1
                
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
            self.selitem = self.selitem - 1
            put = self.songs[self.selitem]
            mixer.music.stop()
            mixer.music.load(u''+ put)
            mixer.music.play()
    
    def nextmusic(self):
        if self.flajok == 1:
            mixer.music.stop()
            self.selitem = self.selitem + 1
            put=self.songs[self.selitem]
            mixer.music.stop()
            mixer.music.load(u''+ put)
            mixer.music.play()
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
