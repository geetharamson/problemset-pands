# python collatz .py
# input a positive integer
#https://stackoverflow.com/questions/33324432/collatz-sequence-python-3
print("This is The Collatz Sequence")
num = int (input ("Enter a number: ") )


def collatz(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)


