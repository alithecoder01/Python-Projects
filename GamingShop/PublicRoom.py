from GamingShop import GamingShop


class PublicRoom(GamingShop):
    pricePerHour =1.5
    def __init__(self, name, age, numPerson, numHour, deviceType):
        super().__init__(name, age, numPerson, numHour, deviceType)
    
    def CheckAge(self):
        if self.age <13 :
            return "Not Allowed"
        else:
            return "Allowed"
    
    def Discount(self):
        
        if self.numPerson >=5:
            return ((self.numPerson*self.numHour*self.pricePerHour)*0.1)
        else:
            return 0

    def TotalPrice(self):
        return ((self.numPerson*self.numHour*self.pricePerHour)- self.Discount())
    
    def toString(self):
         super().toString()
         print("Public Room")
         print("Age Validation: " + self.CheckAge())
         print("Price of the Room per hour: " + str(self.pricePerHour))
         print("Discount: " + str(self.Discount()))
         print("Total Price: " + str(self.TotalPrice()))
    