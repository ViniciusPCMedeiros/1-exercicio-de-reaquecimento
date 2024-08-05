def mult(a,b):
    if b == 0: return 0
    if b == 1:
        return a 
    return a + mult(a,b-1)



#S oma de dois números naturais, através de incrementos sucessivos (Ex.: 3 + 2 = + + (+ + + 1)).
def calcSoma(a, b):
    return calc_Soma(a)+calc_Soma(b)
    
    
def calc_Soma(a):
    if a == 0: 
        return 0
    

#1. Cálculo de 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
def calc_frac(n):
    if n == 1: return 1 
    return 1/n + calc_frac(n-1)


#1. Inversão de uma string.
def inverter_string(palavra):
    if len(palavra) == 1: return palavra 
    return inverter_string(palavra[1:]) + palavra[0]

#Verifique se uma palavra é palíndromo
def palindro(string):return True if string == inverter_string(string) else False
    # if string == inverter_string(string): return True
    # return False

print(palindro('aba'))
print(palindro('arroz'))





