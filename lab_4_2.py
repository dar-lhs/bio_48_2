# ex 2

from Bio import SeqIO 
from Bio.SeqUtils import gc_fraction # Импортируем функцию для вычисления GC-состава последовательности


class GenBankProcessor:
    # Конструктор класса, который будет обрабатывать файл GenBank
    def __init__(self, input_path):
        self.input_path = input_path  # Путь к входному файлу
        self.records = []  # Список для хранения всех записей из файла GenBank

    # Метод для загрузки записей из GenBank-файла
    def load_records(self):
        """Загружаем записи из GenBank-файла"""
        # Считываем все записи из файла с помощью SeqIO.parse
        self.records = list(SeqIO.parse(self.input_path, "genbank"))

    # Метод для сортировки записей по GC-составу
    def get_gc_sorted_records(self):
        """Сортирует записи по GC-составу"""
        gc_records = []  # Список для хранения кортежей (GC, запись)

        # Перебираем все записи в файле
        for record in self.records:
            gc = gc_fraction(
                record.seq
            )  # Вычисляем GC-состав для каждой последовательности
            gc_records.append(
                (gc, record)
            )  # Добавляем кортеж с GC-составом и самой записью

        # Сортируем список по значению GC-состава (по возрастанию)
        gc_sorted = sorted(gc_records, key=lambda x: x[0])
        return gc_sorted  # Возвращаем отсортированный список

    # Метод для вывода отсортированных последовательностей с их GC-составом
    def print_gc_sorted_sequences(self):
        """Вывод в формате как в приложении Б"""
        sorted_records = (
            self.get_gc_sorted_records()
        )  # Получаем отсортированный список записей по GC-составу

        # Перебираем отсортированные записи и выводим информацию о каждой
        for gc, record in sorted_records:
            print(
                f"{record.id}: {record.description}, GC = {gc}"
            )  # Выводим ID, описание и GC-состав


# Использование:
processor = GenBankProcessor(
    "combined_file.gbk"
)  # Создаём объект класса с указанием пути к файлу GenBank
processor.load_records()  # Загружаем записи из файла
processor.print_gc_sorted_sequences()  # Выводим отсортированные последовательности по GC-составу
