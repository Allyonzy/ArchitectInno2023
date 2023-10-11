import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
import os

# Предобработка данных
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),  # Случайное изменение размера и обрезка до 224x224 пикселей
        transforms.RandomHorizontalFlip(),  # Случайное горизонтальное отражение изображения
        transforms.ToTensor(),  # Преобразование в тензор (многомерный массив)
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),  # Изменение размера до 256x256 пикселей
        transforms.CenterCrop(224),  # Обрезка до 224x224 пикселей по центру»
        transforms.ToTensor(),  # Преобразование в тензор
    ]),
}

data_dir = 'images'  # Каталог с изображениями
batch_size = 32  # Размер пакета данных для обучения

# Создание ImageFolder датасета для обучения и валидации с использованием заданных трансформаций
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in ['train', 'val']}

# Создание DataLoader для загрузки данных с пакетами, перемешиванием и указанием числа рабочих процессов
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size, shuffle=True, num_workers=0) for x in ['train', 'val']}

# Определение размеров датасетов для обучения и валидации
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}

# Получение списка классов (классификация: кот или не-кот)
class_names = image_datasets['train'].classes

# Загрузка предварительно обученной модели ResNet18
model = models.resnet18(pretrained=True)

# Получение количества признаков в последнем полносвязном слое
num_ftrs = model.fc.in_features

# Замена последнего полносвязного слоя на слой с 2 выходами (2 класса: кот и не-кот)
model.fc = nn.Linear(num_ftrs, 2)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # Определение устройства (GPU или CPU)
model = model.to(device)  # Перемещение модели на выбранное устройство

# Определение функции потерь (cross-entropy) и оптимизатора (SGD)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Обучение модели
num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for inputs, labels in dataloaders['train']:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad() # стохастический градиентный спуск для обновления весов модели
        outputs = model(inputs)
        loss = criterion(outputs, labels) # принимает предсказанные значения модели и истинные (ожидаемые) значения (метки) и вычисляет, насколько они различаются.
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch {epoch + 1}, Loss: {running_loss / dataset_sizes['train']}")

# Сохранение модели
torch.save(model.state_dict(), 'cat_classification_model.pth')

# Классификация нового изображения
from PIL import Image
from torchvision import transforms

def classify_image(image_path):
    image = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    image = preprocess(image).unsqueeze(0)  # Добавление размерности батча (batch dimension)
    image = image.to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)

    return class_names[predicted[0]]

# Пример использования функции classify_image для классификации новых изображений
new_image_path = 'images/new_not_cat_image.jpeg'
predicted_class = classify_image(new_image_path)
print(f'Predicted Class: {predicted_class}')

#new_image_path = 'images/black.png'
#predicted_class = classify_image(new_image_path)
#print(f'Predicted Class: {predicted_class}')

