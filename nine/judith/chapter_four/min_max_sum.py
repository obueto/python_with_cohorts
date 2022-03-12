# import sys
#
# arr = [1, 3, 5, 7, 9]
# max_number = -sys.maxsize
# min_number = sys.maxsize
#
# for i in range(len(arr)):
#     total = 0
#     for j in range(len(arr)):
#         total += arr[j]
#         value = total - arr[i]
#
#     if value > max_number:
#         max_number = value
#
#     elif value < min_number:
#         min_number = value
# print(max_number, min_number)

a_list = []
for i in range(1, 6):
    a_list += [i]
print(a_list)

b_list = [12, 23, 32, 21]
c_list = [23, 54, 33, 29]
concatenated_list = b_list + c_list
print(concatenated_list)


def cube_list(values):
    for j in range(len(values)):
        values[j] **= 3


number_to_cube = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube_list(number_to_cube)
print(number_to_cube)

characters = []
characters += 'Birthday'
print(characters)

