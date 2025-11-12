class Human:
    age = 33
    def __init__(self, name):
        print("Я создался")
        self.humanname = name


    def sayName(self):
        print("меня зовут", self. humanname)

    def sayAge(self):
        print(self.age)


    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card


adam = Human("Аdam")

adam.sayName()
adam.sayAge()



