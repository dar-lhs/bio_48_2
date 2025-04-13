import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.datasets import cancer

class ScatterPlotFromStatsmodels:
    def __init__(self):
        # Загрузка данных
        self.df = cancer.load_pandas().data

    def classify_column(self, column: str, bins: int = 3, labels=None):
        if labels is None:
            labels = [f"Группа {i+1}" for i in range(bins)]
        self.df['class'] = pd.cut(self.df[column], bins=bins, labels=labels)

    def plot(self, x_col: str, y_col: str, title: str = "Диаграмма рассеяния"):
        plt.figure(figsize=(8, 6))
        for cls in self.df['class'].unique():
            subset = self.df[self.df['class'] == cls]
            plt.scatter(
                subset[x_col],
                subset[y_col],
                label=str(cls)
            )
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()

# Пример
plotter = ScatterPlotFromStatsmodels()
plotter.classify_column('population', bins=3, labels=['Малые', 'Средние', 'Большие'])
plotter.plot('cancer', 'population', title='Cancer vs Population')
