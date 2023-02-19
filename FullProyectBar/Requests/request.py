class Request:
    def __init__(self,table, client, pax, waiter, extraInfo,register, pay):
        self.__table = table
        self.__client = client
        self.__pax = pax
        self.__waiter = waiter
        self.__register=register
        self.__extraInfo=extraInfo
        self.__pay=pay
    
    def getTable(self):
        return self.__table
    
    def getClient(self):
        return self.__client
    
    def getPax(self):
        return self.__pax
    
    def getWaiter(self):
        return self.__waiter
    
    def getRegister(self):
        return self.__register

    def getPay(self):
        return self.__pay
    
    def getExtraInfo(self):
        return self.__extraInfo
    
    def setPay(self,pay):
        self.__pay=pay
   
    
  

    