from template import Pix, Bitcoin

# cliente
if __name__ == "__main__":

    pgto = Pix()
    pgto.realizar_pagamento(1000)

    print("="*40)
    pgto = Bitcoin()
    pgto.realizar_pagamento(1000) # desconto de 10%
