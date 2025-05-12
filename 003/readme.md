# Aula 3 - Métodos de Instância

## CONCEITO GERAL DE MÉTODOS DE INSTÂNCIA
**Métodos de instância** são métodos associados a uma instância específica de uma classe e podem acessar e modificar os atributos (variáveis) de instância da classe. Os métodos de instância também são os tipos de métodos mais comuns em classes.

## MÉTODOS DE INSTÂNCIA
### Métodos de Instância: Operando nos dados de uma instância ``(self)``
**Propósito**: Eles são projetados para operar nos dados específicos de uma instância (objeto) da classe. Isso significa que eles podem acessar e modificar os atributos do objeto.

**Parâmetro** ```self```: O primeiro parâmetro de um método de instância é sempre ``self``. Quando você chama um método em um objeto (por exemplo, ```objeto.metodo()```), o próprio objeto é implicitamente passado como o argumento para o parâmetro ```self```. É através de self que o método pode acessar os atributos (```self.atributo```) e outros métodos (```self.outro_metodo()```) daquela instância específica.

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente.")

# Criando instâncias da classe ContaBancaria
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob")

# Chamando métodos de instância
conta1.depositar(500)   # 'self' é 'conta1'
conta2.sacar(100)     # 'self' é 'conta2' (saldo inicial é 0)
```
No exemplo acima, ```depositar``` e ```sacar``` são métodos de instância porque operam no ```saldo``` específico de cada objeto ```ContaBancaria``` (```conta1``` e ```conta2```).