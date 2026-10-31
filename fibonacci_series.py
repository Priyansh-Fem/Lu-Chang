''' Fibonacci series generator

This script prompts the user for the number of terms and prints the
Fibonacci sequence up to that count.

You can run it with:
    python fibonacci_series.py
'''

def fibonacci(n: int) -> list[int]:
    """Return a list containing the first ``n`` Fibonacci numbers.

    The sequence starts with 0, 1, 1, 2, 3, ...
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def main() -> None:
    try:
        count_str = input("Enter the number of terms: ")
        count = int(count_str)
    except ValueError:
        print("Please enter a valid integer.")
        return

    series = fibonacci(count)
    print(", ".join(str(num) for num in series))


if __name__ == "__main__":
    main()

