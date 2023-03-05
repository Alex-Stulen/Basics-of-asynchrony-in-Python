# Source:
#   YouTuber Oleg Molchanov
#   Video: https://www.youtube.com/watch?v=LO61F07s7gw&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=7


# План:
# 1. Asyncio - фреймворк для создания событийных циклов.
# 2. Пример простой асинхронной программы времён Python 3.4.
# 3. Синтаксис async/await на замену @asyncio.coroutine и yield from.
# 4. Пример асинхронного скачивания файлов.

"""

"""

import asyncio

# Event Loop:
#   coroutine > Task(Future)


# Метод версии python 3.4
# @asyncio.coroutine
# def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         yield from asyncio.sleep(0.1)
#
#
# @asyncio.coroutine
# def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print('{} seconds have passed'.format(count))
#
#         count += 1
#         yield from asyncio.sleep(1)
#
#
# @asyncio.coroutine
# def main():
#     task1 = asyncio.ensure_future(print_nums())
#     task2 = asyncio.ensure_future(print_time())
#
#     yield from asyncio.gather(task1, task2)


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()

# ==================================================

# Новый синтаксис начиная от python версии >= 3.5
# вместо декоратора asyncio.coroutine мы используем синтаксис async/await.
# async def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         await asyncio.sleep(0.1)
#
#
# async def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print('{} seconds have passed'.format(count))
#
#         count += 1
#         await asyncio.sleep(1)
#
#
# async def main():
#     # с python версии >= 3.6 таски нужно создавать через метод .create_task, а не через .ensure_future
#     task1 = asyncio.create_task(print_nums())
#     task2 = asyncio.create_task(print_time())
#
#     await asyncio.gather(task1, task2)
#
#
# if __name__ == '__main__':
#     # с python версии >= 3.7 запуск event loop происходит с помощью функции run
#     asyncio.run(main())
