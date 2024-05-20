class Fruit():
    def __init__(self,color,taste,shape):
        self.color=color
        self.taste=taste
        self.shape=shape
        
    def get_taste(self):
        return self.taste


    def set_taste(self,new_taste):
        self.taste=new_taste

    def showDetails(self):
        print("HELLO! I am a fruit with {} color,{} shape,{} taste".format(self.color,self.shape,self.taste))


apple=Fruit("red","sour","round")
print("OLD TASTE : ",apple.get_taste())
apple.set_taste("sweet")


print("NEW TASTE: ",apple.get_taste())

apple.showDetails()


orange=Fruit("orange","sphere","sweet and sour")

print("OLD TASTE : ",orange.get_taste())
orange.set_taste("sweet")
print("NEW  TASTE: ",orange.get_taste())

orange.showDetails()
