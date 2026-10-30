from .cuenta_bancaria import CuentaBancaria
class CuentaCheque (CuentaBancaria):
    def __init__ (self,titular,cbu,saldo_inicial= 0 , costo_emision =0):
        super().__init__(titular,cbu,saldo_inicial)
        self.costo_emision = costo_emision

    def extraer (self,monto):
        total = monto  + self.costo_emision
        if total <= self.saldo:
             self.saldo -= total
             return True
        return False