from typing import Callable, TypeVar
T = TypeVar("T")

class AuthenticateGoogleOAuth:
  def autenticate_user(email):
    # faz request para api ...
    print('autenticando google oAuth')
    return True
  
class AuthenticateGitHubToken:
  def autorize_access(secret):
    # request para api git
    print('autenticando github token')
    return True

class AdapterAuth:
  def __init__(self, obj: T, **methods: Callable):
    """ adiciona methods ao objeto """
    self.obj = obj
    self.__dict__.update(methods)

  def __getattr__(self, attr):
    """ All non-adapted calls are passed to the object. """
    return getattr(self.obj, attr)

if __name__ == "__main__":
  # opcoes de autenticacao disponiveis ao usuario
  google = AuthenticateGoogleOAuth()
  github = AuthenticateGitHubToken()

  # usuario seleciona o metodo
  method = "google"
  auth = None

  if method == "google":
    auth = AdapterAuth(google, login=google.autenticate_user)
  elif method == "github":
    auth = AdapterAuth(github, login=github.autorize_access)
  else:
    raise Exception("auth mode not recognize")
  
  auth.login()