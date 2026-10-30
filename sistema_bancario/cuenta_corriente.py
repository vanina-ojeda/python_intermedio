from .cuenta_bancaria import CuentaBancaria
class CuentaCorriente (CuentaBancaria):
   def __init__ (self, titular , cbu ,saldo_inicial = 0, limite_descubierto = 500):
     super().__init__(titular,cbu,saldo_inicial)
     self.limite_descubierto = limite_descubierto

   def extraer (self, monto):
        if monto <= self.saldo + self.limite_descubierto :
            return True
        self.saldo -= monto
        return False        