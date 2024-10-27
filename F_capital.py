from typing import Iterable, Iterator

import self


class Cap_iter(Iterable[str]):
    def __init__(self, string: str) -> None:
        self.string = string

    def __iter__(self):
        return Cap_iterator(self.string)

class Cap_iterator(Iterator[str]):
    def __init__(self, string: str) -> None:
        self.words = [w.capitalize() for w in string.split(' ')]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word

if __name__ == '__main__':
    my_iterable= Cap_iter('the quick brown fox jumps over the lazy dog.')
    my_iterator= iter(my_iterable)
    while True:
        try:
            print(next(my_iterator), end= ' ')
        except StopIteration:
            break