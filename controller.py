from PyQt6.QtWidgets import  *
from PyQt6.QtCore import *
from grader import *
import pandas as pd

Grades = {'name': [],'id': [], 'grade': [], 'letter_grade': []}

class MissinStudentInfo(Exception):
    pass
class IncorrectStudentIDLen(Exception):
    pass
class NegativeGrade(Exception):
    pass
class DublicateID(Exception):
    pass
class MissingAssignmentName(Exception):
    pass

class controller(QMainWindow, Ui_Grader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.curve.setChecked(False)
        self.Export.clicked.connect(lambda: self.export())
        self.Add_grade.clicked.connect(lambda: self.add_grade())

    def add_grade(self):
        try:
            int(self.student_id.text())
            int(self.student_grade.text())
            
            if self.student_grade.text() == '' or self.student_id.text() == '' or self.Student_name.text() == '':
                raise MissinStudentInfo('Student name, grade or id missing')
            if len(self.student_id.text()) != 5:
                raise IncorrectStudentIDLen('ID must be 5 digits')
            if int(self.student_grade.text()) < 0:
                raise NegativeGrade('Can not have negative grade') 
            if str(self.student_id.text()) in Grades['id']:
                raise DublicateID('ID already in use')

        except (MissinStudentInfo, IncorrectStudentIDLen, NegativeGrade,DublicateID) as a:
            self.error_label.setText(str(a))
        except ValueError:
            self.error_label.setText("Non-numeric input")  
        else:
            Grades['name'].append(self.Student_name.text().lower()) 
            Grades['grade'].append(int(self.student_grade.text()))
            Grades['id'].append(str(self.student_id.text()))
            self.Student_name.setText('')
            self.student_grade.setText('')
            self.student_id.setText('')
            self.error_label.setText('')
   
    def export(self):
        try:
            if self.assignment_name.text() == '':
                raise MissingAssignmentName('Assignment has no name')
            Max_grade = max(Grades['grade'])
        except MissingAssignmentName as a:
            self.error_label.setText('No Assignment name was entered')
        except ValueError:
            self.error_label.setText('No data has been entered')
        else:
            if self.curve.isChecked() == False:
                for x in range(len(Grades['grade'])):
                    if Grades['grade'][x] >= 100 - 10:
                        Grades['letter_grade'].append('A')
                    elif Grades['grade'][x] >= 100 - 20:
                        Grades['letter_grade'].append('B')
                    elif Grades['grade'][x] >= 100 - 30:
                        Grades['letter_grade'].append('C')
                    elif Grades['grade'][x] >= 100 - 40:
                        Grades['letter_grade'].append('D')
                    else:
                        Grades['letter_grade'].append('F')
            else:
                for x in range(len(Grades['grade'])):
                    if Grades['grade'][x] >= Max_grade - (Max_grade * .10):
                        Grades['letter_grade'].append('A')
                    elif Grades['grade'][x] >= Max_grade - (Max_grade * .20):
                        Grades['letter_grade'].append('B')
                    elif Grades['grade'][x] >= Max_grade - (Max_grade * .30):
                        Grades['letter_grade'].append('C')
                    elif Grades['grade'][x] >= Max_grade - (Max_grade * .40):
                        Grades['letter_grade'].append('D')
                    else:
                        Grades['letter_grade'].append('F')
                self.curve.setChecked(False)

            for x in range(len(Grades['id'])):
                Grades['id'][x] = '"' + Grades['id'][x] + '"'
            df = pd.DataFrame(Grades)
 
            df.to_csv(self.assignment_name.text()+'.csv', sep='\t', index=False,)

            Grades['grade'].clear()
            Grades['grade'].clear()
            Grades['id'].clear()
            Grades['letter_grade'].clear()
            Grades['name'].clear()
            self.assignment_name.setText('')
            self.error_label.setText('')
        