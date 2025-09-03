from context import select_strategy

# =======================================
# [3] - CLIENTE 
#       pede ao contexto por uma estrategia
#       desconhece as classes concretas

if __name__ == "__main__":
    """ Runtime code """
   
    strategy = select_strategy()  # contexto
    password = input("Digite a senha: ")
    hashed_password = strategy.hash(password)
    print(hashed_password)

