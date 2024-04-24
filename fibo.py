def recursive_nth_fibo(n):
    z = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)


def main():
    n = int(input("Zadaj pocet prvkov Fibonnaciho postupnosti: "))
    # seq = []
    # for num in range(n):
    #     seq.append(recursive_nth_fibo(num))
    seq = [recursive_nth_fibo(num) for num in range(n)]
    print(seq)

if __name__ == "__main__":
    main()
