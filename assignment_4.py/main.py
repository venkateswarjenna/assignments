# main.py

import venky_program as mp

menu = {
    1: mp.armstrong_number,
    2: mp.swap_numbers,
    3: mp.count_vowels,
    4: mp.gcd_two_numbers,
    5: mp.reverse_number,
    6: mp.sum_of_digits,
    7: mp.count_words,
    8: mp.title_case,
    9: mp.factorial_number,
    10: mp.fibonacci_series,
    11: mp.palindrome_string,
    12: mp.prime_check,
    13: mp.decimal_to_binary,
    14: mp.max_in_list,
    15: mp.custom_sort
}

while True:
    print("\n------ FUNCTION MENU ------")
    for num, func in menu.items():
        print(f"{num}. {func.__name__.replace('_', ' ').title()}")
    print("0. Exit")
    print("----------------------------")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Invalid input! Enter a number.")
        continue
    
    if choice == 0:
        print("👋 Exiting... Goodbye!")
        break
    elif choice in menu:
        print("\n" + "="*50)
        menu[choice]()
        print("="*50)
    else:
        print("❌ Invalid choice! Please try again.")
