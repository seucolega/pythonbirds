"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
- Motor
- Direção

O Motor terá a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos:
- Atributo de dado velocidade
- Método acelerar, que deverá incremetar a velocidade em uma unidade
- Método frear, que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
- Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
- Método girar_a_esquerda
- Método girar_a_direita

  N
O   L
  S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> # Testando o Carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
DIRECAO = [NORTE, LESTE, SUL, OESTE]


class Direcao:
    def __init__(self):
        self.valor = NORTE

    def girar_a_esquerda(self):
        self.valor = DIRECAO[DIRECAO.index(self.valor) - 1]

    def girar_a_direita(self):
        self.valor = DIRECAO[(DIRECAO.index(self.valor) + 1) % 4]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(self.velocidade - 2, 0)


class Carro:
    def __init__(self, direcao: Direcao, motor: Motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()


if __name__ == '__main__':
    motor = Motor()
    direcao = Direcao()
    direcao.girar_a_esquerda()
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    carro = Carro(direcao, motor)
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()