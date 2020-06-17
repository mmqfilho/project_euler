'''
https://projecteuler.net/problem=2

Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
soma, a, b = 0, 1, 2
while b <= 4_000_000:
    a, b = b, a + b
    if a % 2 == 0:
        soma += a
print(f'A soma dos termos pares menores que 4 milhoes é {soma}')
