import json

lista: list = ["sapato", 39, 10.38, True]
produto_01: dict= {
"nome":"sapato",
"quantidade":30,
"preco":10.38,
"quantidade": True
}
produto_02: dict = {
"nome":"televisao",
"quantidade":10,
"preco":70.38,
"disponibilidade": "False"
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)
