import array as arr

list_array = arr.array('i',[2,3,4,5,55,53,32,234,441])

print("array before any even or odd lists",end="\n")

even_list = []
odd_list = []
for i in range(len(list_array)):
    if list_array[i] % 2 == 0:
        even_list.append(list_array[i])
    else:
        odd_list.append(list_array[i])
print("Even list" + str(even_list) ,end ="\n")
print("Odd list" + str(odd_list) ,end ="\n")

