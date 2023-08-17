# Aula 03

## Singleton

Exemplo: Obter conexão com o banco de dados

```python

class Connection:
  _instance = None
  def __new__(cls, *args, **kwargs):      
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

```

## Strategy

Exemplo: Pagamento

```python
class PagamentoStrategy:
  pass

```
