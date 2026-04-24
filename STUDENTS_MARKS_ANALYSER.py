#ADVANCED PYTHON I.COMPREHENSION
#MINI PROJECT ON STUDENTS MARKS ANALYSER USING COMPREHENSION
Students = {
    'SMITH':82,
    'SCOTT':67,
    'MARTIN':39,
    'ALLEN':91,
    'FORD':45,
    'MILLER':28,
    'VIRAT':76
}

#DICTIONARY COMPREHENSION FOR RESULT(PASS/FAIL)
result={
    name:('Pass' if marks >= 40 else 'Fail')
    for name,marks in Students.items()
}

#DICTIONARY COMPREHENSION FOR GRADES
grades={
    name:(
        'A' if marks >= 75 else
        'B' if marks >= 60 else
        'C' if marks >= 40 else
        'F' 
    )
    for name,marks in Students.items()
}

# #LIST OF PASSED STUDENTS
passed_students = [name for name, status in result.items() if status == 'Pass']

# #LIST OF FAILED STUDENTS
failed_students = [name for name, status in result.items() if status == 'Fail']

#BONUS LIST FOR TOPPERS
toppers = [name for name,marks in Students.items() if marks >= 75]

#DISPLAY OUTPUT
print(f'RESULT: {result}')
print(f'GRADES: {grades}')
print(f'PASSED STUDENTS: {passed_students}')
print(f'FAILED STUDENTS: {failed_students}')
print(f'TOPPERS(BONUS LIST): {toppers}')





