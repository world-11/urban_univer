import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import random

def tubes():
    tubes = np.arange(7, 55, 3.5)
    klem = tubes[1:].copy()
    tubes_indust = np.arange(300, 500, 15)
    total_tubes = np.concatenate((tubes_indust, tubes, klem))
    total_tubes.sort()
    klem = klem * 1.3
    print(f'Хозяйственные трубы: {tubes},\n'
          f'соединительные кольца: {klem}\n'
          f'ВСЕГО ЭЛЕМЕНТОВ: {total_tubes.size}')
    print(total_tubes)
    np.save('Трубы', 'a')

def dynamic():
    # help(np.random)
    fires = np.random.uniform(0, 150, 12)
    fig, ax = plt.subplots()
    y = [1,2,3,4,5,6,7,8,9,10,11,12]
    x = fires
    ax.plot(y, x)
    plt.plot(y, x, '-', color='green')
    plt.show()


def main():
    with requests.Session() as session:
        response = session.get('https://api.github.com/')
    print(response.headers)
    print(response.json())
    tubes()
    dynamic()


if __name__ == '__main__':
    main()

