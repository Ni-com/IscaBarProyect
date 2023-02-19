from productcontroller import ControllerProduct
from requestcontroller import ControllerRequest
from categoryController import ControllerCategory
from ingredientController import ControllerIngredient
controllerProduct = ControllerProduct()
controllerCategory=ControllerCategory()
controllerRequest = ControllerRequest()
controllerIngredient=ControllerIngredient()
controllerProduct.updateProducts()
controllerCategory.updateCategories()
controllerIngredient.updateIngredients()
#box=0.00

def menuProduct():
    print("Cartas disponibles para ver: ")
    categories=controllerProduct.getCategory()
    for id in categories:
        print(str(id) + " - " + str(categories[id]["name"]))
    print(str(0) + " - " + "Productos sin carta")
    select = int(input("Seleccione opcion: "))
    return select
    
def showMenu(select):
    categories=controllerProduct.getCategory()
    dicProducts = controllerProduct.getProducts()
    print("-----CARTA-----")

    if select != 0:
        print("Carta "+str(categories[select]["name"])+"\n")
        for id in dicProducts:
            if (dicProducts[id].getCategory()) == categories[select]["name"]:
                print(str(id) + " - "+dicProducts[id].getName())

    if select == 0:
        print("Productos fuera de carta \n")
        for id in dicProducts:
            if (dicProducts[id].getCategory()) == "Sin carta" or []:
                print(str(id) + " - "+dicProducts[id].getName())

    print("-----------------------------------------------------")

def menuCategories():
    print("Cartas disponibles: ")
    allCategories=controllerCategory.getAllCategories()
    for id in allCategories:
        print(str(id) + " - " + str(allCategories[id]["name"]))
   
    option = int(input("Seleccione opcion: "))
    return option

def menuIngredients():
    print("Ingredientes disponibles: ")
    allIngredients=controllerIngredient.getAllIngredients()
    select = int(input(" 1-Todos los ingredientes \n 2-Ingredientes sin producto: "))
    if select==1:
        for id in allIngredients:
            print(str(id) + " - " + str(allIngredients[id]["name"]))
    if select==2:
        for id in allIngredients:
            if len(allIngredients[id]["products"])==0:
                print(str(id) + " - " + str(allIngredients[id]["name"]))
        option = int(input("Seleccione opcion: "))
        return option


def addOrder():
    print("Añadir pedido")
    table = int(input("Numero de mesa: "))
    client = (input("Nombre de cliente  (intro para dejar en blanco): "))
    pax = int(input("Numero de personas en mesa: "))
    waiter = (input("Nombre de camarero (intro para dejar en blanco): "))
    info = (input("Informacion adicional (intro para dejar en blanco): "))
    if (controllerRequest.addRequest(table, client, pax, waiter, info)):
        print("Pedido creado correctamente")
        print("Empezar pedido en esta mesa?")
        print("1 - Si")
        print("2 - No")
        option = int(input("Seleccione opcion: "))
        if option == 1:
            modOrder(table)
        else:
            return
    else:
        print("Error creando producto, revisa la informacion")
        return False


def modOrder(table):
    option=0
    if table == None:
        print("Pedidos disponibles: ")
        orders = controllerRequest.getRequests()
        if len(orders) ==0:
            print("No hay pedidos, vas a tener que añadir uno")
            return False
        for order in orders:
            print("Mesa - " + str(order))

        table = int(input("Seleccione una mesa: "))

    while option!=5:
        print("Mesa seleccionada: " + str(table))
        print("1 - Añadir producto")
        print("2 - Eliminar producto")
        print("3 - Ver informacion de pedido")
        print("4 - Pagar y Finalizar")
        print("5 - Menu Principal")
        option = int(input("Seleccione opcion: "))

        if option == 5:
            break
            

        if option == 1:
            addProduct(table)

        if option == 2:
            delProduct(table)

        if option == 3:
            order=controllerRequest.getRequest(table)
            print("Numero de mesa: " + str(order.getTable()))
            print("Nombre de cliente: " + order.getClient())
            print("Numero de personas en mesa: " + str(order.getPax()))
            print("Nombre de camarero: " + order.getWaiter())
            print("Cuenta total: " + str(order.getPay()))
            print("Informacion adicional: " + order.getExtraInfo())
            print("Pedidos realizados: ")
            dicProducts = order.getOrder()
            for id in dicProducts:
                print(str(id) + " - "+dicProducts[id].getName())

        if option == 4:
            delProduct(delRequest(table))

