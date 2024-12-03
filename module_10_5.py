import time
import multiprocessing

def read_info(name):
    all_data = []

    with open(name, 'r') as file:
        while True:
            content = file.readline()
            all_data.append(content)
            if not content:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# линейный вызов
start = time.time()
for name in filenames:
    read_info(name)
finish = time.time()
print(f'линейный:{finish - start}')

# мультипроцессорный вызов
if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(processes=len(filenames)) as p:
        p.map(read_info, filenames)
    finish = time.time()
    print(f'мультипроцессорный:{finish - start}')