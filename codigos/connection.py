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
  print(id(conn))

  conn2 = Connection()
  conn2.driver = "nosql"
  print(id(conn2))

  print(conn.driver)

  # conn.execute("Select * from...")


class SiteConfiguration:
  """
  titulo, subtitulo, email, count
  """
  pass