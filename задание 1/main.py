n = int(input("Введите длину массива: "))
m = int(input("введите интервал: "))-1
i=0
print (i*m+1-n*(i*m//n))
while((i+1)*m % n !=0):
    i = i + 1
    print (i*m+1-n*(i*m//n))




