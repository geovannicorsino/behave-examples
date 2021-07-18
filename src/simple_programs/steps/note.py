class Note:
    def __init__(self, value, quantity):
        self.value = value
        self.quantity = quantity

    def __str__(self):
        return "Value:" + str(self.value) + " ,Quantity:" + str(self.quantity)


notes = [
    Note(value=100, quantity=0),
    Note(value=50, quantity=0),
    Note(value=20, quantity=0),
    Note(value=10, quantity=0),
    Note(value=5, quantity=0),
    Note(value=2, quantity=0),
    Note(value=1, quantity=0),
]


def withdraw(money):
    total = 0
    for note in notes:
        while money >= note.value:
            note.quantity += 1
            money -= note.value
            total += 1
    return total