def addProduct(table):
    #global box
    select = menuProduct()
    showMenu(select)
    id = int(input("Seleccione el numero del producto: "))
    price = controllerProduct.getPrice(id)
    product = controllerProduct.getProduct(id)
    
    if product != False:
        if controllerRequest.addOrder(table, id, product):
            controllerRequest.setPay(table, price)
            print("Producto añadido correctamente")
            print("Cuenta total de la mesa: " +
            str(controllerRequest.getPay(table)))
            
            return
    print("Error al añadir producto")


def delProduct(table):
    #global box
    order = controllerRequest.getRequest(table)
    dicProducts = order.getOrder()

    for id in dicProducts:
        print(str(id) + " - "+dicProducts[id].getName())
        id = int(input("Seleccione el numero del producto a eliminar: "))

    product=controllerProduct.getProduct(id)
    price=-(controllerProduct.getPrice(id))
    
    if product!= False:

        if controllerRequest.delOrder(table, id, product):
            print("Producto eliminado correctamente")
            controllerRequest.setPay(table, price)
            print("Cuenta total de la mesa: " + str(controllerRequest.getPay(table)))
            return
    print("Error al eliminar producto")

def delRequest(table):
    if table == None:
        print("Pedidos disponibles: ")
        orders = controllerRequest.getRequests()
        if len(orders) ==0:
            print("No hay pedidos, vas a tener que añadir uno")
            return False
        for order in orders:
            print("Mesa - " + str(order))

        table = int(input("Seleccione una mesa: "))
        order=controllerRequest.getRequest(table)
        print("Cuenta total a pagar : " + str(order.getPay()))
        print("Eliminar pedido en esta mesa?")
        print("1 - Si")
        print("2 - No")
        option = int(input("Seleccione opcion: "))
        if option == 1:
            if(controllerRequest.delTable(table)):
                print("Pedido eliminado correctamente")
            else:
                print("Error al eliminar los pedidos, revisa los datos")
        else:
            return False

def info():

    while True:
        print("Informacion disponible")
        print("1 - Ver ingredientes de producto")
        print("2 - Ver alergias de producto")
        print("3 - Ver valor nutricional de los ingredientes")
        print("4 - Ver toda la informacion de un producto")
        print("5 - MENU PRINCIPAL")
        option = int(input("Seleccione opcion: "))

        if option ==5:
            break

        if option ==1:
            ingredients=getIngPro()
            if ingredients !=None:
                print("Ingredientes: ")
                for ingredient in ingredients:
                    print(ingredients[ingredient]["name"])
            else:
                print ("Producto incorrecto")

        if option ==2:
            ingredients=getIngPro()
            if ingredients !=None:
                print("Alergias: ")
                for ingredient in ingredients:
                    print("Ingrediente: "+ingredients[ingredient]["name"] + " alergias del ingrediente: " + ingredients[ingredient]["allergies"])
            else:
                print ("Producto incorrecto")
        
        if option ==3:
            ingredients=getIngPro()
            if ingredients !=None:
                print("Informacion del producto: ")
                for ingredient in ingredients:
                    print("Ingrediente: "+ingredients[ingredient]["name"] + " valor nutricional del ingrediente: " + ingredients[ingredient]["nutritionalValue"])
            else:
                print ("Producto incorrecto")

        if option ==4:
            showMenu(1)
            id = int(input("Seleccione el numero del producto: "))
            ingredients=controllerProduct.getIngredients(id)
            if ingredients !=None:
                print("Informacion del producto: ")
                print(controllerProduct.getAllInfo(id))
                for ingredient in ingredients:
                    print("Ingrediente: "+ingredients[ingredient]["name"] + " valor nutricional del ingrediente: "
                    + ingredients[ingredient]["nutritionalValue"]+ " alergias del ingrediente: " + ingredients[ingredient]["allergies"])
            else:
                print ("Producto incorrecto")

def getIngPro():
        showMenu(1)
        id = int(input("Seleccione el numero del producto: "))
        ingredients=controllerProduct.getIngredients(id)
        return ingredients


