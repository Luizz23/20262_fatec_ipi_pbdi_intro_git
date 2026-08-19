from calculadora import *

opcao = input(("Escolha a opção do menu:"))

def menu (opcao):
    if opcao == "1":
         return print(f'{3} +  {5} = {soma(3,5)}')
    if opcao == "2":
        return print(f'{2} - {1} = {subtrair(2,1)}')