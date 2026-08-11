import random
import string


def generate_random_string(length=8):
    letters = string.ascii_letters

    return ''.join(
        random.choice(letters)
        for _ in range(length)
    )


def generate_user_data():
    return {
        "name": generate_random_string(8),
        "email": (
            f"{generate_random_string(8)}"
            "@yandex.ru"
        ),
        "password": generate_random_string(10)
    }