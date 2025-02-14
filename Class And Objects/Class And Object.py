class Person:
    def __init__(self,name,age,height) -> None:
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return "Name:{} Age:{} Height:{}".format(self.name, self.age, self.height)

  
class Chess_Player(Person):
    def __init__(self,name,age,height,ELO):
        super(Chess_Player, self).__init__(name, age , height)
        self.ELO = ELO

    def __str__(self):
        text = super(Chess_Player, self).__str__()
        text += " ELO:{}".format(self.ELO)
        return text

Johan = Chess_Player("Johan",20,1.80,2428)

print(Johan)




