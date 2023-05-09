#!/usr/bin/python3

for q in range(0, 10):
    for r in range(x + 1, 10):
        if q == 8 and r == 9:
            print('89')
        else:
            print('{}{}, '.format(q, r), end='')
