class Programa:  #### classe "mãe" (contém atributos e métodos genéricos, que são usadas pelas classes "filhas"
    def __init__(self, nome, ano):  #construtor ## atributos
        self._nome = nome.title()   #### melhor usar somente 1 _, pois de qualquer jeito não é privado e desta maneira pode ser usado mais facilmente na herança
        self.ano = ano
        self._likes = 0     ### tendo o sinal de "_", fica claro ao dev que é privado

    @property # usado para retornar o elemento "privado". Outra diferença é que não é necessario usar os () para chama-lo.
    def nome(self):
        return self._nome

    @nome.setter # setter é o método para alterar algum atributo, sem lançar o "_", por exemplo corrigir o nome do filme/série
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


    @property # como foi protegido(simbólico) o likes para _likes, para não mudar todas as referências, cria-se o @property, que acerta o retorno.
    def likes(self):
        return self._likes

    def dar_like(self):  # lembrar que só vale dentro da classe, ou suas filhas
        self._likes += 1

    def __str__(self): ## definição pythonica para representar uma saída str
        return f'{self._nome} - {self.ano} - {self.likes}'


class Filme(Programa): ### puxa a classe mãe (Programa)
    def __init__(self, nome, ano, duracao): #puxa os atributos da classe mãe, adicionando algo personalizado para a classe (duração)
        super().__init__(nome, ano) ### pega os dados da classe mãe nome e ano
        self.duracao = duracao   # item personalizado

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} minutos - Likes: {self.likes}'


class Serie(Programa):  ###puxa a classe mãe (Programa)
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - Likes: {self.likes}'

class Playlist(list): # list é uma built-in
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

    def tamanho(self):
        return len(self.programas)

################ testes para rodar o programa VICENTE
# harry1 = Filme('Harry Potter(1) e a Pedra Filosofal', 2001, 159)
# harry2 = Filme('Harry Potter(2) e a Câmara Secreta', 2002, 150)
# harry3 = Filme('Harry Potter(3) e o Prisioneiro de Azkaban', 2004, 140)
# harry4 = Filme('Harry Potter(4) e o Cálice de Fogo', 2005, 155)
# harry5 = Filme('Harry Potter(5) e a Ordem da Fênix', 2007, 138)
# harry6 = Filme('Harry Potter(6) e o Enigma do Príncipe', 2009, 152)
# harry7 = Filme('Harry Potter(7) e as Relíquias da Morte: parte 1', 2010, 145)
# harry8 = Filme('Harry Potter(8) e as Relíquias da Morte: parte 2', 2021, 130)

############################

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

