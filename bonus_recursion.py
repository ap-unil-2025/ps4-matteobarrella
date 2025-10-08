
"""
Bonus Problem: Introduction to Recursion
Learn about recursive functions - functions that call themselves!
"""
from typing import List, Any

def factorial(n: int) -> int:
    """Calculate factorial of n using recursion."""
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def countdown(n: int) -> None:
    """Print numbers from n down to 1 using recursion, then 'Blastoff!'."""
    if n <= 0:
        print("Blastoff!")
        return
    print(n)
    countdown(n - 1)

def sum_list(numbers: List[float]) -> float:
    """Calculate sum of list using recursion."""
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

def fibonacci(n: int) -> int:
    """Calculate nth Fibonacci number using recursion (0-indexed)."""
    if n < 0:
        raise ValueError("fibonacci is undefined for negative indices")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def power(base: float, exponent: int) -> float:
    """Calculate base^exponent using recursion (exponent >= 0)."""
    if exponent < 0:
        raise ValueError("exponent must be non-negative for this implementation")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

def reverse_string(text: str) -> str:
    """Reverse a string using recursion."""
    if len(text) <= 1:
        return text
    return text[-1] + reverse_string(text[:-1])

def count_down_list(n: int) -> list:
    """Create a list of numbers from n down to 1 using recursion."""
    if n <= 0:
        return []
    return [n] + count_down_list(n - 1)

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Flatten a nested list using recursion."""
    result: List[Any] = [] #pylint: disable=redefined-outer-name
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


# Test cases
if __name__ == "__main__":
    print("Testing Recursive Functions...")
    print("-" * 50)

    # Test 1: factorial
    print("Test 1: factorial")
    print(f"5! = {factorial(5)}")
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(3) == 6
    print("✓ Passed\n")

    # Test 2: countdown
    print("Test 2: countdown")
    countdown(5)
    print("✓ Passed\n")

    # Test 3: sum_list
    print("Test 3: sum_list")
    result = sum_list([1, 2, 3, 4, 5])
    print(f"Sum of [1, 2, 3, 4, 5] = {result}")
    assert result == 15
    assert sum_list([]) == 0
    print("✓ Passed\n")

    # Test 4: fibonacci
    print("Test 4: fibonacci")
    fib_sequence = [fibonacci(i) for i in range(7)]
    print(f"First 7 Fibonacci numbers: {fib_sequence}")
    assert fib_sequence == [0, 1, 1, 2, 3, 5, 8]
    print("✓ Passed\n")

    # Test 5: power
    print("Test 5: power")
    print(f"2^5 = {power(2, 5)}")
    assert power(2, 5) == 32
    assert power(3, 3) == 27
    assert power(10, 0) == 1
    print("✓ Passed\n")

    # Test 6: reverse_string
    print("Test 6: reverse_string")
    result = reverse_string("hello")
    print(f"Reverse of 'hello' = '{result}'")
    assert result == "olleh"
    assert reverse_string("python") == "nohtyp"
    print("✓ Passed\n")

    # Test 7: count_down_list
    print("Test 7: count_down_list")
    result = count_down_list(5)
    print(f"Countdown list from 5: {result}")
    assert result == [5, 4, 3, 2, 1]
    print("✓ Passed\n")

    # Test 8: flatten_list
    print("Test 8: flatten_list")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    result = flatten_list(nested)
    print(f"Flattened {nested} = {result}")
    assert result == [1, 2, 3, 4, 5, 6, 7]
    print("✓ Passed\n")

    print("=" * 50)
    print("All recursion tests passed!")
    print("\nRecursion Key Concepts:")
    print("1. Every recursive function needs a BASE CASE to stop")
    print("2. Each recursive call should work on a SMALLER problem")
    print("3. Recursion uses the call stack (can cause stack overflow if too deep)")
    print("4. Some problems are naturally recursive (trees, nested structures)")
