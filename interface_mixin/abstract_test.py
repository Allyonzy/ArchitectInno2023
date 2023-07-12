from abc import ABC, abstractmethod

class PersonAbstract(ABC):
    @property
    @abstractmethod
    def pos_x(self, pos_x):
        pass
    
    @property
    @abstractmethod
    def pos_y(self, pos_y):
        pass

    @pos_x.setter
    @abstractmethod
    def pos_x(self, pos_x):
        self._pos_x = pos_x
    
    @pos_y.setter
    @abstractmethod
    def pos_y(self, pos_y):
        self._pos_y = pos_y

    @abstractmethod
    def move(self):
        print('Движение')
        pass

    @abstractmethod
    def work(self):
        print('Работа')
        pass

class Developer(PersonAbstract):
    def move(self):
        super().move()
        print('Идти на митинг')

    def work(self):
        pass

    @property
    def pos_x(self):
        return self.pos_x
    
    @property
    def pos_y(self):
        return self.pos_y
    
    @PersonAbstract.pos_x.setter
    def pos_x(self, pos_x):
        self.pos_x = pos_x
    
    @PersonAbstract.pos_y.setter
    def pos_y(self, pos_y):
        self.pos_y = pos_y


dev = Developer()
dev.move()
dev.work()
dev.pos_x = 0.0
dev.pos_y = 0.0

print(dev.pos_x)
print(dev.pos_y)