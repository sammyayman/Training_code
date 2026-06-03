if __name__ == '__main__': 
    # This block runs only when the file is executed directly
    # Not when imported as a module
    print('__name__ equals __main__')
    
    # Example demonstrating the difference:
    print("\n--- Demonstrating __name__ ---")
    print(f"Current file's __name__: {__name__}")
    
    # When you import this file as a module, 
    # __name__ will be the module name, not '__main__'
    
    # Common use case: testing functions in the module
    # Example function:
    def greet(name):
        return f"Hello, {name}!"
    
    # Only run test code when executed directly
    result = greet("Python Learner")
    print(result)
    
    # Another example: main() function pattern
    def main():
        print("\n--- main() function executed ---")
        print("This is the entry point when running the script directly")
    
    main()
    
    # ===== MATH NUMBERS EXAMPLE =====
    print("\n--- Math Numbers Examples ---")
    
    # Math functions to test
    def square(x): return x ** 2
    def cube(x): return x ** 3
    def is_even(x): return x % 2 == 0
    def is_prime(n): 
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    # Test with numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Test square function
    print("Squares:", [square(x) for x in numbers])
    
    # Test cube function
    print("Cubes:", [cube(x) for x in numbers[:5]])
    
    # Filter even numbers
    evens = list(filter(is_even, numbers))
    print("Even numbers:", evens)
    
    # Filter prime numbers
    primes = list(filter(is_prime, numbers))
    print("Prime numbers:", primes)
    
    # Map and filter combined
    squares_of_evens = list(map(square, filter(is_even, numbers)))
    print("Squares of even numbers:", squares_of_evens)