#######################################CRUD##################################################################3
def menuCrud():
    while True:
        print("MENU CRUD")
        print("1 - Producto")
        print("2 - Ingrediente")
        print("3 - Cartas")
        print("4 - Ver Menu")
        print("5 - Menu Principal")
        option = int(input("Seleccione opcion: "))

        if option ==5:
            break
        if option ==1:
            modProduct()
        if option ==3:
            modcategory()
        if option ==2:
            modIngredient()
        if option ==4:
            select = menuProduct()
            showMenu(select)
            ###############################################PRODUCTOS##############################################################

def modProduct():
     while True:
        print("Menu de producto")
        print("1 - Crear Producto")
        print("2 - Modificar Producto")
        print("3 - Borrar Producto")
        print("4 - Ver Productos")
        print("5 - Añadir Productos a carta")
        print("6 - Quitar Productos de carta")
        print("7 - Añadir ingredientes a producto")
        print("8 - Quitar ingredientes a producto")
        print("9 - Menu CRUD")
        option = int(input("Seleccione opcion: "))

        if option ==9:
            break
        if option ==7:
            ProductAddIngredient()
        if option ==8:
            ProductDeleteIngredient()
        if option ==4:
            select = menuProduct()
            showMenu(select)
            id = int(input("Seleccione numero de producto: "))
            product=controllerProduct.getAllInfo(id)
            if product!= None:
                print("Producto: "+ str(product))
            else:
                print("Producto no encontrado")
                
        if option ==1:
            name = input("Nombre del producto: ")
            description = input("Descripcion del producto: ")
            price=float(input("Precio del producto: "))
            
            
            if controllerProduct.addProduct(name,price,True,description):
                print("Producto añadido correctamente")
            else:
                print("Error al añadir revisa tus datos")
            return
        if option ==2:
            select = menuProduct()
            showMenu(select)
            id = int(input("Seleccione numero de producto: "))
            product=controllerProduct.getAllInfo(id)
            if product!= None:
                while True:
                    product=controllerProduct.getAllInfo(id)
                    put={}
                    print("Producto: "+ str(product))
                    print("Que deseas modificar")
                    print("1 - Nombre del producto")
                    print("2 - Precio producto")
                    print("3 - Stock")
                    print("4 - Descripcion")
                    print("5 - Salir")
                    option = int(input("Seleccione opcion: "))
                    if option ==5:
                        return
                    if option==1:
                        name=input("Nuevo nombre de producto: \n")
                        put["name"]=name
                        if(controllerProduct.setProduct(id,put)):
                            print("Producto modificado")
                        else:
                            print("Error, revisa los datos")
                        
                    if option==4:
                        description=input("Nueva descripcion de producto: \n")
                        put["description"]=description
                        if(controllerProduct.setProduct(id,put)):
                            print("Producto modificado")
                        else:
                            print("Error, revisa los datos")
                        
                    if option==2:
                        price=float(input("Nuevo precio de producto: \n"))
                        put["price"]=price
                        if(controllerProduct.setProduct(id,put)):
                            print("Producto modificado")
                        else:
                             print("Error, revisa los datos")
                        
                    if option==3:
                        stock=True
                        yes = input("Queda Stock del producto (Y / N) ")
                        if yes!="Y" or yes!="y":
                            stock=False
                        put["stock"]=stock
                        if(controllerProduct.setProduct(id,put)):
                            print("Producto modificado")
                        else:
                             print("Error, revisa los datos")
                        
            else:
                print("Parece que ese producto no se encuentra en la base de datos")
                return

        if option ==3:
            select = menuProduct()
            showMenu(select)
            id = int(input("Seleccione numero de producto: "))
            producto=controllerProduct.getAllInfo(id)
            if producto!= None:
                print("Eliminando: "+ str(producto))
                yes = input("Seguro de que deseas borrar el producto (Y / N) ")
                if yes=="Y" or yes=="y":
                    if(controllerProduct.deleteProduct(id)):
                        print("Producto eliminado")
                        controllerProduct.updateProducts()
                        controllerCategory.updateCategories()
                        controllerIngredient.updateIngredients()
                    else:
                        print("Error con la base de datos")
                else:
                    print("Volviendo al menu crud")
                return
            else:
                print("Parece que el producto indicado no existe")
                return

        if option==5:
            productCategory()

        if option==6:
            deleteProductCategory()
        

