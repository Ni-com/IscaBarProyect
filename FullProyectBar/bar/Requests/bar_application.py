import requests

menu={}

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
#print(getProduct())

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
            "products":category["products"]
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


def getCompleteProduct(allProducts, allCategories):
    completeProducts=allProducts
    for product in completeProducts:
        cat=None
        if completeProducts[product]["category"] != False or []:
            for category in completeProducts[product]["category"]:
                if category in allCategories:
                    cat=allCategories[category]["name"]
                completeProducts[product]["category"]=cat
        
    return completeProducts

def getMenu(completeProduct, allIngredients):
    menu=allProducts
    for product in menu:
        dicIngredients={}
        for ingredient in menu[product]["ingredients"]:
            if ingredient in allIngredients:
                dicIngredients[ingredient]=allIngredients[ingredient]
            menu[product]["ingredients"]=dicIngredients
    return menu



allCategories=getCategory("")
allProducts=getProduct("")
completeProduct=getCompleteProduct(allProducts,allCategories)

allIngredients=getIngredients("")



