from rich import print # pip install rich
from context import HashContext

def select_strategy():
    """ 
    Helper function - read user choice
    """
    print("-"*40)
    print("Algoritmos Hash disponiveis")
    print("-"*40)
    print("""
    1 - md5
    2 - sha1
    """)
    choice = int(input("Escolha a opção: "))
    # obs: essa logica poderia ser encapsulada numa factory
    # TODO: mover para factory
    from strategies import MD5Strategy, SHA1Strategy
    if choice==1: 
        strategy=MD5Strategy()
    elif choice==2:
        strategy=SHA1Strategy()
    else:
        raise ValueError("invalid choice")
    return strategy

# =======================================
# CLASSE CLIENTE

if __name__ == "__main__":
    """ Runtime CLIENT """

    strategy = select_strategy()
    password = input("Digite a senha: ")

    context = HashContext(strategy)
    hpass = context.hash(password)
    print(f"\n[cyan]{hpass}[/]\n")
    print("━"*40)

    # print(encrypt_sha1(password))
    # print(encrypt_md5(password))

    # context = ...
    # hpass = ...
