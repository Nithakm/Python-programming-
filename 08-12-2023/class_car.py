class car:
    def __init__(self,color,price,km):
        self.color=color
        self.price=price
        self.km=km
    def __gt__(self,others):
        if(self.price>others.price):
            return True
        else:
            return False
    def __add__(self,others):
        return (self.km+others.km)
c1=car("red",1000000,2000)
c2=car("blue",1500000,2500)
if(c1>c2):
    print("price of car1 is high")
else:
    print("price of car2 is high")
print("Total KMs of two cars:",c1+c2)