###############################################CARTAS##############################################################
def modcategory():
    while True:
        print("Menu de cartas")
        print("1 - Crear Carta")
        print("2 - Modificar Carta")
        print("3 - Borrar Carta")
        print("4 - Ver Carta")
        print("5 - Menu CRUD")
        option = int(input("Seleccione opcion: "))

        if option ==5:
            break
        if option ==4:
            select = menuProduct()
            showMenu(select)
        if option ==1:
            name = input("Nombre de la carta: ")
            description = input("Descripcion de la carta: ")
            if controllerCategory.addCategory(name,description):
                print("Carta añadida correctamente")
            else:
                print("Error al añadir, revisa tus datos")
            return
        if option ==2:
            id = menuProduct()
            categoryinfo=controllerCategory.getAllInfo(id)
            if categoryinfo!= None:
                while True:
                    categoryinfo=controllerCategory.getAllInfo(id)
                    put={}
                    print(""+ str(categoryinfo))
                    print("Que deseas modificar")
                    print("1 - Nombre de carta")
                    print("2 - Descripcion")
                    print("3 - Añadir producto a carta")
                    print("4 - Quitar producto de carta")
                    print("5 - Salir")
                    option = int(input("Seleccione opcion: "))
                    if option ==5:
                        return
                    if option==1:
                        name=input("Nuevo nombre de carta: \n")
                        put["name"]=name
                        if(controllerCategory.setCategory(id,put)):
                            print("Carta modificada")
                        else:
                            print("Error, revisa los datos")
                        
                        
                    if option==2:
                        description=input("Nueva descripcion de carta: \n")
                        put["description"]=description
                        if(controllerCategory.setCategory(id,put)):
                            print("Carta modificada")
                        else:
                             print("Error, revisa los datos")
                        
                    if option==3:
                        productCategory()

                    if option==4:
                        productCategory()
                   

                        
            else:
                print("Parece que esta carta no se encuentra en la base de datos")
                return

        if option ==3: 
            id = menuProduct()
            categoryinfo=controllerCategory.getAllInfo(id)
            if categoryinfo!= None:
                print("Eliminando: "+ str(categoryinfo))
                yes = input("Seguro de que deseas borrar la carta (Y / N) ")
                if yes=="Y" or yes=="y":
                    if(controllerCategory.deleteCategory(id)):
                        controllerProduct.updateProducts()
                        controllerCategory.updateCategories()
                        print("Carta eliminada")
                    else:
                        print("Error con la base de datos")
                else:
                    print("Volviendo al menu crud")
                return
            else:
                print("Parece que la carta indicada no existe")
                return
