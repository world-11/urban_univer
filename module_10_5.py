import datetime
import multiprocessing
# 0:00:02.288162
# 0:00:00.877263


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while file.readline() != '':
        all_data = file.readline()

# start1 = datetime.datetime.now()
# read_info('file 1.txt')
# read_info('file 2.txt')
# read_info('file 3.txt')
# read_info('file 4.txt')
# finish = datetime.datetime.now()
# print(finish - start1)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
        end = datetime.datetime.now()
        print(end - start)