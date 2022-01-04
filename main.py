from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('UI/plan.ui', self)
        #self.show()

        self.button = self.findChild(
            QtWidgets.QPushButton, 'pbEvaluate')  # Find the button
        # Remember to pass the definition/method, not the return value!
        self.button.clicked.connect(self.printButtonPressed)
        

        self.show()

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


# QQuickWindow.setSceneGraphBackend('software')
#app = QGuiApplication(sys.argv)
#engine = QQmlApplicationEngine()
# engine.quit.connect(app.quit)
# engine.load('./UI/main.qml')
# sys.exit(app.exec())
