# ex 2

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


class GenBankProcessor:
    def __init__(self, input_path):
        self.input_path = input_path
        self.records = []

    def load_records(self):
        """Загружаем записи из GenBank-файла"""
        self.records = list(SeqIO.parse(self.input_path, "genbank"))

    def get_gc_sorted_records(self):
        """Сортирует записи по GC-составу"""
        gc_records = []
        for record in self.records:
            gc = gc_fraction(record.seq)  # Вычисляем GC-состав (в долях, от 0 до 1)
            gc_records.append((gc, record))  # Сохраняем кортеж (GC, запись)
        gc_sorted = sorted(
            gc_records, key=lambda x: x[0]
        )  # Сортируем список по значению GC-состава (по возрастанию)
        return gc_sorted

    def print_gc_sorted_sequences(self):
        """Вывод в формате как в приложении Б"""
        sorted_records = self.get_gc_sorted_records()
        for gc, record in sorted_records:
            print(f"{record.id}: {record.description}, GC = {gc}")


# Использование:
processor = GenBankProcessor("combined_file.gbk")
processor.load_records()
processor.print_gc_sorted_sequences()
