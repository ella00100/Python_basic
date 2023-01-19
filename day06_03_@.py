
def document_it(func): #decorator 생성
    def new_function(*args, **kwargs):
        print('실행 중인 함수: ', func.__name__)
        print('위치 기반 인수들: ', args)
        print('키워드 기반 인수들:', kwargs)
        result = func(*args, **kwargs)
        print('실행 결과: ', result)
        return result
    return new_function

@document_it
def sub_int(x,y):
    return x - y
@document_it
def squrare(n):
    return n*n

print(sub_int(7,3))
print(squrare(5))