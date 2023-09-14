from flask import Flask, request, jsonify
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Путь к файлу для сохранения модели
MODEL_FILE = 'flat_model.cbm'

# Функция для создания DataFrame и записи в CSV файл
def createFrame(filename='data.csv'):
    data = {
        'price': [158300, 200000, 120000, 140000, 180000] * 100,
        'region': ['A', 'B', 'A', 'C', 'B'] * 100,
        'rooms': [2, 3, 2, 1, 3] * 100,
        'floor': [5, 7, 3, 2, 6] * 100,
        'toilet_with_bathroom': [False, True, False, False, True] * 100,
        'kitchen_with_living_room': [True, True, False, True, False] * 100,
        'category': ['стандарт', 'улучшенный', 'стандарт', 'стандарт', 'улучшенный'] * 100
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Функция для обучения модели и сохранения результатов
def trainModel(filename='data.csv'):
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
    model.save_model(MODEL_FILE)

# Функция для классификации новой квартиры
def classifyFlat(new_flat):
    # Чтение обученной модели из файла
    model = CatBoostClassifier()
    model.load_model(MODEL_FILE)

    # Преобразование данных новой квартиры в DataFrame
    new_data = pd.DataFrame([new_flat])

    # Использование модели для предсказания
    predicted_category = model.predict(new_data)[0]

    # Преобразование обратно в текстовую категорию
    categories = ['стандарт', 'улучшенный']
    predicted_category = categories[predicted_category]

    return predicted_category

# Функция для загрузки обученной модели
def load_model():
    global model
    try:
        model = CatBoostClassifier()
        model.load_model('flat_model.cbm')
    except:
        trainModel()
        model = CatBoostClassifier()
        model.load_model('flat_model.cbm')

# Метод для обучения модели
# localhost:port/train
@app.route('/train', methods=['GET'])
def train():
    try:
        createFrame()  # Создание данных для обучения (может быть переделано для загрузки из запроса)
        trainModel()  # Обучение модели
        return jsonify({'message': 'model saved'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Метод для классификации новой квартиры
# localhost:port/classify
@app.route('/classify', methods=['GET'])
def classify():
    try:
        # Получение параметров из GET-запроса
        price = request.args.get('price')
        region = request.args.get('region')
        rooms = request.args.get('rooms')
        floor = request.args.get('floor')
        toilet_with_bathroom = request.args.get('toilet_with_bathroom')
        kitchen_with_living_room = request.args.get('kitchen_with_living_room')

        # Преобразование параметров в формат, подходящий для модели
        # Здесь можно добавить код для преобразования данных

        # Прогнозирование с использованием обученной модели
        predicted_category = model.predict([[
            price, region, rooms, floor, toilet_with_bathroom, kitchen_with_living_room
        ]])[0]

        # Преобразование результатов в текстовую категорию
        categories = ['стандарт', 'улучшенный']
        predicted_category = categories[predicted_category]
        return f"Category: {predicted_category}"
    except Exception as e:
        return jsonify({'error': str(e)})

# *POST - отправление новых данных на сервер для сохранения
# *Новую строку можем послать для классификации

if __name__ == '__main__':
    load_model()
    app.run(debug=True)
