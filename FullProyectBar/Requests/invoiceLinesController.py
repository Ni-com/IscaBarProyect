from invoiceLines import InvoiceLines
from bar_application import getInvoiceLine
from bar_application import addInvoiceLine
from bar_application import deleteInvoiceLine
from bar_application import updateInvoiceLine

class ControllerInvoiceLines():
    def __init__(self):
        self.__lines = {}

    
    def updateAllLines(self):
        allInvoiceLines = getInvoiceLine("")
        for id in allInvoiceLines:
                quantity = allInvoiceLines[id]["quantity"]
                if (allInvoiceLines[id]["invoice"]== False or []) or (allInvoiceLines[id]["product"]== False or []):
                    deleteInvoiceLine(id)
                else:
                    invoice=allInvoiceLines[id]["invoice"][0]
                    product=allInvoiceLines[id]["product"][0]

                    newRegister = InvoiceLines(id, quantity, invoice, product)
                    self.__lines[id] = newRegister
        return True
    
    def addLine(self,quantity,invoice,product):
        
        post={
            "quantity":quantity,
            "invoice":invoice,
            "product":product,
        }

        id=addInvoiceLine(post)
        if id == None:
            return False
        newLine = InvoiceLines(id, quantity, invoice, product)
        self.__lines[id] = newLine
        return True
    
    def getLine(self,id):
        if id not in self.__lines:
            return False
        line=self.__lines[id]
        return line