###############################################INGREDIENTES##############################################################
def modIngredient():
    while True:
        print("Menu de ingredientes")
        print("1 - Crear Ingrediente")
        print("2 - Modificar Ingrediente")
        print("3 - Borrar Ingrediente")
        print("4 - Añadir ingredientes a producto")
        print("5 - Eliminar ingredientes a producto")
        print("6 - Ver ingredientes de los productos")
        print("7 - Menu CRUD")
        option = int(input("Seleccione opcion: "))

        if option ==7:
            break
        if option ==1:
            name = input("Nombre del ingrediente: ")
            nutritionalValue = input("Valor nutricional del ingrediente: ")
            allergies = input("Alergias del ingrediente: ")
            if controllerIngredient.addIngredient(name,nutritionalValue,allergies):
                print("Ingrediente añadido correctamente")
            else:
                print("Error al añadir, revisa tus datos")
            return
            
        if option ==2:
            id = menuIngredients()
            ingredienInfo=controllerIngredient.getAllInfo(id)
            if ingredienInfo!= None:
                while True:
                    ingredienInfo=controllerIngredient.getAllInfo(id)
                    put={}
                    print(""+ str(ingredienInfo))
                    print("Que deseas modificar")
                    print("1 - Nombre de ingrediente")
                    print("2 - Valor nutricional")
                    print("3 - Alergias")
                    print("4 - Salir")
                    option = int(input("Seleccione opcion: "))
                    if option ==4:
                        return
                    if option==1:
                        name=input("Nuevo nombre de ingrediente: \n")
                        put["name"]=name
                        if(controllerIngredient.setIngredient(id,put)):
                            print("Ingrediente modificado correctamente")
                        else:
                            print("Error, revisa los datos")
                        
                    if option==2:
                        nutritionalValue=input("Nuevo valor nutricional: \n")
                        put["nutritionalValue"]=nutritionalValue
                        if(controllerIngredient.setIngredient(id,put)):
                            print("Ingrediente modificado correctamente")
                        else:
                            print("Error, revisa los datos")

                    if option==3:
                        allergies=input("Nuevo nombre de ingrediente: \n")
                        put["allergies"]=allergies
                        if(controllerIngredient.setIngredient(id,put)):
                            print("Ingrediente modificado correctamente")
                        else:
                            print("Error, revisa los datos")
                        
            else:
                print("Parece que este ingrediente no se encuentra en la base de datos")
                return

        if option ==3: 
            id = menuIngredients()
            ingredienInfo=controllerIngredient.getAllInfo(id)
            if ingredienInfo!= None:
                print("Eliminando: "+ str(ingredienInfo))
                yes = input("Seguro de que deseas borrar el ingrediente (Y / N) ")
                if yes=="Y" or yes=="y":
                    if(controllerIngredient.deleteIngredient(id)):
                        print("Ingrediente eliminado")
                        controllerProduct.updateProducts()
                        controllerIngredient.updateIngredients()
                    else:
                        print("Error con la base de datos")
                else:
                    print("Volviendo al menu crud")
                return
            else:
                print("Parece que el ingrediente indicado no existe")
                return

        if option ==4:
            ProductAddIngredient()
        if option ==5:
            ProductDeleteIngredient()
        if option ==6:
            showIngredientProduct()
        
def productCategory():
    id = menuCategories()
    productsInCategories=controllerCategory.productInCategories(id)
    if productsInCategories!=False:
        while True:
            productsInCategories=controllerCategory.productInCategories(id)
            print("Productos en esta carta: ")
            for product in productsInCategories:
                print(str(product) +" - " + controllerProduct.getName(product))
            yes = input("Deseas agregar mas productos (Y / N) ")
            if yes=="Y" or yes=="y":
                print("Productos disponibles para añadir: ")
                showMenu(0)
                product = int(input("Seleccione un producto: (0-Cancelar)"))
                if product==0:
                    print("Volviendo al menu crud") 
                    break
                if(controllerProduct.checkNoCategory(product)):
                    productsInCategories.append(product)
                    putCategory={"products":productsInCategories}
                    putProduct={"category":id}
                    if controllerCategory.setCategory(id,putCategory) and controllerProduct.setProduct(product,putProduct):
                        print("Producto añadido a carta")
                    else:
                        print("Error al añadir producto")

                else:
                    print("Producto no disponible")
            else:
                    print("Volviendo al menu crud")
                    break
    else:
        print("Carta no encontrada")
                    
        
def deleteProductCategory():
    id = menuCategories()
    productsInCategories=controllerCategory.productInCategories(id)
    if productsInCategories!=False:
        while True:
            print("Productos en esta carta: ")
            for product in productsInCategories:
                print(str(product) +" - " + controllerProduct.getName(product))
            yes = input("Deseas eliminar mas productos de la carta(Y / N) ")
            if yes=="Y" or yes=="y":
                print("Productos disponibles para eliminar: ")
                showMenu(id)
                productId = int(input("Seleccione un producto: (0-Cancelar)"))
                if productId==0:
                    print("Volviendo al menu crud") 
                    break
                if(controllerCategory.ProductIsInCategory(id,productId)):
                    productsInCategories.remove(productId)
                    print("lista despues del remove: " + str(productsInCategories))
                    putCategory={"products":productsInCategories}
                    putProduct={"category":False}
                    if controllerCategory.setCategory(id,putCategory) and controllerProduct.setProduct(productId,putProduct):
                        print("Producto eliminado de la carta")
                    else:
                        print("Error al eliminar producto")

                else:
                    print("Producto no disponible")
            else:
                    print("Volviendo al menu crud")
                    break
    else:
        print("Carta no encontrada")

