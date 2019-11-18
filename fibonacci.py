# fibonacci.py

def fib():
    fibs = [1, 2]

    q = 0
    w = 1
    for i in range(1,9):
        a = fibs[q]
        b = fibs[w]
        x = a + b
        fibs.append(x)
        q +=1
        w +=1

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
