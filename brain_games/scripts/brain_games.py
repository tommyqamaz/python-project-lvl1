#!/usr/bin/env python
import prompt


def get_name():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def main():
    print("Welcome to the Brain Games!")
    get_name()


if __name__ == "__main__":
    main()
