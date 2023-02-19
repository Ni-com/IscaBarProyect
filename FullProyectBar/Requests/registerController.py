from register import Register
from bar_application import getRegisters
from bar_application import addRegister
from bar_application import deleteRegister
from bar_application import updateRegister

class ControllerRegister():
    def __init__(self):
        self.__registers = {}

    
    def updateAllRegister(self):
        allRegisters = getRegisters("")
        for id in allRegisters:
                quantity = allRegisters[id]["quantity"]
                if (allRegisters[id]["order"]== False or []) or (allRegisters[id]["product"]== False or []):
                    deleteRegister(id)
                else:
                    order=allRegisters[id]["order"][0]
                    product=allRegisters[id]["product"][1]

                    newRegister = Register(id, quantity, order, product)
                    self.__registers[id] = newRegister
        return True
    
    def addRegister(self,quantity,order,product):
        
        post={
            "quantity":quantity,
            "order":order,
            "product":product,
        }

        id=addRegister(post)
        if id == None:
            return False
        newRegister = Register(id, quantity, order, product)
        self.__registers[id] = newRegister
        print("El id es: " + str(id))
        return True
    
    def getInfo(self,id):
        info=""
        register=self.__registers[id]
        info="Registro: " + str(id)+" - Producto: " + str(register.getProduct()) + " - " + " Cantidad: " + str(register.getQuantity())
        return info

    def deleteRegister(self,order,id):
        if id not in self.__registers:
            return False
        register=self.__registers[id]
        if order!=register.getOrder():
            return False
        if deleteRegister(id):
            return True

    def findRegister(self,order,id):
        if id not in self.__registers:
            return False
        register=self.__registers[id]
        if order!=register.getOrder():
            return False
        return register