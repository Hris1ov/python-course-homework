from transaction import Transaction
from transaction_manager import TransactionManager
from utils import validate_float, validate_string
from datetime import datetime

def main():
    """
    Основен интерфейс за взаимодействие с потребителя чрез меню.
    """
    manager = TransactionManager()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Добави транзакция")
        print("2. Покажи всички транзакции")
        print("3. Изтрий транзакция")
        print("4. Изход")
        choice = input("Избор: ")

        if choice == "1":
            amount = validate_float("Сума (положителна за приход, отрицателна за разход): ")
            date = input("Дата (ГГГГ-ММ-ДД ЧЧ:ММ:СС) [остави празно за сега]: ")
            if not date:
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            category = validate_string("Категория: ")
            method = validate_string("Метод на плащане: ")
            note = input("Бележка: ")
            tags = input("Тагове (разделени със запетая): ").split(",") if input("Искаш ли тагове (д/н)? ").lower() == "д" else []
            t = Transaction(amount, date, category, method, note, tags)
            manager.add_transaction(t)
            print("✔ Транзакцията е добавена.")

        elif choice == "2":
            print("\n--- Списък с транзакции ---")
            for t in manager.list_transactions():
                print(f"{t.date} | {t.amount} | {t.category} | {t.method} | {t.note} | Tags: {', '.join(t.tags)}")

        elif choice == "3":
            tid = validate_string("Въведи ID на транзакцията за изтриване: ")
            manager.delete_transaction(tid)
            print("🗑 Транзакцията е изтрита.")

        elif choice == "4":
            print("Изход...")
            break
        else:
            print("Невалиден избор.")

if __name__ == "__main__":
    main()
