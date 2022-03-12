def product_list(my_list):
    product = 1
    for i in my_list:
        product *= i
    return product


int_list = []
value = int(input('enter the number of input'))
for i in range(0, value):
    user_input = int(input('enter a number'))
    int_list.append(user_input)

print(product_list(int_list))
