class Product:
    def __init__(self,id,name,price,stock,category,ingredients,description):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__category = category
        self.__ingredients = ingredients
        self.__description=description

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getStock(self):
        return self.__stock

    def getCategory(self):
        return self.__category
    
    def getIngredients(self):
        return self.__ingredients
    
    def getDescription(self):
        return self.__description
    def getProduct(self):
        return self


    def setId(self,id):
        self.__id=id

    def setName(self,name):
        self.__name=name
    
    def setPrice(self,price):
        self.__price=price
    
    def setStock(self,stock):
        self.__stock=stock
    
    def setCategory(self,category):
        self.__category=category
    
    def setIngredients(self,ingredients):
        self.__ingredients=ingredients
    
    def setDescription(self,description):
        self.__description=description
    
    def setProduct(self,id,name,price,stock,category,ingredients):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__category = category
        self.__ingredients = ingredients
    


    

   
