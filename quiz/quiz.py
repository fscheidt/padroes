"""
Entrega Hoje:
1. Classes Python
- padrões a serem utilizados 
2. Arquivo json
"""
import json

# (1) modelagem classes no python de acordo com o json
class Pergunta:
    """
    "id": 2,
    "questao": "Qual montadora lançou o primeiro carro 100% elétrico fabricado no Brasil?",
    "opcoes": [  # builder
       { "Chevrolet", false}, 
       { "Nissan", true} , 
       "Volkswagen", "Renault"],
    "resposta": "Nissan",
    "nivel_dificuldade": "Médio", # strategy 
    "categoria": "Tecnologia"
    """
    def __init__():
        ...
        # delegar ao factory a criacao das instancias.

# (2) ideia: padrao usado para importar o quiz.json (singleton)
def load(): 
    ...
    # instanciar, criar objeto da classe Perguntas e outras
    # de acordo com o modelo de dados.

# (3) executar