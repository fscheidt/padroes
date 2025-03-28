# from rich import print
from strategies import encrypt_md5, encrypt_sha1

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
    if choice==1: 
        strategy=""
    elif choice==2:
        strategy=""
    else:
        raise ValueError("invalid choice")
    return strategy


if __name__ == "__main__":
    """ Runtime """

    strategy = select_strategy()
    password = input("Digite a senha: ")

    print(encrypt_sha1(password))
    print(encrypt_md5(password))

    # context = ...
    # hpass = ...
    # print(f"\n[cyan]{hpass}[/]\n")
    # print("━"*40)
