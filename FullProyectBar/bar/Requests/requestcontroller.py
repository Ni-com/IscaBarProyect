from request import Request

class ControllerRequest():
    def __init__(self):
        self.__request = {}
        self.__box=0.00

    def addRequest(self,table,client,pax,waiter,extraInfo):
        if table in self.__request:
            return False

        newRequest= Request(table,client,pax,waiter,extraInfo)
        self.__request[table] = newRequest
        return True

    def getRequests(self):
        return self.__request

    def getRequest(self,table):
        return self.__request[table]

    def addOrder(self,table,id,product):
        if table not in self.__request:
            return False
        request=self.__request[table]
        request.addOrder(id,product)
        return True
    
    def setPay(self,table, price):
        request=self.__request[table]
        request.setPay(price)
        
    
    def getPay(self,table):
        request=self.__request[table]
        return request.getPay()

    def delOrder(self,table,id,product):
        if table not in self.__request:
            return False
        request=self.__request[table]
        request.delOrder(id,product)
        return True

    def delTable(self,table):
        if table not in self.__request:
            return False
        del self.__request[table]
        return True

    def getBox(self):
        return self.__box

    def addToBox(self,money):
        self.__box+=money
    