from abc import ABC, abstractmethod
class product:
    def __init__(self,name,price: float):
        self.name=name
        self.price=price

    def get_details(self):
        return f"Name of product: {self.name}, Price of product: {self.price}"
    
class discountable(ABC):
    @abstractmethod
    def apply_discount(self):
        pass


class Eproduct(product,discountable):
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty=warranty

    def get_details(self):
        discount=self.apply_discount()
        return f"Name of product: {self.name}, Price of product: {self.price}, Warranty: {self.warranty}, After Discount: {discount}"
    
    def apply_discount(self):
        d=self.price*0.1
        return self.price-d

class Cproduct(product,discountable):
    def __init__(self, name, price,size):
        super().__init__(name, price)
        self.size=size

    def get_details(self):
        discount=self.apply_discount()
        return f"Name of product: {self.name}, Price of product: {self.price}, Size: {self.size}, After Discount: {discount}"
    
    def apply_discount(self):
        d=self.price*0.4
        return self.price-d
def details(product):
    for i in product:
        print(i.get_details())
    
p=[Eproduct("Laptop", 34000,1),Cproduct("Jeans",1500,"M")]
details(p)