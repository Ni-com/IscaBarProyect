from invoice import Invoice
from bar_application import getInvoice
from bar_application import addInvoice
from bar_application import deleteInvoice
from bar_application import updateInvoice

class ControllerInvoice():
    def __init__(self):
        self.__invoice = {}
        self.box = 0

    def updateAllInvoices(self):
        allInvoices = getInvoice("")
        for id in allInvoices:
                ref = allInvoices[id]["name"]
                pay = allInvoices[id]["pay"]
                vat=allInvoices[id]["vat"]
                lines=allInvoices[id]["lines"]
                if lines==False:
                    lines=[]
                client=allInvoices[id]["client"]
                if client==False:
                    client=""
                total=allInvoices[id]["total"]
                newInvoice = Invoice(id,ref,pay, vat,lines,client, total)
                self.__invoice[id] = newInvoice
        return True
    
    def addInvoice(self,client):
        
        post={
            "client":client,
        }

        id=addInvoice(post)
        if id == None:
            return False
        newInvoice = Invoice(id,id,0, 21,[],client, 0)
        self.__invoice[id] = newInvoice
        return id

    def getInvoice(self,id):
        if id not in self.__invoice:
            return False
        invoice=self.__invoice[id]
        return invoice