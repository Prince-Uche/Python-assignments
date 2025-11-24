student_number = 15

pass_mark = 45

passes = 0

failures = 0

for inputs in range (student_number):
    inputs = int(input("Enter score of student: "))
    if inputs >= pass_mark:
        passes += 1
    if inputs < pass_mark:
        failures += 1
        
print(passes, "Students passed")
print(failures, "Students failed")

