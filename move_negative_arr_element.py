import array as arr

list1 = arr.array('i',[2,-34,-43,-22,3,0,30,4,-33,-4,3])

print(len(list1))
for j in range(len(list1)):
    for i in range(j+1,len(list1)):
        if list1[i] < list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
        print("swapping this {} with this {}".format(list1[i],list1[j]))
    print(list1)
