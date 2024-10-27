def multiply(*args):
    print(f'전달인수: {args}', end='\t')

    z = 1
    for num in args:
        z *= num
    return z

print(f'곱: {multiply(3,4,5)}')

'''
'''

def myFun(arg1, **kwargs):
    print(f'first argument: {arg1}')
    print(f'second argument: {kwargs}')

myFun('hi', first='Geeks', mid='for', last='Geeks')

def student_info(*args, **kwargs):
    print(f'가변 길이 인수: {args}')
    print(f'키워드 가변 길이 인수: {kwargs}')

student_info('math', 'programming', name='Joy', age=20)