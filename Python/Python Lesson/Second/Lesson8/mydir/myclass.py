class Person:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Custmer(Person):

    def __init__(self,nm,ag,ad,tl):
        super().__init__(nm,ag)

        self.adr = ad
        self.tel = tl

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAdr(self):
        return self.adr

    def getTel(self):
        return self.tel
