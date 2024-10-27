from collections.abc import Container

class OddIntegers:
    def __contains__(self, item:int):
        return item %2 != 0

if __name__ == '__main__':
    odds = OddIntegers()

    print(isinstance(odds, Container))
    print(1 in odds)
    print(2 in odds)


'''   
__contains__(self, item) -> bool:

기능: Container객체에 item이 존재하는지 여부 반환
대응 연산자: in   
'''