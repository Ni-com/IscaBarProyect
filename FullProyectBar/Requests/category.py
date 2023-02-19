class Category:

    def __init__(self,id, name, description, products,parent_id,complete_name):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__products = products
        self.__parent_id=parent_id
        self.__complete_name=complete_name

    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    
    def getProducts(self):
        return self.__products
    
    def getId(self):
        return id

    def getCategory(self):
        return self
    
    def getComplete_Name(self):
        return self.__complete_name
    
    def getParent_ID(self):
        return self.__parent_id

        

    def setName(self, name):
        self.__name = name
    
    def setDescription(self, description):
        self.__description = description

    def setAllergies(self, products):
        self.__products=products

    def setCategory(self, id,name,description,products):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__products = products