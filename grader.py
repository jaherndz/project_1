# Form implementation generated from reading ui file 'Grader.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Grader(object):
    def setupUi(self, Grader):
        Grader.setObjectName("Grader")
        Grader.resize(298, 375)
        Grader.setMinimumSize(QtCore.QSize(298, 375))
        Grader.setMaximumSize(QtCore.QSize(298, 375))
        self.assignment_name = QtWidgets.QLineEdit(parent=Grader)
        self.assignment_name.setGeometry(QtCore.QRect(90, 30, 113, 21))
        self.assignment_name.setText("")
        self.assignment_name.setObjectName("assignment_name")
        self.Student_name = QtWidgets.QLineEdit(parent=Grader)
        self.Student_name.setGeometry(QtCore.QRect(90, 70, 113, 21))
        self.Student_name.setObjectName("Student_name")
        self.student_id = QtWidgets.QLineEdit(parent=Grader)
        self.student_id.setGeometry(QtCore.QRect(90, 110, 113, 21))
        self.student_id.setObjectName("student_id")
        self.Export = QtWidgets.QPushButton(parent=Grader)
        self.Export.setGeometry(QtCore.QRect(30, 210, 100, 32))
        self.Export.setObjectName("Export")
        self.Assign_Label = QtWidgets.QLabel(parent=Grader)
        self.Assign_Label.setGeometry(QtCore.QRect(100, 10, 111, 16))
        self.Assign_Label.setMaximumSize(QtCore.QSize(16777215, 300))
        self.Assign_Label.setObjectName("Assign_Label")
        self.Stu_Name_label = QtWidgets.QLabel(parent=Grader)
        self.Stu_Name_label.setGeometry(QtCore.QRect(100, 50, 111, 16))
        self.Stu_Name_label.setObjectName("Stu_Name_label")
        self.Grade_label = QtWidgets.QLabel(parent=Grader)
        self.Grade_label.setGeometry(QtCore.QRect(100, 130, 111, 16))
        self.Grade_label.setObjectName("Grade_label")
        self.curve = QtWidgets.QCheckBox(parent=Grader)
        self.curve.setGeometry(QtCore.QRect(90, 180, 141, 20))
        self.curve.setObjectName("curve")
        self.Add_grade = QtWidgets.QPushButton(parent=Grader)
        self.Add_grade.setGeometry(QtCore.QRect(160, 210, 100, 32))
        self.Add_grade.setObjectName("Add_grade")
        self.id_label = QtWidgets.QLabel(parent=Grader)
        self.id_label.setGeometry(QtCore.QRect(100, 90, 111, 16))
        self.id_label.setObjectName("id_label")
        self.student_grade = QtWidgets.QLineEdit(parent=Grader)
        self.student_grade.setGeometry(QtCore.QRect(90, 150, 113, 21))
        self.student_grade.setObjectName("student_grade")
        self.error_label = QtWidgets.QLabel(parent=Grader)
        self.error_label.setGeometry(QtCore.QRect(30, 250, 241, 111))
        self.error_label.setMaximumSize(QtCore.QSize(16777215, 300))
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Grader)
        QtCore.QMetaObject.connectSlotsByName(Grader)

    def retranslateUi(self, Grader):
        _translate = QtCore.QCoreApplication.translate
        Grader.setWindowTitle(_translate("Grader", "Dialog"))
        self.Export.setText(_translate("Grader", "Export"))
        self.Assign_Label.setText(_translate("Grader", "Assignment Name"))
        self.Stu_Name_label.setText(_translate("Grader", "Student Name"))
        self.Grade_label.setText(_translate("Grader", "Student Grade"))
        self.curve.setText(_translate("Grader", "Apply curve"))
        self.Add_grade.setText(_translate("Grader", "Add Grade"))
        self.id_label.setText(_translate("Grader", "Student ID"))
