class Product(object):
 
    def __init__(self, code, stock, price):
        object.__init__(self)
        self.code = code
        self.stock = stock
        self.price = price
 
    def getPrice(self):
        return self.price
 
    def setPrice(self, price):
        self.price = price
 
    def getStock(self):
        return self.stock
 
    def setStock(self, stock):
        self.stock = stock
 
    def getCode(self):
        return self.code
 
    def totalvalue(self):
        return self.getStock()*self.getPrice()
    
p1=Product("10010", 180, 2)
p2=Product("10013", 240, 1)
print(p1.getCode())
