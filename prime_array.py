import array as arr
list1 = arr.array('i',[53,44,33,45,644,4434,755])
count = 1
prime_list = []

for j in list1:
    count = 1
    for i in range(2,j//2):
        if j%i == 0:
            count = 0
            break
    if count == 1:
        prime_list.append(j)

print(prime_list)






