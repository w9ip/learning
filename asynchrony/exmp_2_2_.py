import asyncio
import time


async def func1(x: int) -> None:
    print(x ** 2)
    await asyncio.sleep(3)
    print('func1 завершена')


async def func2(x: int) -> None:
    print(x ** 0.5)
    await asyncio.sleep(3)
    print('func2 завершена')


async def main():
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func1(5))

    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))
