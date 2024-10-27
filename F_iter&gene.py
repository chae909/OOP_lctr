class CountDown:
    def __init__(self, start):
        self.counter = start+1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter -= 1
        if self.counter == 0:
            raise StopIteration

        return self.counter

if __name__ == '__main__':
    cd = CountDown(5)

    for count in cd:
        print(f'{count}', end=' ')

'''
'''

class CountDown2:
    def __init__(self, start):
        self.counter = start+1

    def start_count(self):
        self.counter -= 1

        while self.counter > 0:
            yield self.counter
            self.counter -= 1

if __name__ == '__main__':
    cd = CountDown2(5)
    cd_generator = cd.start_count()

    for count in cd_generator:
        print(f'{count}', end=' ')