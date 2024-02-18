class Veiculo:
    
  def __init__(self):
    self.modelo = None
    self.motor = None
    self.cor = None
    
  def __str__(self):
    return f"Veículo: {self.modelo}, Cor: {self.cor}, Motor: {self.motor}"
    
class VeiculoBuilder:
  
    def __init__(self):
      self.veiculo = Veiculo()
      
    def set_modelo(self, modelo):
      self.veiculo.modelo = modelo 
      return self 
    
    def set_cor(self, cor):
      self.veiculo.cor = cor 
      return self 
    
    def set_motor(self, motor):
      self.veiculo.motor = motor 
      return self 
    
    def build(self):
      veiculo = self.veiculo
      self.veiculo = Veiculo()
      return veiculo
    

class Diretor:
    def construir_carro_luxo(self, builder):
        return builder.set_modelo("Carro de Luxo").set_cor("Preto").set_motor("V8").build()

    def construir_moto_esportiva(self, builder):
        return builder.set_modelo("Moto Esportiva").set_cor("Vermelho").set_motor("4 cilindros").build()

    def construir_caminhao_robusto(self, builder):
        return builder.set_modelo("Caminhão Robusto").set_cor("Azul").set_motor("Diesel").build()

# Exemplo de uso:
builder = VeiculoBuilder()
diretor = Diretor()

carro_luxo = diretor.construir_carro_luxo(builder)
moto_esportiva = diretor.construir_moto_esportiva(builder)
caminhao_robusto = diretor.construir_caminhao_robusto(builder)

print(f"\n{carro_luxo}\n\n-------------------------------------------------------------\n")
print(f"{moto_esportiva}\n\n----------------------------------------------------------\n")
print(f"{caminhao_robusto}\n")
