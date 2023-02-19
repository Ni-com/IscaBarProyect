class Request:
    def __init__(self,table, client, pax, waiter, extraInfo):
        self.__table = table
        self.__client = client
        self.__pax = pax
        self.__waiter = waiter
        self.__order={}
        self.__pay=0
        self.__extraInfo=extraInfo
    
    def getTable(self):
        return self.__table
    
    def getClient(self):
        return self.__client
    
    def getPax(self):
        return self.__pax
    
    def getWaiter(self):
        return self.__waiter
    
    def getOrder(self):
        return self.__order

    def getPay(self):
        return self.__pay
    
    def getExtraInfo(self):
        return self.__extraInfo
    

    
    def setTable(self,table):
        self.__table=table

    def setClient(self,client):
        self.__client=client

    def setPax(self,pax):
        self.__pax=pax

    def setWaiter(self,waiter):
        self.__waiter=waiter

    def setOrder(self,order):
        self.__order=order

    def setPay(self,pay):
        self.__pay+=pay
    
    def getSetExtraInfo(self, extraInfo):
        self.__extraInfo=extraInfo

    def addOrder(self, id, order):
        self.__order[id]=order

    def delOrder(self, id, order):
        del self.__order[id]