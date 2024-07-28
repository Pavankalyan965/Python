student = {"name":"Pavan",
           "Course":"Data Science"}

getStudentInfo = input("What info do you want?")

try:
    print(f"The value for your request is {student[getStudentInfo]}")
except KeyError:
    print(f"There is no value with the {getStudentInfo}")