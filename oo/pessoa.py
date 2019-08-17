class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome: str = None, idade: int = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimento(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p1 = Pessoa(nome='José')
    p2 = Pessoa(p1, nome='Maria')
    print(Pessoa.olhos, Pessoa.__dict__)
    print(p1.olhos, p1.__dict__)
    p1.olhos = 1
    print(p1.olhos, p1.__dict__)
    Pessoa.olhos = 3
    print(p1.olhos, p1.__dict__)
    print(p2.olhos, p2.__dict__)
