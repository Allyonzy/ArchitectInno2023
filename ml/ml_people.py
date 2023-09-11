# загрузка библиотек
import pandas as pd
import random

from sklearn.preprocessing import LabelEncoder

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.model_selection import train_test_split

from catboost import CatBoostClassifier #ставим дополнительно через pip или conda

from sklearn.metrics import accuracy_score

#работа с моделью в браузере (подключение)
from flask import Flask, request, jsonify

# Набор def и классов
# Функция для классификации новой квартиры
def classifyStudent(new_student):
    # Чтение обученной модели из файла
    model = CatBoostClassifier()
    model.load_model(MODEL_FILE)

    # Преобразование данных студента в DataFrame
    new_data = pd.DataFrame([new_student])

    # Использование модели для предсказания
    predicted_category = model.predict(new_data)[0]

    # Преобразование обратно в текстовую категорию
    categories = [...] #категориальная по студентам
    predicted_category = categories[predicted_category]

    return predicted_category

#1. Входные данные (загрузка/генерация)
'''
Создайте датасет из не менее чем 2000 записей, содержащий данные о
среднем балле студентов (от 0 до 99) по 6 предметам и оценка итоговой
лабораторной работы (удовлетворительно, хорошо, отлично).
Названия предметов, средний балл, оценка  итоговой лабораторной работы задается произвольно 
на ваше усмотрение.

Строки датасета:
id # идентификатор студента
subjects = [{'math': score1}, {'reading': score2}, {'ml': score3}, {'physics': score4}, {'optimisation': score4}, {'sports': score5}] # список предметов
final_lab = ['удовлетворительно', 'хорошо', 'отлично'] # итоговая работа

Варианты получения: 
1. Преобразовать существующий датасет
2. Сгенерировать (random python)

Создать из датасета DataFrame

Разделить на X и y
X - все предметы + *студент*

id студента убрать из X

y - результирующий столбец, Final lab <- LabelEncoder()

'''

# 1. pd.csv() - если прочитать файл с данными
# df_student = pd.DataFrame() #сгенерировать массив студентов

subjects = [{'math': score1}, {'reading': score2}, {'ml': score3}, {'physics': score4}, 
            {'optimisation': score4}, {'sports': score5}] # список предметов

X = df_student[['math', 'reading', 'ml', 'physics', 'optimisation', 'sports']]
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df_student['final_lab'])

# 2. Выберите лучшие 3 признака для обучения
selector = SelectKBest(chi2, k=2)
X_new = selector.fit_transform(X, y)

# 3. Разбейте датасет на тестовую и обучающую выборку train_test_split (для лучших признаков)
# 80% обучающей выборки, 20% тестовой
X_train_eff, X_test_eff, y_train_eff, y_test_eff = train_test_split(X_new, y, test_size=0.2, random_state=1234)

# *3.1* Разбейте датасет на тестовую и обучающую выборку train_test_split (для всех признаков)
# 80% обучающей выборки, 20% тестовой
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# 4. Проведите обучение модели, результатом должна быть сохраненная модель.
# Обучаем модель CatBoostClassifier
model_eff = CatBoostClassifier(iterations=100, depth=4, learning_rate=0.1, cat_features=cat_features)
model_eff.fit(X_train_eff, y_train_eff)

model = CatBoostClassifier(iterations=100, depth=4, learning_rate=0.1, cat_features=cat_features)
model.fit(X_train, y_train)

# 5. Проведите тестирование модели, результатом должно быть число - точность модели (accuracy) на тестовой выборке.
# Делаем предсказания на тестовом наборе
y_pred_eff = model_eff.predict(X_test_eff)

y_pred = model.predict(X_test)

# Оцениваем точность модели
accuracy_eff = accuracy_score(y_test_eff, y_pred_eff)
print(f"Точность модели: {accuracy_eff}")

accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy}")

# Сохранить модель

# 6. Реализуйте функцию, которая на вход принимает оценку студента по 6 предметам и возвращает прогноз оценки.

# генерация новых данных new_student
# прогноз оценки через classifyStudent(new_student)