def ProductAddIngredient():
            select = menuProduct()
            showMenu(select)
            productId = int(input("Seleccione un producto al que añadir ingredientes: "))
            nameProduct=controllerProduct.getName(productId)
            if nameProduct!=None:
                while True:
                    allIngredients=controllerProduct.getIngredientsInfo(productId)
                    print("Ingredientes en " + nameProduct)
                    for ingredient in allIngredients:
                        print(controllerIngredient.getName(ingredient))
                    yes = input("Deseas añadir mas ingredientes (Y / N) ")
                    if yes=="Y" or yes=="y":
                        IdIngredient=menuIngredients()
                        if controllerIngredient.checkIngredientInProduct(IdIngredient,productId):
                            allIngredients.append(IdIngredient)
                            allProducts=controllerIngredient.getProducts(IdIngredient)
                            allProducts.append(productId)
                            putIngredient={"products":allProducts}
                            putProduct={"ingredients":allIngredients}
                            if(controllerIngredient.setIngredient(IdIngredient,putIngredient))and controllerProduct.setProduct(productId,putProduct):
                                print("Ingrediente añadido correctamente")
                                continue
                            else:
                                print("Error en la base de datos")
                        else:
                            print("El producto ya tiene ese ingrediente")
                    else:
                        print("Volviendo al menu crud")
                    break
            else:
                print("Producto no disponible")
            return
def ProductDeleteIngredient():
            select = menuProduct()
            showMenu(select)
            productId = int(input("Seleccione un producto al que eliminar ingredientes: "))
            nameProduct=controllerProduct.getName(productId)
            if nameProduct!=None:
                while True:
                    allIngredients=controllerProduct.getIngredientsInfo(productId)
                    print("Ingredientes en " + nameProduct)
                    for ingredient in allIngredients:
                        print(str(ingredient)+ " - "+controllerIngredient.getName(ingredient))
                    yes = input("Deseas eliminar mas ingredientes (Y / N) ")
                    if yes=="Y" or yes=="y":
                        IdIngredient=int(input("Seleccione un ingrediente que eliminar: "))
                        if controllerIngredient.checkIngredientNotInProduct(IdIngredient,productId):
                            allIngredients.remove(IdIngredient)
                            allProducts=controllerIngredient.getProducts(IdIngredient)
                            allProducts.remove(productId)
                            putIngredient={"products":allProducts}
                            putProduct={"ingredients":allIngredients}
                            if(controllerIngredient.setIngredient(IdIngredient,putIngredient))and controllerProduct.setProduct(productId,putProduct):
                                print("Ingrediente eliminado correctamente")
                                continue
                            else:
                                print("Error en la base de datos")
                        else:
                            print("El producto no tiene ese ingrediente")
                    else:
                        print("Volviendo al menu crud")
                    break
            else:
                print("Producto no disponible")
            return
def showIngredientProduct():
            select = menuProduct()
            showMenu(select)
            productId = int(input("Seleccione un producto al que ver ingredientes: "))
            nameProduct=controllerProduct.getName(productId)
            if nameProduct!=None:
                    allIngredients=controllerProduct.getIngredientsInfo(productId)
                    print("Ingredientes en " + nameProduct)
                    for ingredient in allIngredients:
                        print(controllerIngredient.getName(ingredient))
                    else:
                        print("Volviendo al menu crud")
            else:
                print("Producto no disponible")


while True:
    print("MENU PRINCIPAL")
    print("1 - Mostrar carta")
    print("2 - Añadir pedido")
    print("3 - Acceder a pedidos")
    print("4 - Finalizar pedido")
    print("5 - Informacion sobre carta")
    print("6 - Ver total del dia")
    print("7 - Menu Creacion de cartas")
    print("8 - FIN")
    option = int(input("Seleccione opcion: "))

    if option ==8:
        print("FIN del programa")
        break

    if option ==1:
        select = menuProduct()
        showMenu(select)

    if option ==2:
        addOrder()


    if option ==3:
        modOrder(None)
    
    if option ==4:
        delRequest(None)

    if option ==5:
        info()
    
    if option ==6:
        #print("Total del dia: " + str(controllerRequest.getBox))
        print("Total del dia: ")
        
    if option ==7:
        menuCrud()

