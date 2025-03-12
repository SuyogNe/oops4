class computer:
    def __init__(self):
        self.__price = 990

    def sell(self):
        print(f"Selling Price: {self.__price}")

    def mprice(self,newprice):
        self.__price = newprice
        
c = computer()
c.sell()

c.__price = 1000
c.sell()

c.mprice(1500)
c.sell()