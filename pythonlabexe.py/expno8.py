class detalis:
    def __init__(self,name,id_no,phone_no,eamil):
        self.name=name
        self.id_no=id_no
        self.phone_no=phone_no
        self.eamil=eamil
    def display(self):
        print("detalis: ")
        print(f"detalis id:{self.name}")
        print(f"detalis id:{self.id_no}")
        print(f"detalis id:{self.phone_no}")
        print(f"detalis id:{self.eamil}")
    def update_customer(self,name=None,id_no=None,phone_no=None,eamil=None):
        if name is not None:
            self.name=name
        if id_no is not None:
            self.id_no=id_no
        if phone_no is not None:
            self.phone_no=phone_no
        if eamil is not None:
            self.eamil=eamil
    
c1=detalis("shashank",2553,"05686879900","mrv02gamil.com")
c1.display()
c1.update_customer(name="shenil",id_no=20034)
c1.display()
c2=detalis(input())

