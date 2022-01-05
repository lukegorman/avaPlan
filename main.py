from PyQt5 import QtGui, QtWidgets, QtCore, uic
import sys


class SateEval:
        result = 0
        thirdPartyAssesment = 0 
        snowFall = 0
        wind = 0
        partySize = 0
        slopeIncline = 0
        timeOfDay = 0
        serrac = 0

        def Evaluate(self):
            self.result = (self.thirdPartyAssesment + self.snowFall +
                self.wind + self.partySize + self.slopeIncline
                + self.timeOfDay + self.serrac)
            return self.result/8


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('UI/plan.ui', self)
        # self.show()

        self.state = SateEval()

        self.pbEvaluate = self.findChild(
            QtWidgets.QPushButton, 'pbEvaluate') 
        self.pbEvaluate.clicked.connect(self.pbEvaluatePressed)

        self.slRisk = self.findChild(
            QtWidgets.QSlider, 'slRisk')
        self.slRisk.sliderReleased.connect(self.slRiskReleased)

        #self.slSnow = self.findChild(
        #    QtWidgets.QSlider, 'slSnow')
        #self.slSnow.sliderReleased.connect(self.sliderReleased)


        self.show()


    def pbEvaluatePressed(self):
        print('Risk: ', self.state.Evaluate())

    def slRiskReleased(self):
        self.state.thirdPartyAssesment = self.slRisk.value()
        print('printsliderReleased', self.slRisk.value())



    #def myFunction(self, identifier):
      #   combo = self.findChild(QtGui.QComboBox,identifier)
     #    index = combo.currentIndex()
       #  text = combo.currentText()
        # data = combo.currentData()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


# QQuickWindow.setSceneGraphBackend('software')
# app = QGuiApplication(sys.argv)
# engine = QQmlApplicationEngine()
# engine.quit.connect(app.quit)
# engine.load('./UI/main.qml')
# sys.exit(app.exec())
