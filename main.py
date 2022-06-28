my_list = input("Введите числа через пробел: ")
my_list = my_list.split()
my_list = [int(x) for x in my_list]
a = list(map(lambda x: x + 10, my_list))
b = list(filter(lambda x: x >= 15, a))
print(a)
print(b)