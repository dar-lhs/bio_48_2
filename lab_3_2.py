import pandas as pd  # Работа с табличными данными
import seaborn as sns  # Расширенные возможности визуализации
import matplotlib.pyplot as plt  # Для задания размеров фигуры и отображения графиков
from statsmodels.datasets import cancer  # Набор данных для примера

# Устанавливаем тему Seaborn для эстетики
sns.set_theme(style="darkgrid")


class ScatterPlotFromStatsmodels:
    def __init__(self):
        # Загрузка данных (DataFrame загружается из набора данных "cancer")
        self.df = cancer.load_pandas().data

    def classify_column(self, column: str, bins: int = 3, labels=None):
        """
        Классифицирует значения указанного столбца на заданное число групп (bins).
        Если метки (labels) не заданы, генерирует их автоматически.
        Результат записывается в новый столбец 'class'.
        """
        if labels is None:
            labels = [f"Группа {i+1}" for i in range(bins)]
        self.df["class"] = pd.cut(self.df[column], bins=bins, labels=labels)

    def plot(self, x_col: str, y_col: str, title: str = "Диаграмма рассеяния"):
        """
        Строит диаграмму рассеяния с использованием seaborn.
        Цвет и стиль точек зависят от категориальной переменной 'class'.
        """
        plt.figure(figsize=(8, 6))
        ax = sns.scatterplot(
            data=self.df,
            x=x_col,
            y=y_col,
            hue="class",  # разделение точек по классам
            style="class",  # различие по стилю маркеров для наглядности
            palette="deep",  # набор цветов для категорий
        )
        ax.set_title(title)
        plt.show()


# Пример

# Создаём экземпляр класса
plotter = ScatterPlotFromStatsmodels()

# Классифицируем столбец 'population' на 3 группы с пользовательскими метками
plotter.classify_column("population", bins=3, labels=["Малые", "Средние", "Большие"])

# Строим диаграмму рассеяния: по оси X — 'cancer', по оси Y — 'population'
plotter.plot("cancer", "population", title="Cancer vs Population")
