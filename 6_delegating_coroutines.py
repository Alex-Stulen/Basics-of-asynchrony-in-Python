# Source:
#   YouTuber Oleg Molchanov
#   Video: https://www.youtube.com/watch?v=5SyA3lsO_hQ&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=6

"""
Делегирующий генератор - это генератор, который вызывает какой-то другой генератор.
Под генератор - это вызываемый генератор.
Такая конструкция возможна, когда нам один генератор нужно разбить на несколько.
"""

from inspect import getgeneratorstate
from functools import wraps


def coroutine(generator_func):
    # Декоратор, который будет автоматически инициализировать генератор
    # и вызывать первый раз метод .send с аргументом None,
    # чтобы генератор перешёл в состояние GEN_SUSPENDED, то есть приостановлен.
    @wraps(generator_func)
    def wrapper(*args, **kwargs):
        g = generator_func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper


class BlaBlaException(Exception):
    pass


def subgen():
    for i in 'oleg':
        yield i


def delegator(g):
    # g - some another generator.
    for i in g:
        yield i


# Example:
# sb = subgen()
# g = delegator(sg)
# next(g) -> o
# next(g) -> l
# next(g) -> e
# next(g) -> g

"""
Таким образом генератор delegator отдаёт те же значения, что и subgen, 
но при этом delegator не знает реализации subgen, который пришел в качестве аргумента.
"""


# @coroutine  # этот декоратор не нужен, если мы будем использовать декоратор через конструкцию yield from
def subgen2():
    while True:
        try:
            message = yield
        except BlaBlaException:
            print('Ku-Ku!!!')
        else:
            print('.........', message)


@coroutine
def delegator2(g):
    # g - some another generator

    # old example
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)

    yield from g


"""
Обрати внимание на исключение. Если необходимо, то нужно пробрасывать исключение и в под-генератор. 
Таким образом мы можем перехватывать исключения и пробрасывать их в делегирующие (под) генераторы.
"""


"""
Но всё это занимает много кода. Хотелось бы как-то сократить написание кода.
Для этого используется конструкция yield from <generator>.

Если мы используем yield from, то нам не нужно инициализировать под-генератор декоратором coroutine,
yield from это делаем самостоятельно.

Еще yield from полезен тем, что именно он принимает значение, которое под-генератор будет возвращать 
через ключевое слово return, и нам не нужно отлавливать ошибку StopIteration и получать значение через .value
этой ошибки.

На самом деле yield from просто отъилдивает значения из итерируемого объекта.
Можно записать это так:

    def gen():
        yield from [1, 2, 3, 4]
        
и этот генератор gen будет отдавать по одной цифре из списка при каждом вызове next,
пока не закончит работу и не выкинет исключение StopIteration. 
"""