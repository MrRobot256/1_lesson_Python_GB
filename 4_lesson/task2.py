# Задание 2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [my_list[number] for number in range(1, len(my_list)) if my_list[number] > my_list [number - 1]]

print(new_list)
