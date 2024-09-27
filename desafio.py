#Crie um dicionario para armazenar infomações de um livro,
#incluindo titulo, autor de publicação, imprima cada informação


from typing import Dict, Any

livro01: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 2005
}
livro_02: Dict[str, Any] = {
    "Titulo": "Game of Thrones 2",
    "Autor": "George R. R. Martin",
    "Ano": 2007
}
# lista_de_elementos = livro.items()
# for elemento in lista_de_elementos:
#     print(elemento)

lista_de_livros = []

lista_de_livros.append(livro01)
lista_de_livros.append(livro_02)

#print(lista_de_livros)

# DESSA FORMA PODE SER UTIIZADO PARA API TAMBÉM

lista_de_livros_usando_dict: dict = {
    "livro_01":{"Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 2005},

   "livro_02": {"Titulo": "Game of Thrones 2",
    "Autor": "George R. R. Martin",
    "Ano": 2007}
}

print(lista_de_livros_usando_dict["livro_01"]["Autor"])