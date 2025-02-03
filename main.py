import sys
import os

def main():
    # Receber o valor passado pela GitHub Action
    nome = os.getenv('NOME')
    return f'{nome}'

if __name__ == "__main__":
    main()