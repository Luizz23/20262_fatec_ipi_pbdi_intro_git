from calculadora import *

opcao = input(("Escolha a opção do menu:"))

def menu (opcao):
    if opcao == "1":
         return print(f'{3} +  {5} = {soma(3,5)}')
    if opcao == "2":
        return print(f'{2} - {1} = {subtrair(2,1)}')
    if opcao == "3":
       return print(f'{6} * {5} = {multiplicar(6,5)}')
    if opcao == "4":
       return print(f'{10} / {2} = {dividir(10,2)}')