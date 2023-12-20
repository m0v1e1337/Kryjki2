import pandas as pd
import matplotlib.pyplot as plt

# Конвертация процентов во float
def convert_percentage(value):
    without_percentage = float(value.strip('%'))
    return without_percentage

# Загрузить датасет из файла
dataset = pd.read_csv(r'C:\Users\Dmitrii Tihonov\PycharmProjects\Kryjki\.venv\Lib\Dota2 Heroes by MMR Bracket.csv')

# Применить конвертацию процентов в датасете
dataset['(>5K MMR) WinRate(%)'] = dataset['(>5K MMR) WinRate(%)'].apply(convert_percentage)
dataset['(>5K MMR) PickRate(%)'] = dataset['(>5K MMR) PickRate(%)'].apply(convert_percentage)

# Линейный график
heroes = dataset['Heroes'].head(10)

plt.plot(heroes, dataset['(<2K MMR) PickRate(%)'].head(10), '-o', label='(<2K MMR) PickRate(%)')
plt.plot(heroes, dataset['(<2K MMR) WinRate(%)'].head(10), '-o', label='(<2K MMR) WinRate(%)')
plt.xlabel('Герои')
plt.ylabel('Значения')
plt.title('Линейные графики')
plt.legend()
plt.show()


# Столбчатая диаграмма
plt.bar(heroes, dataset['(2K-3K MMR) PickRate(%)'].head(10), label='(2K-3K MMR) PickRate(%) 5')
plt.bar(heroes, dataset['(3K-4K MMR) PickRate(%)'].head(10), label='(3K-4K MMR) PickRate(%) 7')
plt.bar(heroes, dataset['(4K-5K MMR) PickRate(%)'].head(10), label='(4K-5K MMR) PickRate(%) 9')
plt.xlabel('Герои')
plt.ylabel('Значения')
plt.title('Столбчатые диаграммы')
plt.legend()
plt.show()

# Круговая диаграмма
labels = dataset['(>5K MMR) WinRate(%)'].head(5)
sizes = dataset['(>5K MMR) PickRate(%)'].head(5)

plt.pie(sizes, labels=labels, autopct="1.1", startangle=90)
plt.title('Круговая диаграмма')
plt.axis('equal')
plt.show()

# Диаграмма рассеяния
plt.scatter(dataset['Heroes'].head(100), dataset['(>2K MMR) KDA Ratio'].head(100))
plt.xlabel('Герои')
plt.ylabel('(>2K MMR) KDA Ratio')
plt.title('Диаграмма рассеяния')
plt.xlim(0, 10)  # Ограничение значений по оси X
plt.ylim(0, 10)  # Ограничение значений по оси Y
plt.show()

# Гистограмма
plt.hist(dataset['(>2K MMR) Avg Match'].head(100), bins=10, edgecolor='black')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.xlim(0, 30)  # Ограничение значений по оси X
plt.ylim(0, 50)  # Ограничение значений по оси Y
plt.grid()
plt.show()
