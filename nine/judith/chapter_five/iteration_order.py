#list_order = [[23, 5, 86], [57, 9, 0]]
# for i, row in enumerate(list_order):
#
#     for j, column in enumerate(row):
#         print('{:<8} {:<15} '.format( column,row), end=' ')
#
# print(f'[{i}] [{j}]= {row} ', end=' ')

# for row in list_order:
#
#     for item in row:
#
#         print(item,end=' ')
#     print()


import random

number = [random.randrange(1, 6) for i in range(50)]
from collections import Counter
counter = Counter(number)
for value,count in sorted(counter.items()):
    print(f'{value:<3} {count}')
