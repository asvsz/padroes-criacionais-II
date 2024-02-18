from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def clone(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def clone(self):
        return Circulo(self.raio)

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def clone(self):
        return Retangulo(self.largura, self.altura)

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def clone(self):
        return Triangulo(self.base, self.altura)

# Exemplo de uso
circulo_original = Circulo(5)
circulo_clone = circulo_original.clone()

retangulo_original = Retangulo(35,16)
retangulo_clone = retangulo_original.clone()

triangulo_original = Triangulo(6,12)
triangulo_clone = triangulo_original.clone()

print(f"Raio do círculo original: {circulo_original.raio}")
print(f"\nRaio do círculo clonado: {circulo_clone.raio}\n\n--------------------------------------")


print(f"\nLargura do retângulo original: {retangulo_original.largura}")
print(f"\nAltura do retângulo original: {retangulo_original.altura}")
print(f"\nLargura do retângulo clonado: {retangulo_clone.largura}")
print(f"\nAltura do retângulo clonado: {retangulo_clone.altura}\n\n-------------------------------")

print(f"\nBase do triângulo original: {triangulo_original.base}")
print(f"\nAltura do triângulo original: {triangulo_original.altura}")
print(f"\nBase do triângulo clonado: {triangulo_clone.base}")
print(f"\nAltura do triângulo clonado: {triangulo_clone.altura}")
