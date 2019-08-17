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
    p2.sobrenome = 'Silva'
    if 'sobrenome' in p2.__dict__:
        print(p2.__dict__['sobrenome'])
    del p2.sobrenome
    if 'sobrenome' in p2.__dict__:
        print(p2.__dict__['sobrenome'])
