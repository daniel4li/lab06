class Apartment:
    quality = {
        "bad" : 0,
        "average" : 1,
        "excellent" : 2
    }
    def __init__(self, rent = 0, metersFromUCSB = 0, condition = "N/A"):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self): 
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return "(Apartment) Rent: $" + str(self.getRent()) + ", Distance From UCSB: " + str(self.getMetersFromUCSB()) + "m, Condition: " + self.getCondition()
   
    

    def __lt__(self, other):
       if self.getRent() == other.getRent():
           if self.getMetersFromUCSB() == other.getMetersFromUCSB():
               if self.getCondition() in Apartment.quality.keys() and other.getCondition() in Apartment.quality.keys():
                   return Apartment.quality[self.getCondition()] > Apartment.quality[other.getCondition()]
               return False 
           else:
               return self.getMetersFromUCSB() < other.getMetersFromUCSB()
       else:
           return self.getRent() < other.getRent() 
       


    def __eq__(self, other):
        return (self.getRent() == other.getRent()) and (self.getCondition() == other.getCondition()) and (self.getMetersFromUCSB() == other.getMetersFromUCSB())

    def __gt__(self, other):
       if (self.__eq__(other) or self.__lt__(other)) :
           return False
       return True
           
        
