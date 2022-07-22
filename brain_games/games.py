from random import randint, choice
from typing import Tuple
import math


def brain_even() -> Tuple:
    """Guess the number: is it even or not"""
    generated_number = randint(0, 100)
    answer = ["yes", "no"][generated_number % 2]
    question = generated_number
    return question, answer


def calculator() -> Tuple:
    """
    Generates two random numbers and ask a question
    in one of three categories: num1 {sub, mul or add} num2
    """
    num1, num2 = randint(0, 100), randint(0, 100)
    ACTIONS = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
    }
    action = choice(["+", "-", "*"])
    answer = ACTIONS[action](num1, num2)
    question = f"{num1} {action} {num2}"
    return question, answer


def gcd() -> Tuple:
    """Generates two random numbers for great common divisor question"""
    while True:
        num1, num2 = randint(0, 100), randint(0, 100)
        answer = math.gcd(num1, num2)
        question = f"{num1} {num2}"
        if answer != 1 and num1 != num2:
            return question, answer


def progression():
    a0 = randint(1, 13)  # first term
    d = randint(2, 6)  # common difference
    n = randint(5, 10)  # lenth of sequence
    prog = [a0 + d * i for i in range(n)]
    random_symbol = str(choice(prog))
    prog = " ".join(map(str, prog))
    question = prog.replace(random_symbol, "..", 1)
    answer = random_symbol
    return question, answer
