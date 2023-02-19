import requests

#Product##########################
def getProduct(id):
    url = "http://localhost:8069/bar/getProduct/"+str(id)
    response = requests.request("GET", url)

    if (response.status_code == 200):
        jsonResult = response.json()
        allProducts={}
        for product in jsonResult["data"]:
            allProducts[product["id"]]={
                "name":product["name"],
                "description":product["description"],
                "price":product["price"],
                "stock":product["stock"],
                "description":product["description"],
                "category":product["category"],
                "ingredients":product["ingredients"]

            }

        return allProducts

def addProduct(post):
    url = "http://localhost:8069/bar/addProduct"


    response = requests.post(url, json=post)

    if response.status_code == 200:
        
        id = response.json()["result"]["id"]
        return id
    else:
        
        return None

def updateProduct(id,post):
    url = "http://localhost:8069/bar/updateProduct/"+str(id)

   

    response = requests.put(url, json=post)

    if response.status_code == 200:
        return True
    else:
        return False

def deleteProduct(id):
    url = "http://localhost:8069/bar/deleteProduct"

    response = requests.delete(url, json={"id": id})

    if response.status_code == 200:
        return True
    else:
        return False
#Category##########################
def getCategory(id):
    url = "http://localhost:8069/bar/getCategory/"+str(id)

    response = requests.request("GET", url)

    if (response.status_code == 200):
        jsonResult = response.json()
        allCategories={}
        for category in jsonResult["data"]:
            allCategories[category["id"]]={
            "name":category["name"],
            "description":category["description"],
            "products":category["products"],
            "parent_id":category["parent_id"],
            "complete_name":category["complete_name"]
            }
        return allCategories

def addCategory(post):
    url = "http://localhost:8069/bar/addCategory"


    response = requests.post(url, json=post)

    if response.status_code == 200:
        
        id = response.json()["result"]["id"]
        return id
    else:
        
        return None

def updateCategory(id,post):
    url = "http://localhost:8069/bar/updateCategory/"+str(id)
    response = requests.put(url, json=post)

    if response.status_code == 200:
        return True
    else:
        return False

def deleteCategory(id):
    url = "http://localhost:8069/bar/deleteCategory"

    response = requests.delete(url, json={"id": id})

    if response.status_code == 200:
        return True
    else:
        return False

#Ingredient##########################
def getIngredients(id):
    url = "http://localhost:8069/bar/getIngredient/"+str(id)

    response = requests.request("GET", url)

    if (response.status_code == 200):
        jsonResult = response.json()
        allIngredients={}
        for ingredient in jsonResult["data"]:
            allIngredients[ingredient["id"]]={
                "name":ingredient["name"],
                "allergies":ingredient["allergies"],
                "nutritionalValue":ingredient["nutritionalValue"],
                "products":ingredient["products"]
            }
        return allIngredients

def addIngredient(post):
    url = "http://localhost:8069/bar/addIngredient"


    response = requests.post(url, json=post)

    if response.status_code == 200:
        
        id = response.json()["result"]["id"]
        return id
    else:
        
        return None

def updateIngredient(id,post):
    url = "http://localhost:8069/bar/updateIngredient/"+str(id)
    response = requests.put(url, json=post)

    if response.status_code == 200:
        return True
    else:
        return False

def deleteIngredient(id):
    url = "http://localhost:8069/bar/deleteIngredient"

    response = requests.delete(url, json={"id": id})

    if response.status_code == 200:
        return True
    else:
        return False

#Orders##########################
def getOrders(id):
    url = "http://localhost:8069/bar/getOrder/"+str(id)

    response = requests.request("GET", url)

    if (response.status_code == 200):
        jsonResult = response.json()
        allOrders={}
        for order in jsonResult["data"]:
            allOrders[order["id"]]={
                "name":order["name"],
                "client":order["client"],
                "pax":order["pax"],
                "waiter":order["waiter"],
                "register":order["register"],
                "aditionalData":order["aditionalData"],
                "pay":order["pay"],
                "state":order["state"],
            }

        return allOrders

