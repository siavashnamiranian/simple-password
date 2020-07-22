#simple password
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(137, 153, 131, 41))
        self.textEdit.setObjectName("textEdit")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(137, 81, 49, 18))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(137, 105, 62, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(137, 129, 45, 18))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(51, 153, 80, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.label.passw) #when button clicked run passw function.how get textedit and radiobutton?
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "generate password"))
        self.radioButton.setText(_translate("Dialog", "weak"))
        self.radioButton_2.setText(_translate("Dialog", "medium"))
        self.radioButton_3.setText(_translate("Dialog", "hard"))
        self.label.setText(_translate("Dialog", "password lenght"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


def passw(pass_lenght,strenght):
    weak = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    medium = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s','t','u','v',
              'w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    strong = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s','t','u','v',
              'w','x','y','z','1','2','3','4','5','6','7','8',
              '9','0','/','#','-','_','%','&','@','$']
    if strenght=="weak":
        p =  "".join(random.sample(weak,pass_lenght ))
        return p
    elif strenght=="average":
        pass_lenght_average=pass_lenght
        p =  "".join(random.sample(medium,pass_lenght_average))
        return p
    elif strenght=="hard":
        pass_lenght_hard=pass_lenght
        p =  "".join(random.sample(strong,pass_lenght_hard))
        return p
    else:
        print(" wrong_input ")
        
