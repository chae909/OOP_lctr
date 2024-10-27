from typing import List

class EvenOnly(List[int]):
    def append(self, value:int)->None:
        if not isinstance(value,int):
            raise TypeError('value must be an integer')
        if value%2 != 0:
            raise ValueError('value must be an even number')

        super().append(value)

if __name__ == '__main__':
    data = ["a string", 3, 4, 8, 22, 1, "test"]

    even_data = EvenOnly()

    for itm in data:
        try:
            even_data.append(itm)
        except Exception:
            print(f"Skip item: {itm}")

    print(f'filtered data: {even_data}')