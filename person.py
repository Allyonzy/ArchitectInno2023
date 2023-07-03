import pymorphy2

class Person():
    __age = 0
    # test = 89
    # _test = 98
    # __test = 7545

    def __init__(self, name: str):
        self.name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    @staticmethod
    def is_adult(age):
        print(age)
        if age > 18:
            return "Взрослый"
        else:
            return "Меньше 18 лет"
    

def multiply_age(age: int):
    print(age)
    return age ** 2


print("Распечатка значения name переменной", __name__)
if __name__ == '__main__':
    beta_person = Person('Beta')
    beta_person.age = 35

    print("Имя созданного класса", beta_person.name)
    print(beta_person.__dict__)
    print("Возраст созданного ", beta_person.__class__, beta_person.age)
    beta_person.age = 54
    print("Возраст созданного ", beta_person.__class__, beta_person.age)

    gamma_person = Person('Gamma')
    print("Имя созданного класса", gamma_person.name)
    print(gamma_person.__dict__)
    print("Возраст созданного ", gamma_person.__class__, gamma_person.age)

    print(gamma_person.is_adult(gamma_person.age))
    #print(gamma_person.is_adult())

    print(beta_person.is_adult(multiply_age(beta_person.age)))