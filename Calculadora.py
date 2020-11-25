# Calculadora em Python
operacao = int(input('''*********CALCULADORA EM PYTHON*********


Selecione o número correspondente à operação desejada:


1 - Soma
2 - Subtração
3 - Mutiplicação
4 - Divisão

Digite sua opção(1/2/3/4):'''))

#Soma
if operacao == 1:
    RESULT = lambda x,y : x + y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Subtração    
elif operacao == 2:
    RESULT = lambda x,y : x - y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Multiplicação    
elif operacao == 3:
    RESULT = lambda x,y : x * y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Divisão    
elif operacao == 4:
    RESULT = lambda x,y : x / y
    x = int(input('Digite seu primeiro número:'))
    y = int(input('Digite seu segundo número:'))
    print(RESULT(x,y))

#Número Inválido    
else: print('Operação Invalida')