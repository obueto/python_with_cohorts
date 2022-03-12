arr = [-4, 3, -9, 0, 4, 1]
positive_counter = 0
negative_counter = 0
zero_counter = 0
for i in range(len(arr)):
    if arr[i] > 0:
        positive_counter += 1
    elif arr[i] < 0:
        negative_counter += 1
    else:
        zero_counter += 1
print(f'{positive_counter / len(arr):6f}')
print(f'{negative_counter / len(arr):6f}')
print(f'{zero_counter/ len(arr):6f}')