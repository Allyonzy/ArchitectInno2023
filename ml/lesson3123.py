

import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder


# Функция для создания DataFrame и записи в CSV файл
def createFrame(filename='data.csv'):
    data = {
        'price': [150000, 200000, 120000, 140000, 180000] * 100,
        'region': ['A', 'B', 'A', 'C', 'B'] * 100,
        'rooms': [2, 3, 2, 1, 3] * 100,
        'floor': [5, 7, 3, 2, 6] * 100,
        'toilet_with_bathroom': [False, True, False, False, True] * 100,
        'kitchen_with_living_room': [True, True, False, True, False] * 100,
        'category': ['стандарт', 'улучшенный', 'стандарт', 'стандарт', 'улучшенный'] * 100
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


# X_new теперь содержит только 2 лучших признака

# Пример использования функций
if __name__ == '__main__':
    # Создание DataFrame и запись в CSV файл
    createFrame()
    # Загрузка данных из CSV файла
    filename = 'data.csv'
    df = pd.read_csv(filename)

    # Определение целевой переменной и признаков
    X = df.drop('category', axis=1)  # Убираем целевую переменную
    y = df['category']

    # Создаем экземпляр LabelEncoder
    label_encoder = LabelEncoder()

    # Преобразовываем категориальный признак в числовой
    X['region'] = label_encoder.fit_transform(X['region'])

    # Выбираем лучшие K признаков с использованием критерия хи-квадрат
    selector = SelectKBest(chi2, k=2)
    X_new = selector.fit_transform(X, y)

    # Создаем DataFrame из X_new с исходными названиями столбцов
    X_new = pd.DataFrame(X_new, columns=X.columns[selector.get_support()])
    print(X_new)
    df = pd.DataFrame(X_new)
    df.to_csv('X_new', index=False)
