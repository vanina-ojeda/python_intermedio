from abc import ABC , abstractmethod
class CuentaBancaria (ABC):
    def __init__ (self ,titular , cbu , saldo_inicial = 0):
        self._titular = titular
        self._cbu = cbu
        self._saldo = saldo_inicial 

    @property
    def cbu (self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter 
    def saldo (self , valor):
        if valor <= 0  :
           raise ValueError ("el valor a ingresar debe ser mayor a cero")
        self._saldo = valor 
           
    def depositar (self, monto):
        if  monto <= 0 :
            raise ValueError ("el monto a depositar debe ser mayor a cero")
        self.saldo += monto 

    def __str__(self):
        return f"[tipodecuenta] titular: {self._titular} | cbu: {self._cbu} | saldo: ${self._saldo:.2f}"

    @abstractmethod
    def extraer (self, monto):
        pass