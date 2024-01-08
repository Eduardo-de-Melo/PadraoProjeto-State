STATE_desligado = 0
STATE_ligado = 1
     
class Interruptor():
    def __init__(self):
        self.state = STATE_desligado
        
    def getState(self):
        return self.state
    
    def setState(self,state):
        self.state = state
        
    def liga(self):
        if self.state == STATE_ligado:
            print("ja esta ligado")
        else:
            self.state = STATE_ligado
            print("ligou")
    def desliga(self):
        if self.state == STATE_desligado:
            print("ja esta desligado")
        else:
            self.state = STATE_desligado
            print("desligou")
        


interruptor = Interruptor()

interruptor.liga()
interruptor.desliga()
interruptor.desliga()
interruptor.liga()