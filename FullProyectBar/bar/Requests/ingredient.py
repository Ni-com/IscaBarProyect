class Ingredient:
    
    def __init__(self,id, name, nutritionalValue, allergies, products):
        self.__name = name
        self.__nutritionalValue = nutritionalValue
        self.__allergies = allergies
        self.__products=products
        self.__id=id

    def getName(self):
        return self.__name
    
    def getNutritionalValue(self):
        return self.__nutritionalValue
    
    def getAllergies(self):
        return self.__allergies
    
    def getProducts(self):
        return self.__products

    def getId(self):
        return self.__id



    def setName(self, name):
        self.__name = name
    
    def setNutritionalValue(self, nutritionalValue):
        self.__nutritionalValue = nutritionalValue
    
    def setAllergies(self, allergies):
        self.__allergies = allergies

    def setAllergies(self, products):
        self.__products=products
