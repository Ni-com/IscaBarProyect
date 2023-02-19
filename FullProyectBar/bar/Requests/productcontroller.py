from product import Product
from bar_application import getMenu
from bar_application import getProduct
from bar_application import getIngredients
from bar_application import addProduct
from bar_application import getCategory
from bar_application import deleteProduct
from bar_application import updateProduct
fullProduct=getProduct("")
fullIngredients=getIngredients("")



class ControllerProduct():
    def __init__(self):
        self.__product = {}
        

    def updateProducts(self):
        fullMenu=getMenu(fullProduct,fullIngredients)
        for id in fullMenu:
            #if id not in self.__product:
                name=fullMenu[id]["name"]
                price=fullMenu[id]["price"]
                stock=fullMenu[id]["stock"]
                description=fullMenu[id]["description"]
                category=fullMenu[id]["category"]
                if category==False or []:
                    category="Sin carta"
                ingredients=fullMenu[id]["ingredients"]
                if ingredients==False:
                    ingredients=[]
                newProduct= Product(id,name,price,stock,category,ingredients,description)
                self.__product[id] = newProduct
            
        return True
    
    
            

    def addProduct(self,name,price,stock,description):
        post={
            
            "name":name,
            "price":price,
            "stock":stock,
            "description":description
        }
        id= addProduct(post)
        if id == None:
            return False

        completeProduct=getProduct(id)
        name=completeProduct[id]["name"]
        price=completeProduct[id]["price"]
        stock=completeProduct[id]["stock"]
        description=completeProduct[id]["description"]
        category=completeProduct[id]["category"]
        if category==False or category==[]:
            category="Sin carta"
        else: 
            category=completeProduct[id]["category"][1]
        ingredients=completeProduct[id]["ingredients"]
        if ingredients==False:
            ingredients=[]
        newProduct= Product(id,name,price,stock,category,ingredients,description)
        self.__product[id]=newProduct

        return True

    def getProducts(self):
        return self.__product

    def getProduct(self,id):
        if id not in self.__product:
            return False
        else:
            return self.__product[id]

    def getPrice(self, id):
        product=self.__product[id]
        return product.getPrice()
        
    def getIngredients(self, id):
        if id not in self.__product:
            return None
        product=self.__product[id]
        print("Lista ingredientes en producto: " + str(product.getIngredients()))
        return product.getIngredients()

    
    def getAllInfo(self, id):
        if id not in self.__product:
            return None
        product=self.__product[id]
        info="Nombre del producto: "+product.getName() + "\n Precio: " + str(product.getPrice()) + "\n Carta: " + str(product.getCategory())+ "\n Descripcion: " + str(product.getDescription())
        return info
    
    def lastId(self):
        last=0
        for id in fullProduct:
            if id>last:
                last=id
        last+=1
        return last
    
    def getCategory(self):
        categories=getCategory("")
        return categories
    
    def deleteProduct(self, id):
        if deleteProduct(id):
            del self.__product[id]
            return True
        else:
            return False
    
    def setProduct(self,id,put):
        if id not in self.__product:
            return False
        if updateProduct(id,put):
            
            completeProduct=getProduct(id)
            name=completeProduct[id]["name"]
            price=completeProduct[id]["price"]
            stock=completeProduct[id]["stock"]
            description=completeProduct[id]["description"]
            category=completeProduct[id]["category"]
            if category==False or []:
                category="Sin carta"
            else: 
                category=completeProduct[id]["category"][1]
            ingredients=completeProduct[id]["ingredients"]
            if ingredients==False:
                ingredients=[]
            updatedProduct= Product(id,name,price,stock,category,ingredients,description)
            
            self.__product[id]=updatedProduct
            
            return True
        return False
    
    def getName(self, id):
        if id not in self.__product:
            return None
        product=self.__product[id]
        return product.getName()
    
    def checkNoCategory(self, id):
        if id not in self.__product:
            return False
        product=self.__product[id]
        if product.getCategory()== "Sin carta":
            return True
        return False
    
    def checkCategory(self, id):
        if id not in self.__product:
            return False
        product=self.__product[id]
        if product.getCategory()== "Sin carta":
            return True
        return False
    
    def getIngredientsInfo(self, id):
        if id not in self.__product:
            return None
        completeProduct=getProduct(id)
        ingredients=completeProduct[id]["ingredients"]
        return ingredients

    