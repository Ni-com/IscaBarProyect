class InvoiceLines:
    def __init__(self,id,quantity, invoice, product):
        self.__id = id
        self.__quantity = quantity
        self.__invoice = invoice
        self.__product = product
        
    
    def getId(self):
        return self.__id
    
    def getQuantity(self):
        return self.__quantity
    
    def getOrder(self):
        return self.__invoice
    
    def getProduct(self):
        return self.__product
    
    