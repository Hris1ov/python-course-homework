import uuid
from datetime import datetime

class Transaction:
    """
    Представлява една финансова транзакция.
    """
    def __init__(self, amount, date, category, method, note="", tags=None):
        """
        Инициализира нова транзакция.

        :param amount: сума на транзакцията (положителна за приход, отрицателна за разход)
        :param date: дата и час на транзакцията (стринг или datetime)
        :param category: категория на разход/приход
        :param method: метод на плащане (напр. в брой, карта)
        :param note: допълнителна бележка
        :param tags: списък с тагове за по-добра организация
        """
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.date = date if isinstance(date, datetime) else datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        self.category = category
        self.method = method
        self.note = note
        self.tags = tags or []

    def to_dict(self):
        """Преобразува транзакцията до речник (за запис във файл)."""
        return {
            "id": self.id,
            "amount": self.amount,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "category": self.category,
            "method": self.method,
            "note": self.note,
            "tags": self.tags
        }

    @staticmethod
    def from_dict(data):
        """Създава Transaction от речник (при зареждане от файл)."""
        return Transaction(
            amount=data["amount"],
            date=data["date"],
            category=data["category"],
            method=data["method"],
            note=data.get("note", ""),
            tags=data.get("tags", [])
        )