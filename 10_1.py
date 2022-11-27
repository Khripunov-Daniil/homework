# 1)	Дан массив с числами и строками внутри, необходимо удалить все строки с массива и оставить в нем только числа

# первый вариант решения

arr = ['hello', 1, 2, "world", 5, 9, "sdfkjslff", 3, 6, "sdesw", 9]
for i in arr:
    if type(i) == str :
        arr.remove(i)
print(arr)
#         arr.pop[i]
# print(arr)


# второй вариант решения

res = [i for i in arr if type(i) == int and i > 0]
print(res)
