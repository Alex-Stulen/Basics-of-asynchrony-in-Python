# Source:
#   YouTuber Oleg Molchanov
#   Video: https://www.youtube.com/watch?v=5SyA3lsO_hQ&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=6

"""
Корутины или сопрограммы по своей сути это генераторы, которые в процессе работы
принимать из вне какие-то данные.
Делается это с помощью метода .send (есть у генераторов такой метод).

PS:
    НАЗВАНИЕ ДЕКОРАТОРА coroutine В КОДЕ НИЖЕ, ЯВЛЯЕТСЯ ОШИБОЧНЫМ!
    ЭТО ПРОСТО ДЕКОРАТОР, КОТОРЫЙ ИНИЦИАЛИЗИРУЕТ ГЕНЕРАТОР,
    ТО ЕСТЬ ПЕРЕВОДИТ ГЕНЕРАТОР ИЗ СОСТОЯНИЯ GEN_CREATED
    В СТОСТОЯНИЕ GEN_SUSPENDED.
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


# Example 1:
def subgen():
    x = 'Ready to accept message'
    message = yield x
    print(f'message received: {message}')


# g = subgen()
# Мы не можем просто взять и для генератора вызвать метод .send.

# Проверяем состояние генератора.
# getgeneratorstate(g)  # Вернет 'GEN_CREATED'

# Сперва нужно вызвать метод .send и передать аргумент None.
# Когда мы передадим в метод .send аргумент None, то генератор сдвинется до следующего yield.
# response = g.send(None)
# print(response)
# Output:
# Ready to accept message

# Теперь если мы проверим состояние генератора, то:
# getgeneratorstate(g)  # Вернет 'GEN_SUSPENDED', означает что генератор приостановлен.

# Теперь мы можем вызвать метод .send с другим аргументом:
# g.send('OK')
# Output:
# message received: OK
# and StopIteration error

"""
Таким образом yield может быть одновременно быть в двух состояниях:
1. Отдавать данные.
2. Принимать данные через метод .send.

Сначала yield отдаст данные и потом выполнения сдвинется до этого момента.
А потом, если снова вызвать метод .send, yield уже будет принимать данные.
Таким образом yield как двухсторонняя форточка, через которую мы можем отдавать данные
и получать данные.
"""


# Example 2:
# Функция, которая будет возвращать среднее арифметическое.
@coroutine
def average():
    count = 0
    summa = 0
    average_ = None

    while True:
        try:
            x = yield average_
        except StopIteration:
            print('Done!')
            break
        else:
            count += 1
            summa += x
            average_ = round(summa / count, 2)

    return average_

# Мы не просто так написали блок try/except у бесконечного генератора.
# Так как у генераторов есть метод .throw, которые принимает класс исключения и выбросит это исключение.


"""
В генераторах можно явно вернуть значение через ключевое слово return.
Таким образом генератор заканчивает свое генеративное существование и не сможет отдавать значения, как до этого.
Чтобы снова использовать генератор, его нужно заново инициализировать.

Example:
try:
    g = average()
    g.send(5)
    g.send(6)
    g.send(1)
    g.throw(StopIteration)
except StopIteration as e:
    print('Average:', e.value)

# Output:
# Done!
# Average: 4.0

В таком случае мы бросаем исключение StopIteration в генератор,
он останавливается, возвращает значение average_ через ключевое слово return, 
сразу ловим это исключение и получение значение через ошибку e.value, которое вернул генератор. 
"""