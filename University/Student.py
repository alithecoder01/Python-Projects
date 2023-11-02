class Student:
    def __init__(self,name,id,major,gpa):
        self.name = name 
        self.id = id
        self.major = major
        self.gpa = gpa
        
    

    def onHonor(self):
        if self.gpa> 3.0:
            return True
        else:
            return False
    

    def haveDiscount(self):
        if self.gpa>3.5:
            print("Have a discount of %30")
        elif self.gpa>=3.0 and self.gpa<3.5:
            print("Have a discount of %25")
    

    def gpaValid (self):
        if self.gpa >=2.0 :
            print("Student can continue")
        else:
            print("Give a Warning")