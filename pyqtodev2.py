from PyQt4.QtGui import *
from PyQt4.QtCore import *

class devirHizi(QDialog):
    def __init__(self,ebeveyn=None):
        super(devirHizi,self).__init__(ebeveyn)

        grid=QGridLayout()
        grid.addWidget(QLabel("Personel Devir Hızı Hesaplama"))

        grid.addWidget(QLabel("Aybaşı Çalışan Sayısı:"),1,0)

        self.aybasiCalisan=QLineEdit()
        grid.addWidget(self.aybasiCalisan,1,1)

        grid.addWidget(QLabel("Aysonu Çalışan Sayısı:"),2,0)

        self.aysonuCalisan=QLineEdit()
        grid.addWidget(self.aysonuCalisan,2,1)

        grid.addWidget(QLabel("İşten Çıkan Personel Sayısı:"),3,0)

        self.istenCikan=QLineEdit()
        grid.addWidget(self.istenCikan,3,1)

        grid.addWidget(QLabel("Personel Devir Hızınız(%):"),4,0)
        self.sonucOran=QLabel("Sonuç")
        grid.addWidget(self.sonucOran,4,1)

        hesaplaDugme=QPushButton("Hesapla")
        grid.addWidget(hesaplaDugme,5,1,1,2)
        self.connect(hesaplaDugme,SIGNAL('pressed()'),self.hesapla)

        self.setLayout(grid)
        self.setWindowTitle("Turnover")

    def hesapla(self):
        abCa=int(self.aybasiCalisan.text())
        asCa=int(self.aysonuCalisan.text())
        iC=int(self.istenCikan.text())
        sonuc=(iC/((abCa+asCa)/2))*100
        self.sonucOran.setText('<font color="blue"><b>%0.1f</b></font>'%sonuc)

uygulama=QApplication([])
pencere=devirHizi()
pencere.show()
uygulama.exec_
