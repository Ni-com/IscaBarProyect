from category import Category
from bar_application import getCategory
from bar_application import updateCategory
from bar_application import addCategory
from bar_application import deleteCategory
from productcontroller import ControllerProduct
controllerProduct = ControllerProduct()

class ControllerCategory():
    def __init__(self):
        self.__category = {}

    def updateCategories(self):
        allCategories = getCategory("")
        for id in allCategories:
            #if id not in self.__category:
                name = allCategories[id]["name"]
                description = allCategories[id]["description"]
                if description == False:
                    description = "Sin descripcion"
                products = allCategories[id]["products"]
                if products == False:
                    products = []
                newCategory = Category(id,name,description,products)
                self.__category[id] = newCategory
        return True

    def addCategory(self,name,description):
        post={
            
            "name":name,
            "description":description,
        }
        id= addCategory(post)
        if id == None:
            return False

        completeCategory=getCategory(id)

        name=completeCategory[id]["name"]
        description=completeCategory[id]["description"]
        products=completeCategory[id]["products"]
        if products==False:
            products=[]
        newCategory= Category(id,name,description,products)
        self.__category[id]=newCategory
        return True

        

    def getAllInfo(self, id):
        if id not in self.__category:
            return None
        category=self.__category[id]
        info="Nombre de carta: "+str(category.getName()) + " - " + str(category.getDescription())
        return info

    def setCategory(self,id,put):
        if id not in self.__category:
            return False
        if updateCategory(id,put):
            
            completeCategory=getCategory(id)
            name=completeCategory[id]["name"]
            description=completeCategory[id]["description"]
            products=completeCategory[id]["products"]
            if products==False:
                products=[]
            categoryUpdated= Category(id,name,description,products)
            

            self.__category[id]=categoryUpdated
            return True
    def deleteCategory(self, id):
        if id not in self.__category:
            return False
        if deleteCategory(id):
            del self.__category[id]
            return True
        else:
            return False
    
    def getAllCategories(self):
        allcategories = getCategory("")
        return allcategories
    
    def productInCategories(self, id):
        if id not in self.__category:
            return False
        category=self.__category[id]
        productsInCategory=category.getProducts()
        return productsInCategory

    def ProductIsInCategory(self, id, product):
        if id not in self.__category:
            return False
        category=self.__category[id]
        productsInCategory=category.getProducts()
        if product not in productsInCategory:
            return False
        return True