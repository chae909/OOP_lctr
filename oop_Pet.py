from datetime import date

class Pet:
    def __init__(self, name, birthday:date)->None:
        self._name = name
        self._birthday = date.fromisoformat(birthday)

    @property
    def age(self):
        return date.today().year - self._birthday.year

    def eat(self)->None:
        print(f"'{self._name}' is eating now. yummy yum yum ...")

    def sleep(self)->None:
        print(f"'{self._name}' slept just before. zzz ...")

    def __str__(self)->None:
        return f"이름: {self._name}, 나이: {self.age}"

class Dog(Pet):
    def __init__(self, name:str, birthday:date, weight:float):
        super().__init__(name, birthday)
        self.__weight = weight

    @property
    def weight(self)->float:
        return self.__weight

    def bark(self):
        print(f"'{self._name}' is barking.")

    def sniff(self):
        print(f"'{self._name}' sniffs at my hand.")

    def __str__(self):
        return super().__str__() + f", 몸무게: {self.__weight}"

class Cat(Pet):
    def __init__(self, name:str, birthday:date, eye_col:str='black'):
        super().__init__(name, birthday)
        self.__eye_color = eye_col

    @property
    def eye_color(self):
        return self.__eye_color

    def mew(self):
        print(f"'{self._name}' make sound mew mew ....")

    def jump(self):
        print(f"'{self._name}' jumps to the shelf.")

    def __str__(self):
        return super().__str__() + f', 눈동자 색: {self.__eye_color}'

if __name__ == "__main__":
    my_pets = [Dog('Bomy', '20210320', 4),
               Dog('Gauly', '20220401', 2),
               Cat('Yang', '20200702', 'brown')]

    for pet in my_pets:
        print(pet)
        pet.eat()

        if isinstance(pet, Dog):
            pet.bark()
            pet.sleep()
        elif isinstance(pet, Cat):
            pet.mew()
            pet.jump()