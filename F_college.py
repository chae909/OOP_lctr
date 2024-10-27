class Student:
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

class Department:
    def __init__(self, name, students):
        self.name = name
        self.students = students

class College:
    def __init__(self, college_name, departments):
        self.college_name = college_name
        self.departments = departments

    def get_total_students(self):
        num = 0
        for dept in self.departments:
            for stud in dept.students:
                num += 1
        return num


if __name__ == '__main__':
    s1 = Student("Mia", 1, "InfoStat")
    s2 = Student("Priya", 2, "InfoStat")
    s3 = Student("John", 1, "ComSci")
    s4 = Student("Rahul", 2, "ComSci")

    stat_students = [s1, s2]
    com_students = [s3, s4]

    info_stat = Department("InfoStat", stat_students)
    com_sci = Department("ComSci", com_students)

    departments = [info_stat, com_sci]
    college = College("CIS", departments)
    print(f'전체 학생수: {college.get_total_students()}')