n = int(input('Informe um número: '))

def fib(n):
    if n <= 0: return 0
    elif n == 1: return 1
    return fib(n-1) + fib(n-2)

i = 0

while True:
    fibo = fib(i)
    if fibo == n: 
        print(f'O número {n} pertence a sequência de Fibonacci')
        break
    elif fibo > n: 
        print(f'O número {n} não pertence a sequência de Fibonacci') 
        break
    i += 1