def addOrder(post):
    url = "http://localhost:8069/bar/addOrder"

    response = requests.post(url, json=post)

    if response.status_code == 200:
        id = response.json()["result"]["id"]
        return id
    else:
        return None


def updateOrder(id, post):
    url = "http://localhost:8069/bar/updateOrder/"+str(id)

    response = requests.put(url, json=post)

    if response.status_code == 200:
        return True
    else:
        return False

def deleteOrder(id):
    url = "http://localhost:8069/bar/deleteOrder"

    response = requests.delete(url, json={"id": id})

    if response.status_code == 200:
        return True
    else:
        return False
####CREATE INVOICE #############
def createInvoice(order_id):
    url = "http://localhost:8069/bar/create_invoice"
    data = { "id": order_id }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return True
    else:
        return False

#Registers##########################
def getRegisters(id):
    url = "http://localhost:8069/bar/getRegister/"+str(id)

    response = requests.request("GET", url)

    if (response.status_code == 200):
        jsonResult = response.json()
        allRegisters={}
        for register in jsonResult["data"]:
            allRegisters[register["id"]]={
                "quantity":register["quantity"],
                "order":register["order"],
                "product":register["product"]
            }

        return allRegisters

def addRegister(post):
    url = "http://localhost:8069/bar/addRegister"

    response = requests.post(url, json=post)

    if response.status_code == 200:
        id = response.json()["result"]["id"]
        return id
    else:
        return None

def updateRegister(id, post):
    url = "http://localhost:8069/bar/updateRegister"+str(id)

    response = requests.put(url, json=post)

    if response.status_code == 200:
        return True
    else:
        return False

def deleteRegister(id):
    url = "http://localhost:8069/bar/deleteRegister"

    response = requests.delete(url, json={"id": id})

    if response.status_code == 200:
        return True
    else:
        return False

#Invoice##########################
def getInvoice(id):
    url = "http://localhost:8069/bar/getInvoice/"+str(id)

    response = requests.request("GET", url)

    if (response.status_code == 200):
        jsonResult = response.json()
        allInvoices={}
        for invoice in jsonResult["data"]:
            allInvoices[invoice["id"]]={
                "name": invoice["name"],           
                "pay": invoice["pay"],
                "vat": invoice["vat"],
                "lines": invoice["lines"],
                "client": invoice["client"],
                "total": invoice["total"],
        }
        return allInvoices
    else:
        return None

def addInvoice(post):
    url = "http://localhost:8069/bar/addInvoice"

    response = requests.post(url, json=post)

    if response.status_code == 200:
        id = response.json()["result"]["id"]
        return id
    else:
        return None

def updateInvoice(id, post):
    url = "http://localhost:8069/bar/updateInvoice"+str(id)

    response = requests.put(url, json=post)

    if response.status_code == 200:
        return True
    else:
        return False

def deleteInvoice(id):
    url = "http://localhost:8069/bar/deleteInvoice"

    response = requests.delete(url, json={"id": id})

    if response.status_code == 200:
        return True
    else:
        return False

#InvoiceLines##########################
def getInvoiceLine(id):
    url = "http://localhost:8069/bar/getInvoiceLine/"+str(id)

    response = requests.request("GET", url)
    if (response.status_code == 200):
        jsonResult = response.json()
        allLines={}
        for line in jsonResult["data"]:
            allLines[line["id"]] = {
                "quantity": line["quantity"],
                "invoice": line["invoice"],
                "product": line["product"]
            }
        return allLines
    else:
        return None

def addInvoiceLine(post):
    url = "http://localhost:8069/bar/addInvoiceLine"

    response = requests.post(url, json=post)

    if response.status_code == 200:
        id = response.json()["result"]["id"]
        return id
    else:
        return None

def updateInvoiceLine(id, post):
    url = "http://localhost:8069/bar/updateInvoiceLine"+str(id)

    response = requests.put(url, json=post)

    if response.status_code == 200:
        return True
    else:
        return False

def deleteInvoiceLine(id):
    url = "http://localhost:8069/bar/deleteInvoiceLine"

    response = requests.delete(url, json={"id": id})

    if response.status_code == 200:
        return True
    else:
        return False
