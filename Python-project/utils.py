def validate_float(prompt):
    """Изисква валидно число с плаваща запетая от потребителя."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Моля, въведи валидна сума.")

def validate_string(prompt):
    """Изисква не празен стринг от потребителя."""
    value = input(prompt).strip()
    return value if value else "Няма описание"