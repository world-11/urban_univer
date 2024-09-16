import asyncio
import time

async def start_strongman(name, power):
    ball = 0
    while ball <= 5:
        if ball == 0:
            print(f'Силач {name} начал соревнования.')
            await asyncio.sleep(1 / power)
        else:
            print(f'Силач {name} поднял {ball} шар')
            await asyncio.sleep(1 / power)
        ball += 1
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    print('Дан старт соревнованиям!')
    task1 = asyncio.create_task(start_strongman('ВАЛЕРИЙ', 3))
    task2 = asyncio.create_task(start_strongman('АЛЕКСАНДР', 4))
    task3 = asyncio.create_task(start_strongman('МАГОМЕД', 5))
    await task1
    await task2
    await task3
    print('Соревнования закончились')

asyncio.run(start_tournament())