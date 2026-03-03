class Student:
    # default constructor
    collage_name = "ITS Collage"#class attr
    def __init__(self):
        pass
    def __init__(self,name,marks):
        self.name = name#Obbecjt attr
        self.marks = marks
        print("adding new student in database")
st1 = Student("iInzamam",95)
print(st1.name,st1.marks,st1.collage_name)
st2 = Student("Rahul",74.64)
print(st2.name,st2.marks,st1.collage_name)
