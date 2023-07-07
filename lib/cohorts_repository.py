from lib.cohort import Cohort
from lib.student import Student

class CohortsRepository():
    def __init__(self, connection):
        self.connection = connection

    def find_cohort_with_students(self,id):
        rows = self.connection.execute("SELECT * FROM cohorts JOIN students ON students.cohort_id = cohorts.id WHERE students.cohorts.id = %s",[id])
        
        students = []
        for row in rows:
            student = Student(row["id"], row["name"], row["cohort_id"])
            students.append(student)
        cohort = Cohort(rows[0]["cohorts_id"], rows[0]["name"], rows[0]["starting_date"],students)
        return cohort