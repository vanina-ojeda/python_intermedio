from .cuenta_bancaria import CuentaBancaria
class CuentaAhorro (CuentaBancaria):
    def extraer (self,monto):
        if monto <=  self.saldo :
         self.saldo -= monto 
         return True

    def aplicar_interes (self,tasa=0.001):
    
      self.saldo += self.saldo * tasa 
