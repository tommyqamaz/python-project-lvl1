from random import randint
from random import choice
from typing import Tuple


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
