def main():
    n = int(input("Digite a altura que você quer a piramide: "))# n é a altura da pirâmide

    for i in range(n):
        for j in range(n-i-1):
            print(" ", end = "")
        print("#" * (i+1), end = "")
        print("  ", end = "")
        print("#" * (i+1), end = "")
        print()
main()