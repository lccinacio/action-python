import sys


def main():
    # Receber o valor passado pela GitHub Action
    nome = sys.argv
    print(f'Nome dele é {nome}') 

if __name__ == "__main__":
    main()