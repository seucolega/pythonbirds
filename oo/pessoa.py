class Pessoa:
    def __init__(self, nome: str = None, idade: int = 35):
        self.nome = nome
        self.idade = idade

    def cumprimento(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p = Pessoa(nome='Maria')
    print(p.cumprimento())
