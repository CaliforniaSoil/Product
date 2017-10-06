class product(object):
    def __init__(self, price, name, weight, brand, cost, reason, box):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.reason = reason
        self.box = box
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addtax(self):
        self.price += 0.15*self.price
        
        return self
    def retrn(self, reason, box):
        self.reason = reason
        if reason == "defective":
            self.price = 0
            self.status = "defective"
        if box == "opened":
            self.price -= self.price*(0.2) 
        else:
            self.status = "for sale"
        return self
    def displayInfo(self):
        print "Price: $", self.price
        print "Item Name:", self.name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost: $", self.cost
        print "Status:", self.status


product1 = product(1000, "gold", "1oz", "GoldCo", 50, "", "")
product2 = product(10, "gunpowder", "1kilo", "PyrotechnicsCo", 5, "", "")
product3 = product(15, "vodka", "750ml", "Stolichnaya", 5, "", "")
product1.retrn("", "").sell().addtax().displayInfo()
         
        

