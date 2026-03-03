class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("Hello Everyone")
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is:- ", sum/3)
st2 =Student("Tony Stark", [97,85,79])
st2.get_avg()
st2.name = "ironman"
st2.get_avg()
st2.hello()