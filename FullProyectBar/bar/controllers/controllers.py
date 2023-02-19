from odoo import http
from odoo.http import json, request


class ProductApp(http.Controller):
    
    @http.route(['/bar/getProduct',"/bar/getProduct/<int:productid>"], auth='public', type='http')
    def getProduct(self, productid=None, **kw):
        if productid:
            domain=[("id","=", productid)]
        else:
            domain=[]
        productdata=http.request.env["bar.product_model"].sudo().search_read(domain,["name","description","price","stock","category","ingredients"])
        data={"status":200,
               "data":productdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/bar/getProductsAndCategories', '/bar/getProductsAndCategories/<int:productid>'], auth='public', type='http')
    def getProductAndCategories(self, productid=None, **kw):
        domain = [("id","=", productid)] if productid else []
        products = http.request.env["bar.product_model"].sudo().search_read(domain, ["name","description","price","stock","category","ingredients"])
        details = []
        for product in products:
            for category_id in product["category"]:
                category = http.request.env["bar.category_model"].sudo().search_read([("id","=", category_id)], ["name","description","products","parent_id","complete_name"])
                details.append(category)
            product["category"] = details
            details = []
        data = {"status":200, "data":products}
        return http.Response(json.dumps(data).encode("utf8"), mimetype="application/json")

    @http.route('/bar/addProduct', auth='public', type='json', method="POST")
    def addProduct(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["bar.product_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/bar/updateProduct/<int:productid>', auth='public', type='json', method="PUT")
    def updateProduct(self, productid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar.product_model"].sudo().search([("id", "=", productid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/bar/deleteProduct', auth='public', type='json', method="DELETE")
    def deleteCat(self, **kw):
        productid = request.jsonrequest["id"]
        try:
            result = http.request.env["bar.product_model"].sudo().search([("id", "=", productid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

class CategoryApp(http.Controller):

    @http.route(['/bar/getCategory',"/bar/getCategory/<int:categoryid>"], auth='public', type='http')
    def getCategory(self, categoryid=None, **kw):
        if categoryid:
            domain=[("id","=", categoryid)]
        else:
            domain=[]
        categorydata=http.request.env["bar.category_model"].sudo().search_read(domain,["name","description","products","parent_id","complete_name"])
        data={"status":200,
              "data":categorydata}    #cambiar por data
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar/addCategory', auth='public', type='json', method="POST")
    def addCategory(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["bar.category_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data

    @http.route('/bar/updateCategory/<int:categoryid>', auth='public', type='json', method="PUT")
    def updateCategory(self, categoryid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar.category_model"].sudo().search([("id", "=", categoryid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/bar/deleteCategory', auth='public', type='json', method="DELETE")
    def deleteCategory(self, **kw):
        categoryid = request.jsonrequest["id"]
        try:
            result = http.request.env["bar.category_model"].sudo().search([("id", "=", categoryid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

class IngredientApp(http.Controller):

    @http.route(['/bar/getIngredient',"/bar/getIngredient/<int:ingredientid>"], auth='public', type='http')
    def getIngredient(self, ingredientid=None, **kw):
        if ingredientid:
            domain=[("id","=", ingredientid)]
        else:
            domain=[]
        ingredientdata=http.request.env["bar.ingredient_model"].sudo().search_read(domain,["name","allergies","nutritionalValue","products"])
        data={"status":200,
               "data":ingredientdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar/addIngredient', auth='public', type='json', method="POST")
    def addIngredient(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["bar.ingredient_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/bar/updateIngredient/<int:ingredientid>', auth='public', type='json', method="PUT")
    def updateIngredient(self, ingredientid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar.ingredient_model"].sudo().search([("id", "=", ingredientid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/bar/deleteIngredient', auth='public', type='json', method="DELETE")
    def deleteIngredient(self, **kw):
        ingredientid = request.jsonrequest["id"]
        try:
            result = http.request.env["bar.ingredient_model"].sudo().search([("id", "=", ingredientid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

class RegisterApp(http.Controller):

    @http.route(['/bar/getRegister',"/bar/getRegister/<int:registerid>"], auth='public', type='http')
    def getRegister(self, registerid=None, **kw):
        if registerid:
            domain=[("id","=", registerid)]
        else:
            domain=[]
        registerdata=http.request.env["bar.register_model"].sudo().search_read(domain,["quantity","order","product","anotation"])
        data={"status":200,
               "data":registerdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar/addRegister', auth='public', type='json', method="POST")
    def addRegister(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["bar.register_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/bar/updateRegister/<int:registerid>', auth='public', type='json', method="PUT")
    def updateRegister(self, registerid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar.register_model"].sudo().search([("id", "=", registerid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/bar/deleteRegister', auth='public', type='json', method="DELETE")
    def deleteRegister(self, **kw):
        registerid = request.jsonrequest["id"]
        try:
            result = http.request.env["bar.register_model"].sudo().search([("id", "=", registerid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data
class OrderApp(http.Controller):

    @http.route(['/bar/getOrder',"/bar/getOrder/<int:orderid>"], auth='public', type='http')
    def getOrder(self, orderid=None, **kw):
        if orderid:
            domain=[("id","=", orderid)]
        else:
            domain=[]
        orderdata=http.request.env["bar.order_model"].sudo().search_read(domain,["name","client","pax","waiter","register","aditionalData","pay","state"])
        data={"status":200,
               "data":orderdata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar/addOrder', auth='public', type='json', method="POST")
    def addOrder(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["bar.order_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/bar/updateOrder/<int:orderid>', auth='public', type='json', method="PUT")
    def updateOrder(self, orderid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar.order_model"].sudo().search([("id", "=", orderid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/bar/deleteOrder', auth='public', type='json', method="DELETE")
    def deleteOrder(self, **kw):
        orderid = request.jsonrequest["id"]
        try:
            result = http.request.env["bar.order_model"].sudo().search([("id", "=", orderid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data
    
    @http.route('/bar/create_invoice', auth='public', type='json', method="POST")
    def create_invoice(self, **kw):
        orderid = request.jsonrequest["id"]
        order = http.request.env["bar.order_model"].sudo().search([("id","=", orderid)])
        if order:
            order.create_invoice()
            data = { "status": 200}
            return data
        else:
            data = { "status": 404,
                    "error": "Invoice not created"}
        return http.Response(json.dumps(data), content_type='application/json')

class InvoiceApp(http.Controller):

    @http.route(['/bar/getInvoice',"/bar/getInvoice/<int:invoiceid>"], auth='public', type='http')
    def getInvoice(self, invoiceid=None, **kw):
        if invoiceid:
            domain=[("id","=", invoiceid)]
        else:
            domain=[]
        invoicedata=http.request.env["bar.invoice_model"].sudo().search_read(domain,["name","client","pay","vat","lines","total"])
        data={"status":200,
               "data":invoicedata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar/addInvoice', auth='public', type='json', method="POST")
    def addInvoice(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["bar.invoice_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/bar/updateInvoice/<int:invoiceid>', auth='public', type='json', method="PUT")
    def updateInvoice(self, invoiceid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar.invoice_model"].sudo().search([("id", "=", invoiceid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/bar/deleteInvoice', auth='public', type='json', method="DELETE")
    def deleteInvoice(self, **kw):
        invoiceid = request.jsonrequest["id"]
        try:
            result = http.request.env["bar.invoice_model"].sudo().search([("id", "=", invoiceid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data
class InvoiceLinesApp(http.Controller):

    @http.route(['/bar/getInvoiceLine',"/bar/getInvoiceLine/<int:invoicelineid>"], auth='public', type='http')
    def getInvoiceLine(self, invoicelineid=None, **kw):
        if invoicelineid:
            domain=[("id","=", invoicelineid)]
        else:
            domain=[]
        invoicelinedata=http.request.env["bar.invoicelines_model"].sudo().search_read(domain,["quantity","invoice","product"])
        data={"status":200,
               "data":invoicelinedata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/bar/addInvoiceLine', auth='public', type='json', method="POST")
    def addInvoiceLine(self, **kw):
        response=request.jsonrequest
        try:
            result=http.request.env["bar.invoicelines_model"].sudo().create(response)
            data={ "status":200,
                    "id":result.id}
            return data
        except Exception as e:
            data={ "status":404,
                    "error":e}
            return data
    
    @http.route('/bar/updateInvoiceLine/<int:invoicelineid>', auth='public', type='json', method="PUT")
    def updateInvoiceLine(self, invoicelineid, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["bar.invoicelines_model"].sudo().search([("id", "=", invoicelineid)])
            result.write(response)
            data = { "status": 200,
                    "id": result.id}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data

    @http.route('/bar/deleteInvoiceLine', auth='public', type='json', method="DELETE")
    def deleteInvoiceLine(self, **kw):
        invoicelineid = request.jsonrequest["id"]
        try:
            result = http.request.env["bar.invoicelines_model"].sudo().search([("id", "=", invoicelineid)])
            result.unlink()
            data = { "status": 200}
            return data
        except Exception as e:
            data = { "status": 404,
                    "error": e}
            return data