student_number = int(input("please enter the student number : "))
tutorial_mark = float(input("please enter the student's  tutorial mark : "))
test_mark = float(input("please enter the student's test mark : "))
if (tutorial_mark + test_mark) / 2 < 40:
    grade = "F"
else:
    exam_mark = float(input("please enter the student's exam mark : "))
    mark = (tutorial_mark + test_mark +2 * exam_mark) / 4
    if 80 <= mark <= 100:
        grade = "A"
    elif 70 <= mark < 80:
        grade = "B"
    elif 60 <= mark < 70:
        grade = "C"
    elif 50 <= mark < 60:
        grade = "D"
    else:
        grade = "F"

print("%s's grade is %s."%(student_number,grade))
