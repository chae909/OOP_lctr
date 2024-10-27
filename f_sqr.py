my_lst = [1,2,3,4,5]
sqr_lst = [x*x for x in my_lst]

print(sqr_lst)

print('sqr_lst의 순차적 아이템 액세스:', end=' ')
for itm in my_lst:
    print(itm, end=' ')

print(f'\nsqr_lst의 개별 아이템 액세스: ', end=' ')
print(f'네번째 아이템: {sqr_lst[3]}')

'''
'''

sqr_generator = (x*x for x in my_lst)
print(sqr_generator)

print('sqr_generator의 순차적 아이템 액세스:', end=' ')
for itm in sqr_generator:
    print(itm, end=' ')

'''
'''

from sys import getsizeof

sqr_num = [n**2 for n in range(1, 1000001)]
print(f'\nlist comprehension sqr_num의 메모리 크기: {getsizeof(sqr_num)} 바이트')
print(f'1..1000000의 제곱합: {sum(sqr_num)}')

sqr_gen = (n**2 for n in range(1, 1000001))
print(f'generator expression sqr_gen의 메모리 크기: {getsizeof(sqr_gen)} 바이트')
print(f'1..1000000의 제곱합: {sum(sqr_gen)}')