import re

def extract_numbers(text: str) -> list[int]:
    """Extracts all numbers from a given text and returns them as a list of integers."""
    return [int(num) for num in re.findall(r'\d+', text)]



def extract_signs(text: str) -> list[int]:
    return [int(num) for num in re.findall(r'[+-]?\d+', text)]


def average_nums(vals: list[int]) -> float:
    return sum(vals) / len(vals) if vals else 0.0


if __name__ == "__main__":
    sample_text = "The year is 2024 and the temperature is 30 degrees."
    numbers = extract_numbers(sample_text)
    print(numbers)  # Output: [2024, 30]

    sample_text_with_signs = "The temperature is -5 degrees and the pressure is +1013 hPa."
    signs = extract_signs(sample_text_with_signs)
    print(signs)  # Output: [-5, 1013]

    average = average_nums(numbers)
    print(average)  # Output: 1027.0

