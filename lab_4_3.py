# ex 3

from Bio import SeqIO


class GenBankProcessor:
    # Инициализация класса, который будет обрабатывать файл GenBank
    def __init__(self, input_path):
        self.input_path = input_path  # Путь к входному файлу (GenBank файл)
        self.records = []  # Список для хранения записей из файла

    # Метод для загрузки записей из файла GenBank
    def load_records(self):
        """Загружаем все записи из файла GenBank"""
        try:
            # Используем SeqIO для парсинга файла GenBank и сохраняем записи в список
            self.records = list(SeqIO.parse(self.input_path, "genbank"))
            print(
                f"Загружено {len(self.records)} записей."
            )  # Выводим количество загруженных записей
        except FileNotFoundError:
            # Если файл не найден, выводим ошибку и останавливаем выполнение
            print(f"Файл {self.input_path} не найден.")
            raise

    # Метод для трансляции всех CDS в белки и сохранения результата в файл
    def translate_cds(self, output_path="translations.txt"):
        """Находит и транслирует все CDS в белковые последовательности и сохраняет в файл"""
        # Открываем файл для записи
        with open(output_path, "w") as out_file:
            # Перебираем все записи, загруженные в self.records
            for record in self.records:
                # Проходим по всем features каждой записи
                for feature in record.features:
                    # Проверяем, является ли фича типом "CDS" и имеет ли она перевод
                    if feature.type == "CDS" and "translation" in feature.qualifiers:
                        # Извлекаем описание записи и её координаты CDS
                        description = record.description
                        location = feature.location
                        translation = feature.qualifiers["translation"][0]

                        # Записываем результаты в файл
                        out_file.write(
                            f"{record.id}: {description}\n"
                        )  # ID и описание записи
                        out_file.write(
                            f"Coding sequence location = {location} \n"
                        )  # Координаты CDS
                        out_file.write(
                            f"Translation =\n{translation}\n\n"
                        )  # Белковая последовательность

        # После того как всё сохранено, выводим сообщение о завершении
        print(f"Результаты трансляции сохранены в файл: {output_path}")


# Использование класса
processor = GenBankProcessor(
    "sequence.gb"
)  # Создаём экземпляр класса с указанием пути к файлу
processor.load_records()  # Загружаем записи из файла
processor.translate_cds()  # Выполняем трансляцию CDS и сохраняем результаты в файл
