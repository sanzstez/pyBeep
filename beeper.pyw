#-*- coding: UTF-8 -*-

from PyQt4 import QtGui,QtCore  # импорт ядра GUI
import sys, time
from winsound import Beep

__version__ = u'Stets BeepER (1.0.0) MurKa and Йолочка Edition'

# создание кнопачек
class Button(QtGui.QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size    

# главный класс проги
class Program(QtGui.QWidget):
        def __init__(self,parent=None):
                QtGui.QWidget.__init__(self, parent,  QtCore.Qt.WindowSystemMenuHint | 
                                                     QtCore.Qt.WindowStaysOnTopHint) # Иниц отрисовки QT
                splash = QtGui.QSplashScreen(QtGui.QPixmap('images/loading.png'))
                splash.showMessage(u'Программа загружается...',QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
                splash.show()
                QtGui.qApp.processEvents()

                self.setWindowIcon(QtGui.QIcon('images/icon.jpg')) # иконка окна проги
                self.setFixedSize(750, 350) # фиксированный размер окна

                self.originalPixmap = QtGui.QApplication.desktop().screen(0)
                x = (self.originalPixmap.width() - self.width())/2
                y = (self.originalPixmap.height() - self.height())/2

                self.move(x,y)
                self.setWindowOpacity(0.9) # прозрачность окна
                self.setWindowIconText(__version__)
                self.setWindowTitle(__version__)

                self.paint_buttons() # рисуем кнопачки
                self.signals() # иниц обработку сигналов

                splash.finish(self)
                self.show() #  показываем главное окно
         
        # рисуем кнопачки
        def paint_buttons(self):  
            self.digitButtons = []
        
            for i in range(65,91):
                self.digitButtons.append(self.createButton(str(chr(i)),self.beeper))

            self.yolka = QtGui.QPushButton(u'Йолочка')
            self.murka = QtGui.QPushButton(u'Мурка')
            self.classic = QtGui.QPushButton(u'Классика')
            self.vagon = QtGui.QPushButton(u'Чебурашка')
            self.tetris = QtGui.QPushButton(u'Тетрис')
            self.xz = QtGui.QPushButton(u'Track 1')
            self.exit = QtGui.QPushButton(u'Да ухожу...')
            self.labelinfo = QtGui.QLabel(u'<b>Код симовола:</b>', self)
            
            mainLayout = QtGui.QGridLayout()
                        
            mainLayout.addWidget(self.yolka)
            mainLayout.addWidget(self.murka)
            mainLayout.addWidget(self.classic)
            mainLayout.addWidget(self.vagon)
            mainLayout.addWidget(self.tetris)
            mainLayout.addWidget(self.xz)
            mainLayout.addWidget(self.exit)
            mainLayout.addWidget(self.labelinfo)

        
            for i in range(1, 25):
                row = ((25 - i) / 3) + 2
                column = ((i - 1) % 3) + 1
                mainLayout.addWidget(self.digitButtons[i], row, column)
                
            self.setLayout(mainLayout)
           
        # пищалик кнопачек 
        def beeper(self):
            clickedButton = self.sender()
            digitValue = str(clickedButton.text())
            int_val = ord(digitValue)
            
            if  65 < int_val <75:
                add = 300
            elif 75 < int_val <85:
                add = 700
            elif 85 < int_val <95:
                add = 1100
            elif 95 < int_val <105:
                add = 2100
            elif 105 < int_val <130:
                add = 3100
            else:
                add = 6000
                
            beep = int_val+add
            Beep(beep,500)
            self.labelinfo.setText(u'<b>Код: '+str(int_val)+'</b>')
         
        # создание кнопачки от класса       
        def createButton(self, text, member):
            button = Button(text)
            button.setShortcut(text)
            button.clicked.connect(member)
            return button
                
        # pi Yolka
        def beep_yolka(self):
            Beep(247, 500)
            Beep(417, 500)
            Beep(417, 500)
            Beep(370, 500)
            Beep(417, 500)
            Beep(329, 500)
            Beep(247, 500)
            Beep(247, 500)
            Beep(247, 500)
            Beep(417, 500)
            Beep(417, 500)
            Beep(370, 500)
            Beep(417, 500)
            Beep(497, 500)
            time.sleep(0.5)
            Beep(497, 500)
            Beep(277, 500)
            Beep(277, 500)
            Beep(440, 500)
            Beep(440, 500)
            Beep(417, 500)
            Beep(370, 500)
            Beep(329, 500)
            Beep(247, 500)
            Beep(417, 500)
            Beep(417, 500)
            Beep(370, 500)
            Beep(417, 500)
            Beep(329, 500)
            
        # pi Murka
        def beep_murka(self):
            Beep(163, 500)
            time.sleep(0.5)
            Beep(163, 500)
            Beep(154, 500)
            Beep(163, 500)
            Beep(173, 500)
            Beep(163, 500)
            time.sleep(1)

            Beep(146, 500)
            Beep(130, 500)
            Beep(122, 500)
            Beep(130, 500)
            Beep(122, 500)
            Beep(219, 500)
            time.sleep(1)

            Beep(219, 500)
            time.sleep(0.5)
            Beep(219, 500)
            Beep(208, 500)
            Beep(219, 500)
            Beep(247, 500)
            Beep(219, 500)
            Beep(208, 500)
            Beep(219, 500)
            Beep(247, 500)
            time.sleep(1)

            Beep(262, 500)
            Beep(246, 500)
            Beep(219, 500)
            Beep(208, 500)
            Beep(247, 500)
            Beep(219, 500)
            time.sleep(0.5)
            Beep(219, 500)
            Beep(247, 500)
            Beep(173, 500)
            Beep(163, 500)
            Beep(247, 500)
            Beep(173, 500)
            time.sleep(0.5)

            Beep(163, 500)
            Beep(163, 500)
            Beep(194, 500)
            Beep(173, 500)
            Beep(163, 500)
            Beep(145, 500)
            Beep(130, 500)
            Beep(123, 500)
            Beep(110, 500)
        
        def beep_classic(self):
            Beep ( 659, 120 ) 
            Beep ( 337, 120 )
            Beep ( 622, 120 )
            Beep ( 337, 120 )

            Beep ( 659, 120 )
            Beep ( 337, 120 )
            Beep ( 622, 120 )
            Beep (337, 120 )
            Beep ( 659, 120 )
            Beep (337, 120 )
            Beep ( 494 ,120  )
            Beep (337, 120)
            Beep ( 587, 120)
            Beep (337, 120)
            Beep ( 523, 120)
            Beep (337, 120)

            Beep ( 440, 120 )
            Beep (337, 140)
            Beep ( 262, 120 )
            Beep (337, 120)
            Beep ( 330, 120)
            Beep (337, 120)
            Beep ( 440, 120 )
            Beep (337, 120)

            Beep ( 494, 120)
            Beep (337, 140)
            Beep ( 330, 120 )
            Beep (337, 120)
            Beep ( 415, 120)
            Beep (337, 120)
            Beep ( 494, 120 )
            Beep (337, 120)

            Beep ( 523, 120  )
            Beep (337, 140)
            Beep ( 330, 120 )
            Beep (337, 120)
            Beep ( 659, 120 )
            Beep (337, 120)
            Beep ( 622, 120 )
            Beep (337, 120)

            Beep ( 659, 120 )
            Beep (337, 120)
            Beep ( 622, 120)
            Beep (337, 120)
            Beep ( 659, 120 )
            Beep (337, 120)
            Beep ( 494, 120 )
            Beep (337, 120)
            Beep ( 587, 120 )
            Beep (337, 120)
            Beep ( 523, 120 )
            Beep (337, 120)

            Beep ( 440, 120)
            Beep (337, 140)
            Beep ( 262, 120)
            Beep (337, 120)
            Beep ( 330, 120)
            Beep (337, 120)
            Beep ( 440, 120 )
            Beep (337, 120)

            Beep ( 494, 120)
            Beep (337, 140)
            Beep ( 330, 120)
            Beep (337, 120)
            Beep ( 523, 120 )
            Beep (337, 120)
            Beep ( 494, 120)
            Beep (337, 140)
            Beep ( 440, 120)
            
        def chebur(self):
            Beep(330, 200); Beep(439, 200); Beep(414, 200); Beep(439, 200);
            Beep(493, 200); Beep(439, 200); Beep(391, 200); Beep(439, 200);
            Beep(391, 400); Beep(349, 400); Beep(348, 600); Beep(32767, 200);

            Beep(293, 200); Beep(391, 200); Beep(369, 200); Beep(391, 200);
            Beep(439, 200); Beep(391, 200); Beep(293, 200); Beep(348, 200);
            Beep(329, 600); Beep(32767, 600);

            Beep(329, 200); Beep(439, 200); Beep(414, 200); Beep(439, 200);
            Beep(493, 200); Beep(439, 200); Beep(391, 200); Beep(348, 200);
            Beep(329, 400); Beep(293, 400); Beep(439, 600); Beep(32767, 200);

            Beep(329, 200); Beep(523, 200); Beep(493, 200); Beep(439, 200);
            Beep(414, 200); Beep(439, 200); Beep(493, 200); Beep(414, 200);
            Beep(439, 600); Beep(32767, 600); 
            
        def beep_xz(self):
            Beep(1000,500); Beep(500,500);  Beep(1000,500);     Beep(1500,500);
            Beep(2000,500); Beep(1500,500);   Beep(1000,500);    Beep(500,500);
            Beep(250,500);  Beep(500,500);  Beep(250,500);    Beep(500,200);
            
            Beep(750,200);  Beep(1000,200);    Beep(1250,200);  Beep(1500,200);
            Beep(1750,200);         Beep(2000,200);    Beep(2250,200); Beep(2500,200);
            Beep(2250,200);   Beep(2000,200);        Beep(1750,200);  Beep(1500,200);
            
            Beep(1250,200);  Beep(1000,200);   Beep(750,200);     Beep(500,200);
            Beep(250,200);     time.sleep(0.5);       Beep(250,500);      time.sleep(1.5);
            Beep(250,1000);
            
        def beep_tetris(self):
            Beep(1320,500);     Beep(990,250);      Beep(1056,250);     Beep(1188,250);
            Beep(1320,125);     Beep(1188,125);     Beep(1056,250);     Beep(990,250);
            Beep(880,500);      Beep(880,250);      Beep(1056,250);     Beep(1320,500);
            Beep(1188,250);     Beep(1056,250);     Beep(990,750);      Beep(1056,250);
            
            Beep(1188,500);
            Beep(1320,500);
            Beep(1056,500);
            Beep(880,500);
            Beep(880,500);
            time.sleep(0.5);
            Beep(1188,500);
            Beep(1408,250);
            Beep(1760,500);
            Beep(1584,250);
            Beep(1408,250);
            Beep(1320,750);
            Beep(1056,250);
            Beep(1320,500);
            Beep(1188,250);
            Beep(1056,250);
            Beep(990,500);
            Beep(990,250);
            Beep(1056,250);
            Beep(1188,500);
            Beep(1320,500);
            Beep(1056,500);
            Beep(880,500);
            Beep(880,500);
            time.sleep(1);
            Beep(1320,500);
            Beep(990,250);
            Beep(1056,250);
            Beep(1188,250);
            Beep(1320,125);
            Beep(1188,125);
            Beep(1056,250);
            Beep(990,250);
            Beep(880,500);
            Beep(880,250);
            Beep(1056,250);
            Beep(1320,500);
            Beep(1188,250);
            Beep(1056,250);
            Beep(990,750);
            Beep(1056,250);
            Beep(1188,500);
            Beep(1320,500);
            Beep(1056,500);
            Beep(880,500);
            Beep(880,500);
            time.sleep(0.5);
            Beep(1188,500);
            Beep(1408,250);
            Beep(1760,500);
            Beep(1584,250);
            Beep(1408,250);
            Beep(1320,750);
            Beep(1056,250);
            Beep(1320,500);
            Beep(1188,250);
            Beep(1056,250);
            Beep(990,500);
            Beep(990,250);
            Beep(1056,250);
            Beep(1188,500);
            Beep(1320,500);
            Beep(1056,500);
            Beep(880,500);
            Beep(880,500);
            time.sleep(1);
            Beep(660,1000);
            Beep(528,1000);
            Beep(594,1000);
            Beep(495,1000);
            Beep(528,1000);
            Beep(440,1000);
            Beep(419,1000);
            Beep(495,1000);
            Beep(660,1000);
            Beep(528,1000);
            Beep(594,1000);
            Beep(495,1000);
            Beep(528,500);
            Beep(660,500);
            Beep(880,1000);
            Beep(838,2000);
            Beep(660,1000);
            Beep(528,1000);
            Beep(594,1000);
            Beep(495,1000);
            Beep(528,1000);
            Beep(440,1000);
            Beep(419,1000);
            Beep(495,1000);
            Beep(660,1000);
            Beep(528,1000);
            Beep(594,1000);
            Beep(495,1000);
            Beep(528,500);
            Beep(660,500);
            Beep(880,1000);
            Beep(838,2000);
        # Ф-ция отрисовки в проги (Главная инициализация)
        def signals(self):

            self.connect(self.yolka, QtCore.SIGNAL('clicked()'),self.beep_yolka)
            self.connect(self.murka, QtCore.SIGNAL('clicked()'),self.beep_murka)
            self.connect(self.classic, QtCore.SIGNAL('clicked()'),self.beep_classic)
            self.connect(self.vagon, QtCore.SIGNAL('clicked()'),self.chebur)
            self.connect(self.xz, QtCore.SIGNAL('clicked()'),self.beep_xz)
            self.connect(self.tetris, QtCore.SIGNAL('clicked()'),self.beep_tetris)
            self.connect(self.exit, QtCore.SIGNAL('clicked()'),QtGui.qApp.quit)

            QtGui.qApp.processEvents()

        '''
        def mousePressEvent(self, event):
                if event.button() == QtCore.Qt.LeftButton:
                    self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
                    event.accept()

        def mouseMoveEvent(self, event):
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(event.globalPos() - self.dragPosition)
                    event.accept()
        '''
            
# Запускаем прогу и ставим стили для элементов некоторых
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    rendering = Program()
    rendering.setStyleSheet(
                            " QWidget  {"
                             "border: 1px solid #8f8f91;"
                             "border-radius: 4px;"
                             "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}"

                             "QLabel {"
                             "border: 2px solid darkkhaki; padding-left: 2px; padding-right: 2px;"
                             "border-radius: 4px;}"

                            "QPushButton:pressed {"
                            "padding-left: 5px;"
                            ""
                            "background-color: #d0d67c;}"
                          )

    rendering.show()
    sys.exit(app.exec_())

