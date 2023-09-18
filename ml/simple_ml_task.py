'''
1. Примените алгоритм KNN (k-ближайших соседей) для данных по
заболеваемости сахарным диабетом. Датасет представлен по ссылке.
Выходной столбец “outcome” принимает значения 0 или 1 и является
классификатором текущего набора данных.
https://colab.research.google.com/drive/1fMkgigcGRx_9JYlZQ-JO09XkO_nHqmpa?usp=sharing 
https://colab.research.google.com/drive/128KXJlMWvuGIaDgmo3RF5Nf4O9puMqQL?usp=sharing 

80 на 20

- имеется диабет (значение 1)
- заболевание отсутствует (значение 0)
Используйте все остальные столбцы как data features (входные числовые
данные) для адаптации модели kNN.
Рассчитайте модель kNN для k = 5, 10, 15, 20, 25. 
Укажите объем тестового набора данных равным 25% от общего количества данных.
75 на 25
Укажите score модели и постройте визуализацию обученной классификации для указанных k.
https://scikit-learn.ru/3-3-metrics-and-scoring-quantifying-the-quality-of-predictions/ 
A, P, R, F1

2. Постройте модель множественной линейной регрессии для атрибутов X =
{SkinThickness, BMI} и Y = {Insulin} из датасета предыдущего задания.
Укажите score модели и предоставьте значения b, a1, a2 формулы:
y = b + a1*x1 + a2*x2 # формула матмодели для текущих данных

MSE, R^2
https://colab.research.google.com/drive/1ozolk-cjgIzrW7n__Z77EmPP6lYxYIQI?authuser=1 

3. Примените к указанным данным любую одну модель (решите сами - для задачи
классификации или задачи регрессии) из списка ниже
- SVM - classificator
- DecisionTree - classificator, regressor
- Полиномиальная регрессия - regressor

** Подумать как сделать программу

Набор файлов и def, class для элементов датасета
------------------------------
Функция импорта данных
class DiabetInfo
Функция обработки данных под модель
Алгоритм knn
Алгоритм регрессии
Алгоритм 3 (SVM, DecisionTree, Полиномиальная)
Оценка качества
Визуализация - отдельно для регрессии, отдельно для классификации
Экспорт алгоритма (модель)
Проверка на экпортированной модели
'''

# загрузка данных

# Разделение на тренировочную и тестовую

# X (data features) и y (outcome)

# Примените алгоритм KNN (k-ближайших соседей) для данных

# Рассчитайте модель kNN для k = 5, 10, 15, 20, 25.

# Укажите объем тестового набора данных равным 25% от общего количества данных

# Укажите score модели (метрики) и постройте визуализацию обученной классификации для указанных k.