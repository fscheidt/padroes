# Definir uma interface que representa as
# possibilidades de pagamentos (formas de pgto)
class PagamentoStrategy:
  def pagar(valor):
    pass

class CartaoStrategy(PagamentoStrategy):
  def __init__(self, nome, numero, cvc, data_val):
    self.nome = nome
    self.numero = numero
    self.cvc = cvc 
    self.data_val = data_val
  # pagar()....

# existe uma classe concreta de pagamento PixStrategy
class PixStrategy(PagamentoStrategy):
  def __init__(self, chave_origem, chave_dest=None):
    self.chave = chave_origem
    self.chave_dest = chave_dest
  def pagar(self, valor):
    # aqui vai a logica de pagamento por pix ...
    print(f"pagamento por pix no valor de {valor} "+
          f"com a chave {self.chave}")

# existe um contexto, que representa a preferencia
# por uma forma de pagamento.
class Context:
  def realiza_pagamento(self, strategy, valor):
    strategy.pagar(valor)

if __name__ == "__main__":
  # 1. Usuario escolhe pagar com PIX
  pix = PixStrategy("45-848389992")

  # 2. Passar para o Context processar o pagamento
  context = Context()
  context.realiza_pagamento(pix, 430)

  # 3. Implementa
  # boleto = BoletoStrategy()
  # desconto de 10%, e precisa do codigo de barras
  # context.realiza_pagamento(boleto, 300)

  # 4. Implementar o CartaoStrategy
  # acrescenta +5%
  