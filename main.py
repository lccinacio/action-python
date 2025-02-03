import sys
import os

def main():
    # Receber o valor passado pela GitHub Action
    nome = os.getenv('NOME')
    sobrenome = os.getenv('SOBRENOME')
    cargo  = os.getenv('SOBRENOME')
    return f'Nome: {nome}, Sobrenome: {sobrenome}, cargo: {cargo}'

if __name__ == "__main__":
    main()