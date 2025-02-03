import sys
import os

def main():
    # Receber o valor passado pela GitHub Action
    entrada = sys.argv[1]
    print(f'Recebi a entrada: {entrada}')
    nome = os.getenv('NOME')
    print(f'O nome dele é {nome}')

if __name__ == "__main__":
    main()