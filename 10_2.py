# 2)	Отсортируйте массив чисел НЕ ИСПОЛЬЗУЯ МЕТОД sort()

num = [1,6,3,6,9,6,2,1,3,567,43,2,21,3,5,6876]

for i in range(len(num)):
    for x in range(i, len(num)):
        if num[i] > num[x]:
           num[i], num[x] = num[x], num[i]

print(num)