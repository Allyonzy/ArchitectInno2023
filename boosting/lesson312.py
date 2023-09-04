import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Генерируем тестовые данные и сохраняем их в файл data.csv
data = {
    'цена': [1000000, 1500000, 800000, 1200000, 900000] * 20000,
    'район': ['A', 'B', 'C', 'B', 'A'] * 20000,
    'комнаты': [3, 2, 4, 3, 2] * 20000,
    'этаж': [2, 3, 1, 2, 3] * 20000,
    'санузел': [False, True, True, False, True] * 20000,
    'кухня_гостиная': [True, False, False, True, False] * 20000,
    'тип_квартиры': ['стандарт', 'улучшенный', 'стандарт', 'стандарт', 'улучшенный'] * 20000
}

df = pd.DataFrame(data)
df.to_csv('train_data.csv', index=False)

# Загружаем данные из файла data.csv
df = pd.read_csv('data.csv')

# Преобразуем категориальные признаки в числовые с помощью Label Encoding
cat_features = ['район', 'санузел', 'кухня_гостиная']
for feature in cat_features:
    df[feature] = df[feature].astype('category')

# Разделяем данные на обучающий и тестовый наборы
X = df.drop('тип_квартиры', axis=1)
y = df['тип_квартиры']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучаем модель CatBoostClassifier
model = CatBoostClassifier(iterations=100, depth=4, learning_rate=0.1, cat_features=cat_features)
model.fit(X_train, y_train)

# Делаем предсказания на тестовом наборе
y_pred = model.predict(X_test)

# Оцениваем точность модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy}")
