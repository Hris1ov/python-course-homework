import json
import os
from transaction import Transaction

class TransactionManager:
    """
    Клас за управление на множество транзакции.
    """
    def __init__(self, filename="data/transactions.json"):
        self.filename = filename
        self.transactions = []
        self.load()

    def add_transaction(self, transaction):
        """Добавя нова транзакция."""
        self.transactions.append(transaction)
        self.save()

    def delete_transaction(self, transaction_id):
        """Изтрива транзакция по ID."""
        self.transactions = [t for t in self.transactions if t.id != transaction_id]
        self.save()

    def list_transactions(self):
        """Връща списък с всички транзакции."""
        return self.transactions

    def save(self):
        """Запазва транзакциите във файл (JSON)."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.transactions], f, ensure_ascii=False, indent=2)

    def load(self):
        """Зарежда транзакциите от файл (ако съществува)."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(item) for item in data]