from request import Request
from bar_application import getOrders
from bar_application import addOrder
from bar_application import deleteOrder
from bar_application import updateOrder
from bar_application import createInvoice
class ControllerRequest():
    def __init__(self):
        self.__request = {}
        self.box = 0

    def updateAllOrders(self):
        allOrders = getOrders("")
        for id in allOrders:
            if allOrders[id]["state"]=="D":
                name = allOrders[id]["name"]
                client=allOrders[id]["client"]
                if client==False:
                    client=""
                pax=allOrders[id]["pax"]
                waiter=allOrders[id]["waiter"]
                if waiter==False:
                    waiter=""
                aditionalData=allOrders[id]["aditionalData"]
                if aditionalData==False:
                    aditionalData=""
                register=allOrders[id]["register"]
                if register==False:
                    register=[]
                pay=allOrders[id]["pay"]
                newOrder = Request(name, client, pax, waiter,aditionalData,register,pay)
                self.__request[id] = newOrder
        return True
    
    def addRequest(self,name,client,pax,waiter,aditionalData):
        for id in self.__request:
            order=self.__request[id]
            if order.getTable()==name:
                return False
        post={
            
            "name":name,
            "client":client,
            "pax":pax,
            "waiter":waiter,
            "aditionalData":aditionalData
        }
        id=addOrder(post)
        if id == None:
            return False
        register=[]
        pay=0
        newOrder = Request(name, client, pax, waiter,aditionalData,register,pay)
        self.__request[id] = newOrder
        print("El id es: " + str(id))
        return True
    
    def setRequest(self,table,put):
        orderFind=0
        for id in self.__request:
            order=self.__request[id]
            if order.getTable()==table:
                orderFind=id
        if orderFind==0: 
            return False
        if updateOrder(orderFind,put):
            allOrders = getOrders(orderFind)
            name = allOrders[id]["name"]
            client=allOrders[id]["client"]
            pax=allOrders[id]["pax"]
            waiter=allOrders[id]["waiter"]
            aditionalData=allOrders[id]["aditionalData"]
            register=allOrders[id]["register"]
            if register==False:
                register=[]
            pay=allOrders[id]["pay"]
            newOrder = Request(name, client, pax, waiter,aditionalData,register,pay)
            self.__request[id] = newOrder
            return True
        return False

    def getRequests(self):
        orders=""
        if len(self.__request)==0:
            return None
        for id in self.__request:
            order=self.__request[id]
            orders+="Mesa "+str(order.getTable())+"\n"
        return orders


 
    def tablesAvaliable(self):
        tables=""
        for id in self.__request:
            order=self.__request[id]
            tables+="Mesa: " + str(order.getTable())+"\n"
        if tables =="":
            tables="Todos los numeros de mesas disponibles"
        return tables

    def getIdByTable(self,table):
        for id in self.__request:
            order=self.__request[id]
            if order.getTable()==table:
                return id
        return False
    def getRegisters(self,id):
        order=self.__request[id]
        return order.getRegister()
    
    def getPay(self,id):
        
        order=self.__request[id]
        return order.getPay()

    def updatePay(self,id,pay):
        order=self.__request[id]
        oldPay=order.getPay()
        order.setPay(pay+oldPay)
    
    def deleteOrder(self,id):
        if deleteOrder(id):
            order=self.__request[id]
            self.box+=order.getPay()
            del self.__request[id]
            return True
        else:
            return False
    def getOrderbyTable(self,table):
        for id in self.__request:
            order=self.__request[id]
            if order.getTable()==table:
                return order
    def getBox(self):
        return self.box

    
    def createInvoice(self,idOrder):
        if idOrder not in self.__request:
            return False
        order=self.__request[idOrder]
        if createInvoice(idOrder):
            self.box+=order.getPay()
            del self.__request[idOrder]
            return True
        return False