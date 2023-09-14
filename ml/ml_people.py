# загрузка библиотек
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder # кодирование категориальных
from sklearn.feature_selection import SelectKBest # выбор признаков
from sklearn.feature_selection import chi2 # выбор по Хи квадрат

from sklearn.model_selection import train_test_split # деление на тест и обучение
# 0.2 тестовой к 0.8, 0.3 к 0.7 тренировочной

from catboost import CatBoostClassifier #ставим дополнительно через pip или conda

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# критерий качества, точность accuracy
# precision_score, recall_score, f1_score (confusion_matrix)

# работа с моделью в браузере (подключение)
# * реализовать интерфейсную часть (API)
from flask import Flask, request, jsonify

#TODO добавить Flask

# Набор констант по программе
MODEL_FILE_EFF = 'people_university_model_eff.cbm' # модель с 3 лучшими признаками
MODEL_FILE = 'people_university_model.cbm' # модель 
DF_COUNT = 2001  # число строк 
SUBJ_COUNT = 6  # число предметов
MIN_GRADE = 0  # мин балл
MAX_GRADE = 99  # макс балл
FINAL_RESULT_LIST = ['удовлетворительно', 'хорошо', 'отлично']  # результат теста

# Набор def и классов

def generate_students():
    '''
    Создайте датасет из не менее чем 2000 записей, содержащий данные о
    среднем балле студентов (от 0 до 99) по 6 предметам и оценка итоговой
    лабораторной работы (удовлетворительно, хорошо, отлично).

    Строки датасета:
    id # идентификатор студента
    subjects = [{'math': score1}, {'reading': score2}, {'ml': score3}, {'physics': score4}, {'optimisation': score4}, {'sports': score5}] # список предметов
    final_lab = ['удовлетворительно', 'хорошо', 'отлично'] # итоговая работа

    Варианты получения: 
    1. Преобразовать существующий датасет
    2. Сгенерировать (random python)

    Создать из датасета DataFrame
    '''
    def generate_final(row):
        # TODO поменять random
        # Балл ниже 30 - удовл
        cond_c = row['mean_score'] < 35
        # Балл 35 - 60 - хор
        cond_b = row['mean_score'] >= 35 
        cond_b_1 = row['mean_score'] < 60
        # Балл 60 - 100 - отл
        cond_a = row['mean_score'] >= 60
        val = ''
        if(cond_c):
            val = FINAL_RESULT_LIST[0]
        elif(cond_b and cond_b_1):
            val = FINAL_RESULT_LIST[1]
        else:
            val = FINAL_RESULT_LIST[2]
        # return FINAL_RESULT_LIST[0] if cond_c else (FINAL_RESULT_LIST[1] if cond_b else FINAL_RESULT_LIST[2])
        return val

    subjects = [f"subject_{num + 1}" for num in range(SUBJ_COUNT)]

    grades = np.random.randint(MIN_GRADE, MAX_GRADE + 1, (DF_COUNT, SUBJ_COUNT))
    student_scores = pd.DataFrame (grades, columns = subjects)
    
    student_scores.sum(axis=0) # axis 1 - по столбцам, axis 0 - построчно, сумма
    student_scores['mean_score'] = np.round((student_scores.sum(axis=1)/SUBJ_COUNT), 3)
    print(student_scores.head(5))
    
    # apply - применить функцию к датасету
    student_scores['final_lab'] = student_scores.apply(generate_final, axis=1)
    return student_scores



def classifyStudent(new_student, new_columns, model_file, categories=[0, 1, 2]):
    '''
    Функция для классификации студентов
    @param new_student - массив ключ-значение или строка в датасете
    '''
    # Чтение обученной модели из файла
    model = CatBoostClassifier()
    model.load_model(model_file)

    # Преобразование данных студента в DataFrame
    new_data = pd.DataFrame([new_student], columns=new_columns)

    # Использование модели для предсказания
    predicted_category = model.predict(new_data)[0]

    # Преобразование обратно в текстовую категорию
    categories = [...] #категориальная по студентам
    predicted_category = categories[predicted_category]

    return predicted_category

def create_new_dataset():
    df = generate_students()
    df.to_csv('ml/student.csv', index=False)

def preprocess_dataset(
            file='ml/student.csv', 
            to_drop=['final_lab', 'mean_score'], 
            y_name='final_lab',
            need_to_encode_y=True,
            need_best_features=True,
            test_size=0.2,
            random_state=1234
        ):
    '''
    Разделить на X и y
    X - все предметы + *студент*

    id студента убрать из X

    y - результирующий столбец, Final lab <- LabelEncoder()

    '''
    df = pd.read_csv(file)
    X = df.drop(columns=to_drop, axis=1)
    print(X)
    y = df[y_name] #Series
    print(y)

    if (need_to_encode_y):
        label_encoder = LabelEncoder()
        temp = label_encoder.fit_transform(y)
        new_result = pd.DataFrame([y, temp], columns=['y', 'encoded_y'])
        new_result.to_csv('ml/result_labels.csv', index=False)
        y = temp       
        print(y)

    if (need_best_features):
        # 2. Выберите лучшие 3 признака для обучения
        selector = SelectKBest(chi2, k=3)
        X = selector.fit_transform(X, y)

    # 3. Разбейте датасет на тестовую и обучающую выборку train_test_split (для лучших признаков)
    # 80% обучающей выборки, 20% тестовой
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train, iterations=100, depth=4, learning_rate=0.1, file_to_save=MODEL_FILE):
    # # 4. Проведите обучение модели, результатом должна быть сохраненная модель.
    # # Обучаем модель CatBoostClassifier
    model = CatBoostClassifier(iterations=iterations, depth=depth, learning_rate=learning_rate)
    model.fit(X_train, y_train)
    # Сохранение модели в файл
    model.save_model(file_to_save)

def model_report(model, X_test, y_test, average='weighted'):
    # 5. Проведите тестирование модели, результатом должно быть число - точность модели (accuracy) на тестовой выборке.
    # Делаем предсказания на тестовом наборе
    y_pred = model.predict(X_test)

    # Оцениваем точность модели
    accuracy_eff = accuracy_score(y_test, y_pred)
    print(f"Правильность (accuracy) модели: {accuracy_eff}")

    precision_eff = precision_score(y_test, y_pred, average=average)
    print(f"Точность (precision) модели: {precision_eff}")

    recall_eff = recall_score(y_test, y_pred, average=average)
    print(f"Полнота (recall) модели: {recall_eff}")

    f1_eff = f1_score(y_test, y_pred, average=average)
    print(f"F1 мера модели: {f1_eff}")

# #Натренировать модель
# X_train, X_test, y_train, y_test = preprocess_dataset()
# train_model(X_train, y_train)
# new_model = CatBoostClassifier()
# new_model.load_model(MODEL_FILE)
# model_report(new_model, X_test, y_test, average='weighted')


# # Сохранить модель

# # 6. Реализуйте функцию, которая на вход принимает оценку студента по 6 предметам и возвращает прогноз оценки.

new_grades = np.random.randint(MIN_GRADE, MAX_GRADE + 1, SUBJ_COUNT)
print(new_grades)
result = classifyStudent(new_grades, MODEL_FILE)

print(f"Студент скорее всего получит: {result}")

result = classifyStudent(new_grades, MODEL_FILE_EFF)

print(f"Студент скорее всего получит (если была модель с SelectBestK): {result}")

# # генерация новых данных new_student
# # прогноз оценки через classifyStudent(new_student)