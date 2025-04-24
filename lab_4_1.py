# ex 1

from Bio import SeqIO


class GenBankProcessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.records = []

    def load_records(self):
        """Считываем записи из файла GenBank"""
        try:
            self.records = list(SeqIO.parse(self.input_path, "genbank"))
            print(f"Загружено {len(self.records)} записей.")
        except FileNotFoundError:
            print(f"Файл {self.input_path} не найден.")
            raise

    def count_cds(self):
        """Считаем количество CDS во всех записях"""
        cds_count = 0
        for record in self.records:
            cds_count += sum(1 for feature in record.features if feature.type == "CDS")
        return cds_count

    def save_records(self):
        """Сохраняем записи в новый файл"""
        with open(self.output_path, "w") as out_handle:
            SeqIO.write(self.records, out_handle, "genbank")
        print(f"Сохранено в файл: {self.output_path}")


# Использование:
processor = GenBankProcessor("sequence.gb", "combined_file.gbk")
processor.load_records()
cds_total = processor.count_cds()
print(f"Общее количество CDS: {cds_total}")
processor.save_records()
