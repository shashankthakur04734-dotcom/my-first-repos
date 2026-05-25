# class person:
#     def __init__(self,name,branch,roll_no):
#         self.name=name
#         self.branch=branch
#         self.roll_on=roll_no

#     def display(self):
#             print("my name is : ",self.name)
#             print("my branch is: ", self.branch)
#             print("my roll_on is: ",self.roll_on)

# shashank=person("shashank","csm",443)
# shashank.display()

class bankaccount:
    def __init__(self,acc_num,acc_holder,bal=0):
        self.acc_num=acc_num
        self.acc_holder=acc_holder
        self.bal=bal

    def doposite(self,amount):
        if amount>0:
            self.bal+=amount
            print("after doposite: ",self.bal)
        else:
            print("amount must be positive")
    def withdraw(self,amount):
        if amount>0:
            self.bal+=amount
            print("after withdraw: ",self.bal)
        else:
            print("insufficientn balance")
   
        





        

        