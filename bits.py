def NOT(valor):
    return (-Valor)

def AND(valor1,valor2):
    return (valor1 & valor2)

def OR(valor1,valor2):
    return (valor1 | valor2)

def OR(valor1,valor2):
    return (valor1^valor2)

def shiftleft(valor, num):
     return (val << num)

def shiftright(valor, num):
     return  (val >> num)

def bit(val, idx):
    mask = 1 <<  idx #all 0 except idx
    return bool (val & 1)