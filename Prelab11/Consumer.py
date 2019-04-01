
#######################################################
#   Author:     <Your Full Name>
#   email:      <Your Email>
#   ID:         <Your course ID, e.g. ee364j20>
#   Date:       <Start Date>
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from Prelab11.BasicUI import *
import re

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.box = [self.txtStudentName,       self.txtStudentID,
                      self.txtComponentCount_1,  self.txtComponentCount_2,  self.txtComponentCount_3,  self.txtComponentCount_4,   self.txtComponentCount_5,
                      self.txtComponentCount_6,  self.txtComponentCount_7,  self.txtComponentCount_8,  self.txtComponentCount_9,   self.txtComponentCount_10,
                      self.txtComponentCount_11, self.txtComponentCount_12, self.txtComponentCount_13, self.txtComponentCount_14,  self.txtComponentCount_15,
                      self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18, self.txtComponentCount_19,  self.txtComponentCount_20,
                      self.txtComponentName_1,   self.txtComponentName_2,   self.txtComponentName_3,   self.txtComponentName_4,    self.txtComponentName_5,
                      self.txtComponentName_6,   self.txtComponentName_7,   self.txtComponentName_8,   self.txtComponentName_9,    self.txtComponentName_10,
                      self.txtComponentName_11,  self.txtComponentName_12,  self.txtComponentName_13,  self.txtComponentName_14,   self.txtComponentName_15,
                      self.txtComponentName_16,  self.txtComponentName_17,  self.txtComponentName_18,  self.txtComponentName_19,   self.txtComponentName_20,
                      ]
        self.btnSave.setDisabled(True)
        self.btnLoad.setEnabled(True)
        for elements in self.box:
            elements.textChanged.connect(self.check)
        self.chkGraduate.stateChanged.connect(self.check)
        self.cboCollege.currentTextChanged.connect(self.check)
        self.btnClear.clicked.connect(self.reset)
        self.btnSave.clicked.connect(self.savefile)
        self.btnLoad.clicked.connect(self.loadData)
    def check(self):

                self.btnSave.setEnabled(True)
                self.btnLoad.setDisabled(True)

    def savefile(self):
        #if self.chkGraduate.isChecked():
        #    x.append('<StudentName graduate="[true]">[{foo}]</StudentName>'.format(foo=self.txtStudentName))
        #else:
        #    x.append('<StudentName graduate="[false]">[{foo}]</StudentName>'.format(foo=self.txtStudentName))
        x=[]
        x.append('<?xml version="1.0" encoding="UTF-8"?>\n')
        x.append('<Content>\n')
        if self.chkGraduate.isChecked():
            x.append('    <StudentName graduate="{}">{}</StudentName>\n'.format('true',self.txtStudentName.text()))
        else:
            x.append('    <StudentName graduate="{}">{}</StudentName>\n'.format('false',self.txtStudentName.text()))
        x.append('    <StudentID>{}</StudentID>\n'.format(self.txtStudentID.text()))
        x.append('    <College>{}</College>\n'.format(self.cboCollege.currentText()))
        x.append('    <Components>\n')
        index=2
        for elements in self.box[2:22]:
            if elements.text() != '':
                x.append('        <Component name="{}" count="{}" />\n'.format(self.box[20+index].text(),elements.text()))
            index += 1
        x.append('    </Components>')
        x.append('</Content>')
        f=open("target.xml", "w")
        f.writelines(x)
    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        f=open(filePath,'r')
            #print(lines)
        i = 0

        for line1 in f:
            match0 = re.search('[g][r][a][d][u][a][t][e][=]["](?P<True>(?:[t][r][u][e]|[f][a][l][s][e]))["][>](?P<Name>[a-zA-Z0-9- \t]+)[<][/][S][t][u][d][e][n][t][N][a][m][e][>]',line1)
            print(match0)
            if match0 != None:
                print(match0["Name"],match0["True"])
                self.box[0].setText(match0["Name"])
                if match0["True"] == 'true':
                    self.chkGraduate.setChecked(True)
        f1=open(filePath,'r')
        for line in f1:
                #print(line)
            if i > 19:
                line=''
            match = re.search('[<][C][o][m][p][o][n][e][n][t][ ][n][a][m][e][=]["](?P<Last>[a-zA-Z0-9- \t]+)["][ \t][count]+[=]["](?P<First>[0-9]+)["][ \t][/][>]',line)
                #print(match)

            if match != None:
                self.box[2+i].setText(match["First"])
                self.box[22 + i].setText(match["Last"])
                i += 1
        f2 = open(filePath, 'r')
        #'    <StudentID>14712-45699</StudentID>'
        for line in f2:
            match=re.search('[<][S][t][u][d][e][n][t][I][D][>](?P<Last>[0-9-]{11})[<][/][S][t][u][d][e][n][t][I][D][>]',line)
            if match != None:
                self.txtStudentID.setText(match["Last"])
        '    <College>Industrial Engineering</College>'
        f3 = open(filePath, 'r')
        for line in f3:
            match=re.search('[<][C][o][l][l][e][g][e][>](?P<Last>[a-zA-z]+[ ][E][n][g][i][n][e][e][r][i][n][g])[<][/][C][o][l][l][e][g][e][>]',line)
            if match != None:
                self.cboCollege.setCurrentIndex(self.cboCollege.findText(match["Last"]))

        #'<StudentName graduate="true">Nicole Jackson</StudentName>'

    def reset(self):
        everything = [self.txtStudentName,       self.txtStudentID,
                      self.txtComponentCount_1,  self.txtComponentCount_2,  self.txtComponentCount_3,  self.txtComponentCount_4,   self.txtComponentCount_5,
                      self.txtComponentCount_6,  self.txtComponentCount_7,  self.txtComponentCount_8,  self.txtComponentCount_9,   self.txtComponentCount_10,
                      self.txtComponentCount_11, self.txtComponentCount_12, self.txtComponentCount_13, self.txtComponentCount_14,  self.txtComponentCount_15,
                      self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18, self.txtComponentCount_19,  self.txtComponentCount_20,
                      self.txtComponentName_1,   self.txtComponentName_2,   self.txtComponentName_3,   self.txtComponentName_4,    self.txtComponentName_5,
                      self.txtComponentName_6,   self.txtComponentName_7,   self.txtComponentName_8,   self.txtComponentName_9,    self.txtComponentName_10,
                      self.txtComponentName_11,  self.txtComponentName_12,  self.txtComponentName_13,  self.txtComponentName_14,   self.txtComponentName_15,
                      self.txtComponentName_16,  self.txtComponentName_17,  self.txtComponentName_18,  self.txtComponentName_19,   self.txtComponentName_20,
                      ]
        for element in everything:
            element.setText('')
        self.chkGraduate.setChecked(False)
        self.cboCollege.setCurrentIndex(0)
        self.btnSave.setDisabled(True)
        self.btnLoad.setEnabled(True)
        #self.cboCollege.setCurrentIndex(items.keys(),0)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
