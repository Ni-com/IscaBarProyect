class Register:
    def __init__(self,id,quantity, order, product):
        self.__id = id
        self.__quantity = quantity
        self.__order = order
        self.__product = product
        
    
    def getId(self):
        return self.__id
    
    def getQuantity(self):
        return self.__quantity
    
    def getOrder(self):
        return self.__order
    
    def getProduct(self):
        return self.__product
    
    