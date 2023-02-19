from ingredient import Ingredient
from bar_application import getIngredients
from bar_application import updateIngredient
from bar_application import addIngredient
from bar_application import deleteIngredient


class ControllerIngredient():
    def __init__(self):
        self.__ingredients = {}

    def updateIngredients(self):
        allIngredients = getIngredients("")
        for id in allIngredients:
            if id not in self.__ingredients:
                name = allIngredients[id]["name"]
                allergies = allIngredients[id]["allergies"]
                if allergies == False:
                    allergies = "Sin informacion"
                nutritionalValue = allIngredients[id]["nutritionalValue"]
                if nutritionalValue == False:
                    nutritionalValue = "Sin informacion"
                products = allIngredients[id]["products"]
                if products == False:
                    products = []
                newIngredient = Ingredient(id,name, nutritionalValue, allergies, products)
                self.__ingredients[id] = newIngredient
        return True

    def addIngredient(self, name, allergies, nutritionalValue):
        post = {

            "name": name,
            "allergies": allergies,
            "nutritionalValue": nutritionalValue

        }
        id = addIngredient(post)
        if id == None:
            return False

        completeIngredient = getIngredients(id)
        name = completeIngredient[id]["name"]
        allergies = completeIngredient[id]["allergies"]
        if allergies == False:
            allergies = "Sin informacion"
        nutritionalValue = completeIngredient[id]["nutritionalValue"]
        if nutritionalValue == False:
            nutritionalValue = "Sin informacion"
        products = completeIngredient[id]["products"]
        if products == False:
            products = []
        ingredientUpdated = Ingredient(id,name,nutritionalValue,allergies,products)
        self.__ingredients[id] = ingredientUpdated
        return True

    def getAllIngredients(self):
        allingredients = getIngredients("")
        return allingredients

    def getAllInfo(self, id):
        if id not in self.__ingredients:
            return None
        ingredient = self.__ingredients[id]
        info = "Nombre de ingrediente: "+str(ingredient.getName()) + "\n" + "Valor nutricional: " + str(ingredient.getNutritionalValue())+ "\nAlegias " + str(ingredient.getAllergies())
        return info

    def setIngredient(self, id, put):
        if id not in self.__ingredients:
            return False
        if updateIngredient(id, put):
            completeIngredient = getIngredients(id)
            name = completeIngredient[id]["name"]
            allergies = completeIngredient[id]["allergies"]
            if allergies == False:
                allergies = "Sin informacion"
            nutritionalValue = completeIngredient[id]["nutritionalValue"]
            if nutritionalValue == False:
                nutritionalValue = "Sin informacion"
            products = completeIngredient[id]["products"]
            
            if products == False:
                products = []
            ingredientUpdated = Ingredient(id,name,nutritionalValue,allergies,products)
            self.__ingredients[id] = ingredientUpdated
            return True
        return False

    def deleteIngredient(self, id):
        if id in self.__ingredients:
            if deleteIngredient(id):
                del self.__ingredients[id]
                return True
            else:
                return False
        else:
            return False
    
    def checkIngredientInProduct(self, idIngredient, idProduct):
        if idIngredient in self.__ingredients:
            ingredient=self.__ingredients[idIngredient]
            if idProduct not in ingredient.getProducts():
                return True
        return False

    def getName(self, id):
        if id in self.__ingredients:
            ingredient=self.__ingredients[id]
            return ingredient.getName()
    
    def getProducts(self,id):
        if id in self.__ingredients:
            ingredient=self.__ingredients[id]
            print("todos los productos en ingrediente: " + str(ingredient.getProducts()))
            return ingredient.getProducts()

    def checkIngredientNotInProduct(self, idIngredient, idProduct):
        if idIngredient in self.__ingredients:
            ingredient=self.__ingredients[idIngredient]
            if idProduct in ingredient.getProducts():
                return True
        return False