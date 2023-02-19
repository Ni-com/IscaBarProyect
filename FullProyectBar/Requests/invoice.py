class Invoice:
    def __init__(self,id,ref,pay, vat,lines,client, total):
        self.__id = id
        self.__ref= ref
        self.__pay=pay
        self.__vat = vat
        self.__client = client
        self.__total=total
        self.__lines = lines
        
        
    
    def getId(self):
        return self.__id

    def getRef(self):
        return self.__ref
    
    def getClient(self):
        return self.__client
    
    def getVat(self):
        return self.__vat
    
    def getLines(self):
        return self.__lines

    def getPay(self):
        return self.__pay
    
    def getTotal(self):
        return self.__total
    

    