def run_quiz(questions):
    score = 0
    print(" Welcome to the Python Quiz Game!\n")

    for index, q in enumerate(questions, start=1):
        print(f"Question {index}: {q['question']}")
        for option in ['a', 'b', 'c', 'd']:
            print(f"{option}) {q['options'][option]}")
        user_ans = input("Your answer (a/b/c/d): ").lower()

        if user_ans == q['answer']:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct answer is '{q['answer']}'\n")

    print(f" Your Final Score: {score}/{len(questions)}")
    if score >= 15:
        print("🎉 Excellent job! You’re well-prepared!")
    elif score >= 10:
        print(" Good job! Keep practicing!")
    else:
        print(" Review your concepts and try again.")


questions = [
    {
        "question": "What is the output of: print(type([]))?",
        "options": {
            "a": "<class 'list'>",
            "b": "<class 'dict'>",
            "c": "<class 'set'>",
            "d": "<class 'tuple'>"
        },
        "answer": "a"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "a": "function",
            "b": "def",
            "c": "fun",
            "d": "define"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of 3 * '5'?",
        "options": {
            "a": "15",
            "b": "555",
            "c": "Error",
            "d": "None"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following is immutable?",
        "options": {
            "a": "list",
            "b": "dict",
            "c": "set",
            "d": "tuple"
        },
        "answer": "d"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": {
            "a": "//",
            "b": "<!--",
            "c": "#",
            "d": "**"
        },
        "answer": "c"
    },
    {
        "question": "What does len() do in Python?",
        "options": {
            "a": "Calculates size of int",
            "b": "Returns list length",
            "c": "Finds memory usage",
            "d": "Loops through list"
        },
        "answer": "b"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": {
            "a": ".pt",
            "b": ".python",
            "c": ".py",
            "d": ".pyt"
        },
        "answer": "c"
    },
    {
        "question": "Which of the following is used to import a module?",
        "options": {
            "a": "include",
            "b": "import",
            "c": "using",
            "d": "require"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of bool(0)?",
        "options": {
            "a": "True",
            "b": "False",
            "c": "0",
            "d": "None"
        },
        "answer": "b"
    },
    {
        "question": "What is used to define a block of code in Python?",
        "options": {
            "a": "Brackets {}",
            "b": "Parentheses ()",
            "c": "Indentation",
            "d": "Curly braces"
        },
        "answer": "c"
    },
    {
        "question": "What is the result of: 2 ** 3?",
        "options": {
            "a": "6",
            "b": "8",
            "c": "9",
            "d": "Error"
        },
        "answer": "b"
    },
    {
        "question": "Which one is a valid variable name?",
        "options": {
            "a": "2name",
            "b": "name_2",
            "c": "name-2",
            "d": "name 2"
        },
        "answer": "b"
    },
    {
        "question": "Which keyword is used for loops in Python?",
        "options": {
            "a": "repeat",
            "b": "loop",
            "c": "for",
            "d": "iterate"
        },
        "answer": "c"
    },
    {
        "question": "Which function is used to take input from user?",
        "options": {
            "a": "input()",
            "b": "get()",
            "c": "scan()",
            "d": "read()"
        },
        "answer": "a"
    },
    {
        "question": "What is the data type of: {'a': 1, 'b': 2}?",
        "options": {
            "a": "list",
            "b": "tuple",
            "c": "dict",
            "d": "set"
        },
        "answer": "c"
    },
    {
        "question": "What is the output of: type((10,))?",
        "options": {
            "a": "<class 'tuple'>",
            "b": "<class 'int'>",
            "c": "<class 'list'>",
            "d": "<class 'str'>"
        },
        "answer": "a"
    },
    {
        "question": "Which operator is used for equality checking?",
        "options": {
            "a": "=",
            "b": "==",
            "c": "!=",
            "d": "<>"
        },
        "answer": "b"
    },
    {
        "question": "What will be the output of: print('Hello'[::-1])?",
        "options": {
            "a": "Hello",
            "b": "olleH",
            "c": "Error",
            "d": "None"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following creates a list?",
        "options": {
            "a": "{}",
            "b": "()",
            "c": "[]",
            "d": "<>"
        },
        "answer": "c"
    },
    {
        "question": "What is the default return value of a function that doesn't return anything?",
        "options": {
            "a": "0",
            "b": "False",
            "c": "None",
            "d": "undefined"
        },
        "answer": "c"
    }
]

run_quiz(questions)
