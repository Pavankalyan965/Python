def sum(marks):
    total = 0
    for x in marks:
        total += x;
    return total
subject_marks = sum((20, 30, 40, 50, 60, 70))
print(subject_marks)

additional_marks = 50
total_marks = subject_marks + additional_marks
print(total_marks)
