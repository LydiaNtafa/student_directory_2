class Cohort:
    def __init__(self, id, name, staring_date, students = None):
        self.id = id
        self.name = name
        self.starting_date = staring_date
        self.students = students or []

    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Cohort({self.id}, {self.name}, {self.starting_date})"