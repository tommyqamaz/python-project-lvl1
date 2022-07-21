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
    num1, num2 = randint(0, 55), randint(0, 55)
    answer = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, answer
