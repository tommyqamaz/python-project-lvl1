from random import randint


def brain_even():
    generated_number = randint(0, 100)
    right_answer = ["yes", "no"][generated_number % 2]
    return generated_number, right_answer
