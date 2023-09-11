import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Функция для создания DataFrame и записи в CSV файл
def createFrame(filename='data.csv'):
    data = {
        'price': [150000, 200000, 120000, 140000, 180000],
        'region': ['A', 'B', 'A', 'C', 'B'],
        'rooms': [2, 3, 2, 1, 3],
        'floor': [5, 7, 3, 2, 6],
        'toilet_with_bathroom': [False, True, False, False, True],
        'kitchen_with_living_room': [True, True, False, True, False],
        'category': ['стандарт', 'улучшенный', 'стандарт', 'стандарт', 'улучшенный']
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def createTestFrame(filename='train_data.csv'):
    data = {
        'price': [150000, 200000, 120000, 140000, 180000],
        'region': ['A', 'B', 'A', 'C', 'B'],
        'rooms': [2, 3, 2, 1, 3],
        'floor': [5, 7, 3, 2, 6],
        'toilet_with_bathroom': [False, True, False, False, True],
        'kitchen_with_living_room': [True, True, False, True, False],
        'category': ['стандарт', 'улучшенный', 'стандарт', 'стандарт', 'улучшенный']
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Функция для классификации типов квартир
def flatClassifyingML(filename='data.csv'):
    # Определите категории заранее
    categories = ['стандарт', 'улучшенный']

    # Чтение данных из файла
    df = pd.read_csv(filename)

    # Преобразование категорий в числовые значения
    df['category'] = df['category'].apply(lambda x: categories.index(x))

    # Определение признаков и целевой переменной
    X = df.drop(columns=['category'])
    y = df['category']

    # Обучение модели CatBoostClassifier
    model = CatBoostClassifier(iterations=100, depth=4, learning_rate=0.1, cat_features=['region'])
    model.fit(X, y)

    # Сохранение модели в файл
    model.save_model('flat_model.cbm')

# Функция для классификации новой квартиры
def classifyFlat(new_flat, model_filename='flat_model.cbm'):
    # Чтение обученной модели из файла
    model = CatBoostClassifier()
    model.load_model(model_filename)

    # Преобразование данных новой квартиры в DataFrame
    new_data = pd.DataFrame([new_flat])

    # Использование модели для предсказания
    predicted_category = model.predict(new_data)[0]

    # Преобразование обратно в текстовую категорию
    categories = ['стандарт', 'улучшенный']
    predicted_category = categories[predicted_category]

    return predicted_category

# Класс для создания объекта Flat
class Flat:
    def __init__(self, price, region, rooms, floor, toilet_with_bathroom, kitchen_with_living_room):
        self.price = price
        self.region = region
        self.rooms = rooms
        self.floor = floor
        self.toilet_with_bathroom = toilet_with_bathroom
        self.kitchen_with_living_room = kitchen_with_living_room


# Функция для загрузки модели
def loadModel(model_filename):
    model = CatBoostClassifier()
    model.load_model(model_filename)
    return model

# Функция для тестирования модели и оценки точности
def testFlatClassifying(test_filename, model_filename):
    # Загрузить обученную модель
    model = CatBoostClassifier()
    model.load_model(model_filename)

    # Загрузить тестовый датафрейм
    test_df = pd.read_csv(test_filename)

    # Разделить признаки и целевую переменную
    X_test = test_df.drop(columns=['category'])
    y_test = test_df['category']

    # Предсказать категории на тестовом наборе
    y_pred = model.predict(X_test)

    # Создать объект LabelEncoder
    label_encoder = LabelEncoder()

    # Преобразовать истинные метки в числовой формат
    y_true_numeric = label_encoder.fit_transform(y_test)

    # Оценить точность модели
    accuracy = accuracy_score(y_true_numeric, y_pred)

    return accuracy

# Пример использования функций
if __name__ == '__main__':
    # Создание DataFrame и запись в CSV файл
    #createFrame()
    createTestFrame()

    # Обучение модели и сохранение результатов
    #flatClassifyingML()


    # Тестируем модель на тестовых данных и оцениваем точность
    test_accuracy = testFlatClassifying('train_data.csv', 'flat_model.cbm')
    print(f'Test accuracy: {test_accuracy}')

    # Пример классификации новой квартиры
    new_flat = Flat(price=160000, region='B', rooms=12, floor=6, toilet_with_bathroom=True, kitchen_with_living_room=True)
    category = classifyFlat(new_flat.__dict__)
    print(f'Predicted Category: {category}')

