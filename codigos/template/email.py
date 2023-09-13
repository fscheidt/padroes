
"""
Metodo template
- define uma sequencia de passos
"""
from abc import ABC, abstractmethod

class Email(ABC):
  def enviar(self, from_user, to):
    """ 
    metodo template:
    - define a sequencia de passos para enviar um email
    """
    # 1) validacao
    self.validate(from_user) # <= Estatico
    self.validate(to)
    # 2) obter o conteudo do email
    self.get_content() # <= ABSTRATO
    # 3) anexar arquivos
    self.attach()
    # 4) enviar email
    self.send()

  def validate(self, email):
    print(f"parece valido {email}")

  @abstractmethod 
  def get_content(self): # hook 
    pass

  def attach(self):
    print("anexando arquivos")

  def send(self):
    print("enviando email")
    print("="*40)

class ProdutoEstoque(Email):
  def get_content(self):
    body = "<div>Informamos que o produto tal esta disponivel</div>"
    print(body)
    return body

class Pagamento(Email):
  def get_content(self):
    body = "<p>Pagamento recebido - pedido em processamento</p>"
    print(body)
    return body

def app(email: Email):
  email.enviar("abc@org.br","xyz@org.br")

if __name__ == "__main__":
  app(ProdutoEstoque())
  app(Pagamento())


"""
Implementar um esquema de autenticacao (aka Login)
- usuario fornece email e senha
- Definir os passos para autenticar:
  (1) verificar o login e senha no banco de dados; 
  (2) salvar em um arquivo de log o email do usuário; 
  (3) carrega preferências do usuário; 
  (4) obtem a pagina para redirecionamento.
    - index.html
    - error.html

"""








