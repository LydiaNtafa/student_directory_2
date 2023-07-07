class Cohort:
    def __init__(self, id, name, staring_date, students = []):
        self.id = id
        self.cohort_name = name
        self.starting_date = staring_date
        self.students = students

    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Cohort({self.id}, {self.cohort_name}, {self.starting_date}, {self.students})"