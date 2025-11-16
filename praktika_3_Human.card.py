from praktika_3_Human import Human
from praktika_3_card import Card

Adam = Human("Adam")

Adam.sayName()
Adam.sayAge()


card = Card("1234 5678 9101 1213", "01/99", "Adam F")

Adam.addCard(card)
Adam.getCard().pay(1000)
# card.pay(1000)






