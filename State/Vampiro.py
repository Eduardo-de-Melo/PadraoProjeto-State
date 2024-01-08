class Vampiro:
    def __init__(self):
        self.state = None
        
    def se_mover(self):
        self.state.se_mover()
     
class Humano:
    def se_mover(self):
        print("Andando")
        
class Morcego:
    def se_mover(self):
        print("Voando")
        
dracula = Vampiro()
dracula.state = Humano()
dracula.se_mover()
dracula.state = Morcego()
dracula.se_mover()