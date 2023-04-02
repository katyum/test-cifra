file = str(input("введите имя файла: "))
Nums = []
#testfile.txt
#считываем из файла, предполагая, что там только целые числа в столбик
with open(file) as f:
    for line in f:
        Nums.append(int(line))
    f.close()
#сортируем список и находим медиану
#четная нечетная длинна не влияют на результат
Nums = sorted(Nums)
med = Nums[(len(Nums) // 2)]
#Подсчитываем количество ходов
Sum = 0
for i in range(len(Nums)):
   Sum += abs(Nums[i]-med)
print(Sum)