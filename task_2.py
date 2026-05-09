import re

def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"

    for number in re.finditer(pattern, text):
        yield float(number.group())

def sum_profit(text: str, func):
    total = 0

    for number in func(text):
        total += number

    return total

text = "Загальний дохід працівника складається з декількох частин: 900.04 як основний дохід, доповнений додатковими надходженнями 18.54 і 678.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
