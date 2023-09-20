
class MetersToKilometers:
    __km = 0

    def __init__(self, metres: float = 0):
        self.__metres = metres
        self.__km = self.to_kilometres()

    def to_kilometres(self):
        self.__km = self.__metres / 1000
        return self.__km
    
    def set_kilometres(self, new_km):
        if isinstance(new_km, (int, float)):
            self.__km = new_km
            self.__metres = new_km * 1000
        else:
            raise ValueError('Километры - это число')
        
    def get_km(self):
        return self.__km
    
    def __str__(self):
        return "MetersToKilometers metres: {0}, km: {1}".format(self.__metres, self.__km)
    
    
class ConverterMToKmAndMiles:
    __km = 0

    def __init__(self, metres: float = 0):
        self.__metres = metres
        self.__km = self.__metres / 1000 #TODO рефакторинг
   
    @property    
    def km(self):
        return self.__km
    
    @km.setter
    def km(self, new_km):
        if isinstance(new_km, (int, float)):
            self.__km = new_km
            self.__metres = new_km * 1000
        else:
            raise ValueError('Километры - это число')
        
    def to_kilometres(self):
        return self.__metres / 1000
    
    def to_miles(self):
        return self.__metres * 0.000621
    
    def __str__(self):
        return "ConverterMToKmAndMiles metres: {0}, km: {1}".format(self.__metres, self.__km)
    
if __name__ == "__main__":
    print('test')



