# my_programs.py

def armstrong_number():
    print("🧠 Program: Armstrong Number")
    print("""
def is_armstrong(num):
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    return total == num
""")
    print("🧪 Test Case 1: is_armstrong(153) → True")
    print("🧪 Test Case 2: is_armstrong(123) → False")
    print("📝 Explanation: Armstrong number = sum of its digits raised to power of number of digits.")

def swap_numbers():
    print("🧠 Program: Swap Two Numbers")
    print("""
def swap(a, b):
    a, b = b, a
    return a, b
""")
    print("🧪 Test Case 1: swap(10, 20) → (20, 10)")
    print("🧪 Test Case 2: swap(-5, 3) → (3, -5)")
    print("📝 Explanation: Uses tuple unpacking to swap without a temp variable.")

def count_vowels():
    print("🧠 Program: Count Vowels in String")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
""")
    print("🧪 Test Case 1: count_vowels('hello') → 2")
    print("🧪 Test Case 2: count_vowels('PYTHON') → 1")
    print("📝 Explanation: Checks each character if it’s in vowel list.")

def gcd_two_numbers():
    print("🧠 Program: GCD of Two Numbers")
    print("""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
""")
    print("🧪 Test Case 1: gcd(54, 24) → 6")
    print("🧪 Test Case 2: gcd(100, 80) → 20")
    print("📝 Explanation: Uses Euclidean algorithm to find greatest common divisor.")

def reverse_number():
    print("🧠 Program: Reverse a Number")
    print("""
def reverse_num(n):
    return int(str(n)[::-1])
""")
    print("🧪 Test Case 1: reverse_num(1234) → 4321")
    print("🧪 Test Case 2: reverse_num(560) → 65")
    print("📝 Explanation: Converts number to string, reverses it, then back to int.")

def sum_of_digits():
    print("🧠 Program: Sum of Digits")
    print("""
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
""")
    print("🧪 Test Case 1: sum_digits(123) → 6")
    print("🧪 Test Case 2: sum_digits(999) → 27")
    print("📝 Explanation: Converts number to string, sums integer value of digits.")

def count_words():
    print("🧠 Program: Count Words in a Sentence")
    print("""
def count_words(sentence):
    return len(sentence.split())
""")
    print("🧪 Test Case 1: count_words('Hello world') → 2")
    print("🧪 Test Case 2: count_words('Python is awesome') → 3")
    print("📝 Explanation: Splits sentence by spaces and counts words.")

def title_case():
    print("🧠 Program: Convert String to Title Case")
    print("""
def to_title_case(s):
    return s.title()
""")
    print("🧪 Test Case 1: to_title_case('hello world') → 'Hello World'")
    print("🧪 Test Case 2: to_title_case('PYTHON language') → 'Python Language'")
    print("📝 Explanation: Uses built-in title() method.")

def factorial_number():
    print("🧠 Program: Factorial of a Number")
    print("""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
""")
    print("🧪 Test Case 1: factorial(5) → 120")
    print("🧪 Test Case 2: factorial(0) → 1")
    print("📝 Explanation: Multiplies numbers from 1 to n.")

def fibonacci_series():
    print("🧠 Program: Fibonacci Series")
    print("""
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
""")
    print("🧪 Test Case 1: fibonacci(5) → [0, 1, 1, 2, 3]")
    print("🧪 Test Case 2: fibonacci(1) → [0]")
    print("📝 Explanation: Adds last two elements to generate next term.")

def palindrome_string():
    print("🧠 Program: Palindrome String")
    print("""
def is_palindrome(s):
    return s == s[::-1]
""")
    print("🧪 Test Case 1: is_palindrome('madam') → True")
    print("🧪 Test Case 2: is_palindrome('hello') → False")
    print("📝 Explanation: Checks if string reads same forwards and backwards.")

def prime_check():
    print("🧠 Program: Check Prime Number")
    print("""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
""")
    print("🧪 Test Case 1: is_prime(7) → True")
    print("🧪 Test Case 2: is_prime(10) → False")
    print("📝 Explanation: Checks divisibility up to square root.")

def decimal_to_binary():
    print("🧠 Program: Convert Decimal to Binary")
    print("""
def decimal_to_bin(n):
    return bin(n).replace('0b', '')
""")
    print("🧪 Test Case 1: decimal_to_bin(5) → '101'")
    print("🧪 Test Case 2: decimal_to_bin(10) → '1010'")
    print("📝 Explanation: Uses Python’s built-in bin() function.")

def max_in_list():
    print("🧠 Program: Find Maximum in a List")
    print("""
def max_value(lst):
    return max(lst)
""")
    print("🧪 Test Case 1: max_value([1, 3, 2]) → 3")
    print("🧪 Test Case 2: max_value([-1, -5, -3]) → -1")
    print("📝 Explanation: Uses Python’s max() to find largest element.")

def custom_sort():
    print("🧠 Program: Custom Sort (by Length)")
    print("""
def sort_by_length(lst):
    return sorted(lst, key=len)
""")
    print("🧪 Test Case 1: sort_by_length(['apple', 'kiwi', 'banana']) → ['kiwi', 'apple', 'banana']")
    print("🧪 Test Case 2: sort_by_length(['aa', 'b', 'ccc']) → ['b', 'aa', 'ccc']")
    print("📝 Explanation: Sorts list by string length using sorted() with key parameter.")
