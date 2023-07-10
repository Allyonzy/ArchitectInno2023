class Fish:
    def __init__(self):
        pass

    def __str__(self):
        return "рыба существует"


class Water:
    def __init__(self, fish: Fish):
        '''
        Инициализация класса
        @param fish - рыба, экземпляр класса Fish
        '''
        if isinstance(fish, Fish):
            self.fish = fish
        else:
            self.fish = Fish()

    def __str__(self):
        return f"{self.fish}"


water = Water('рыба')
print(water)

Water().__str__()
