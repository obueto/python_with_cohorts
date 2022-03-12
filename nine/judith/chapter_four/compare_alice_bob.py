a = [1, 2, 3]
b = [3, 2, 1]



def compare_array(a, b):
    a_counter = 0
    b_counter = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_counter += 1
        elif a[i] == b[i]:
            a_counter += 0
            b_counter += 0
        else:
            b_counter += 1
    return [a_counter, b_counter]


print(compare_array(a, b))
