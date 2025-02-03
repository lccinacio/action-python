import sys

def main():
    # Receber o valor passado pela GitHub Action
    entrada = sys.argv[1]
    print(f'Recebi a entrada: {entrada}')

if __name__ == "__main__":
    main()