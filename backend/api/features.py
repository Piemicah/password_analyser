import math


def extract_features(password):
    return [
        [
            len(password),
            sum(1 for c in password if c.isupper()),
            sum(1 for c in password if c.islower()),
            sum(1 for c in password if c.isdigit()),
            sum(1 for c in password if not c.isalnum()),
            calculate_entropy(password),
        ]
    ]


def calculate_entropy(password):
    unique_chars = set(password)
    length = len(password)

    alphabet_size = 0
    if any(char.islower() for char in unique_chars):
        alphabet_size += 26  # a-z
    if any(char.isupper() for char in unique_chars):
        alphabet_size += 26  # A-Z
    if any(char.isdigit() for char in unique_chars):
        alphabet_size += 10  # 0-9
    if any(not char.isalnum() for char in unique_chars):
        alphabet_size += 32  # Specials (aproximated)

    if alphabet_size > 0:
        entropy = length * math.log2(alphabet_size)
    else:
        entropy = 0

    return entropy
