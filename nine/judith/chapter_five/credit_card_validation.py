to_check = input("Enter your credit card number")

if len(to_check) == 13 or len(to_check) == 16:
    print(True)
if to_check[0] == "4" or to_check[0] == "5" or to_check[0] == "6":
    print("CARD A")
if to_check[0] == "3" and to_check[1] == "7":
    print("CARD B")
print("Valid Card")
string_to_list = list(to_check.split())
add_element = to_check[::2]
total = 0
for i in range(len(add_element)):
    numbers = int(add_element[i])
    total += numbers

second_element = to_check[1::2]
total_second_element = 0





print(add_element)
print(total)
