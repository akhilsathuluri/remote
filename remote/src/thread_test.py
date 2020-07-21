import multiprocessing as mp
import time

def write_register(val):
    i = 0
    while True:
        i = i+1
        print('i =' , i)

def read_register(val):
    j = 0
    while True:
        j = j+1
        print('j =' , j)


if __name__ == "__main__":
    val = 0
    p1 = mp.Process(target=write_register, args = (val, ))
    p2 = mp.Process(target=read_register, args = (val, ))

    p1.start()
    p2.start()
