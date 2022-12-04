# python learing
# author:TNT
from collections import deque
from random import randint
import pickle


queue = deque([], 5)
M = randint(0, 100)
def guess(k):
    if k == M:
        print('right')
        return True
    if k < M:
        print('%s is less - than M' % k)
    else:
        print('%s is greater - than M' % k)
    return False

while True:
    line = input('Please input a number:')

    if line.isdigit():
        k = int(line)
        queue.append(k)
        if guess(k):
            break
    elif line == 'h%':
        print(queue)



