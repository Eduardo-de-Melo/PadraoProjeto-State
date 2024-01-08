class Ligado():
    def em_evento(self, evento: str):
        if evento =='desligar':
            print("Desligado")
            return Desligado()
        if evento =='ligar':
            print("Já está ligada, impossível ligar novamente")
            return Ligado()
            
class Desligado():
    def em_evento(self, evento: str):
        if evento =='ligar':
            print("Ligado")
            return Ligado()
        if evento =='desligar':
            print("Já está desligada, impossível deligar novamente")
            return Ligado()
        
class Interruptor():
    def __init__(self):
        self.state = Desligado()
        
    def em_evento(self, evento: str):
        self.state = self.state.em_evento(evento)
        

        


interruptor = Interruptor()
interruptor.em_evento('ligar')
interruptor.em_evento('ligar')
interruptor.em_evento('desligar')
interruptor.em_evento('desligar')

