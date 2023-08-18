def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Cambia el valor de 'n' para obtener una secuencia más larga
n = 10
fibonacci_sequence = fibonacci(n)
print(f"Los primeros {n} números de la secuencia de Fibonacci son: {fibonacci_sequence}")
