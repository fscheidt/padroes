from rich import print # pip install rich
from context import HashContext, select_strategy

# =======================================
# CLIENT CLASS - usa uma estrategia 
# atraves do contexto

if __name__ == "__main__":
    """ Runtime CLIENT """

    strategy = select_strategy()
    password = input("Digite a senha: ")

    context = HashContext(strategy)
    hpass = context.hash(password)
    print(f"\n[cyan]{hpass}[/]\n")
    print("━"*40)
