
class GamingShop :
    def __init__(self,name,age,numPerson,numHour,deviceType) :
        self.name = name
        self.age = age
        self.numPerson = numPerson
        self.numHour = numHour
        self.deviceType= deviceType

    
    def Discount(self):
        pass

    
    def CheckAge(self):
        pass


    def TotalPrice(self):
        return str((self.numHour*self.numPerson)- self.Discount())
    

    def toString(self):
        print("RECIPT")
        print("Recipt name: "+ self.name)
        print("Age: "+ str(self.age))
        print("Type of device: " +str(self.deviceType))
    



        
    

    


        