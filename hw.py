class Student():
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade
        
    def getGrade(self):
        return self.grade


    def setGrade(self,newGrade):
        self.grade=newGrade

    def showDetails(self):
        print("HELLO! I am {} ,my id is {} ,I study in grade {}".format(self.name,self.id,self.grade))

anu=Student(4182,"anu",6)
print("old grade :",anu.getGrade())
anu.setGrade(7)
anu.showDetails()