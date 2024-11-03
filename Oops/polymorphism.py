class Bird:
    def sound(self):
        return "Bird Sounds"
    
class Duck(Bird):
    def sound(self):
        return "Quacks"

class Owl(Bird):
    def sound(self):
        return "Hoots"

def make_sound(bird):
    print(bird.sound())

duck=Duck()
owl=Owl()
make_sound(duck)
make_sound(owl)

# Objects of different classes, objects of same superclass