# Calculadora em Python
OPRC = int(input('''*********CALCULADORA EM PYTHON*********


Selecione o número correspondente à operação desejada:


1 - Soma
2 - Subtração
3 - Mutiplicação
4 - Divisão

Digite sua opção(1/2/3/4):'''))

#Soma
if OPRC == 1:
    RESULT = lambda x,y : x + y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Subtração    
elif OPRC == 2:
    RESULT = lambda x,y : x - y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Multiplicação    
elif OPRC == 3:
    RESULT = lambda x,y : x * y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Divisão    
elif OPRC == 4:
    RESULT = lambda x,y : x % y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Número Inválido    
else: print('Operação Invalida')