def selectionSort(list):
   for fillslot in range(len(list)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if list[location]>list[positionOfMax]:
               positionOfMax = location

       temp = list[fillslot]
       alist[fillslot] = list[positionOfMax]
       alist[positionOfMax] = temp

list = [54,26,93,17,77,31,44,55,20]
selectionSort(list)
print(list)
