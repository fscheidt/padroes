from context import select_strategy

# =======================================
# Classe cliente: obtem uma estrategia atraves do contexto

if __name__ == "__main__":
    """ Runtime code """
   
    strategy = select_strategy()  # contexto
    password = input("Digite a senha: ")
    hashed_password = strategy.hash(password)
    print(hashed_password)

