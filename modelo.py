class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title() # o "__" serve para proteger atributos, não deixando-o totalmente disponível para edição
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0 # este o usuário não definirá, será incrementado

    @property
    def nome(self):
        return self.__nome

    @nome.setter # usado para alterar algum atributo, sem lançar o "__", por exemplo corrigir o nome do filme/série
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self): # lembrar que só vale dentro da classe
        self.__likes += 1

    def likes(self):
        return self.__likes

    @property # como foi protegido o likes para __likes, para não mudar todas as referências, cria-se o @property, que acerta o retorno.
    def likes(self):
        return self.__likes

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter # usado para alterar algum atributo, sem lançar o "__", por exemplo corrigir o nome do filme/série
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


    def dar_like(self):
        self.__likes += 1

    @property # como foi protegido o likes para __likes, para não mudar todas as referências, cria-se o @property, que acerta o retorno.
    def likes(self):
        return self.__likes

vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)


vingadores.dar_like() #testando o incremento
atlanta.dar_like()
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - '
      f'Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - '
      f'Likes: {atlanta.likes}')

