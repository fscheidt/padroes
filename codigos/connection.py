# Implementar o Singleton

class Connection:
  _instance = None
  def __init__(self):
    # print("__init__")
    self.driver = "mysql"
  def __new__(cls, *args, **kwargs):    
    # print("__new__")
    if cls._instance is None:
      # print("_if__new__")
      cls._instance = super().__new__(cls)
    return cls._instance

if __name__ == "__main__":
  conn = Connection()
  conn.driver = "sqlite"
  # id retorna o endereco de memoria
  print(id(conn)) 

  conn2 = Connection()
  conn2.driver = "nosql"
  print(id(conn2))
  # para validar o singleton id(conn) == id(conn2)
  print(id(conn) == id(conn2)) # True
  print(conn.driver)

  # conn.execute("Select * from...")


class SiteConfiguration:
  """
  titulo, subtitulo, email, count
  """
  def __init__(self):
    pass
  def __new__(cls):
    pass

