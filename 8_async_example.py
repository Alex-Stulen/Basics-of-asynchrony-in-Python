# Суть примера: скачивание файлов заглушек в синхронном варианте и асинхронном.
import time


# Синхронный вариант:

# from time import time
#
# import requests
#
# URL = 'https://loremflickr.com/320/240'
#
#
# def get_file(url):
#     return requests.get(url, allow_redirects=True)
#
#
# def write_file(response: requests.Response):
#     filename = response.url.split('/')[-1]
#     with open(filename, mode='wb') as file:
#         file.write(response.content)
#
#
# def main():
#     t0 = time()
#
#     for _ in range(10):
#         write_file(get_file(URL))
#
#     print(time() - t0)
#
#
# if __name__ == '__main__':
#     main()

# ===================================================

# Асинхронный вариант

# import asyncio
# from time import time
#
# import aiohttp
#
# URL = 'https://loremflickr.com/320/240'
#
#
# def write_image(data: bytes):
#     filename = 'file-{}.jpeg'.format(int(time() * 1000))
#     with open(filename, mode='wb') as file:
#         file.write(data)
#
#
# async def fetch_content(url, session: aiohttp.ClientSession):
#     async with session.get(url, allow_redirects=True) as response:
#         data = await response.read()
#         write_image(data)
#
#
# async def main():
#     tasks = []
#
#     async with aiohttp.ClientSession() as session:
#         for _ in range(10):
#             task = asyncio.create_task(fetch_content(URL, session))
#             tasks.append(task)
#
#         await asyncio.gather(*tasks)
#
#
# if __name__ == '__main__':
#     t0 = time()
#     asyncio.run(main())
#     print(time() - t0)

# ===================================================

# Условный (демонстрационный) пример чисто на генераторах
# queue = []
#
#
# def counter():
#     c = 0
#     while True:
#         print('c:', c)
#         c += 1
#         yield
#
#
# def printer():
#     c = 0
#     while True:
#         if c % 3 == 0:
#             print('Bang!')
#         c += 1
#         yield
#
#
# def main():
#     while True:
#         task = queue.pop(0)
#         next(task)
#         queue.append(task)
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     g1 = counter()
#     queue.append(g1)
#
#     g2 = printer()
#     queue.append(g2)
#
#     main()
