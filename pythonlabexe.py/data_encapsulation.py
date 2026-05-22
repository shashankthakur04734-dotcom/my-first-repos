class Atm:
    def __init__(self,bal=0):
        self.bal=1000  #it is a public variable
atm1=Atm()
print(atm1.bal)

class Atm:
    def __init__(self,bal=0):
        self._bal=1000  #it is a protected variable
atm1=Atm()
print(atm1._bal)

class Atm:
    def __init__(self,bal=0):
        self.__bal=1000  #it is a private variable
        #getters
    def get_balance(self):
        print(self.__bal)
#setter
    def update_balance(self,amount):
        if amount>0:
            self.__bal+=amount
        else:
            print("invalid")
b=Atm()
b.get_balance()
b.update_balance(1000)
b.get_balance()




