from calculadora import *

opcao = input(("Escolha a opção do menu:"))

def menu (opcao):
    if opcao == "1":
         return print(f'{3} +  {5} = {somar(3,5)}')