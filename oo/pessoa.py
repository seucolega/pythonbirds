class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome: str = None, idade: int = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimento(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass



if __name__ == '__main__':
    p1 = Pessoa(nome='José')
    p2 = Pessoa(p1, nome='Maria')
    print(Pessoa.metodo_estatico(), p1.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), p1.nome_e_atributos_de_classe())
    print(isinstance(Pessoa(), Pessoa))
    print(isinstance(Pessoa(), Homem))
    print(isinstance(Homem(), Pessoa))
    print(isinstance(Homem(), Homem))
