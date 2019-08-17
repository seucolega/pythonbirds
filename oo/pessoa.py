class Pessoa:
    def __init__(self, *filhos, nome: str = None, idade: int = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimento(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p1 = Pessoa(nome='José')
    p2 = Pessoa(p1, nome='Maria')
    print(p1.cumprimento())
