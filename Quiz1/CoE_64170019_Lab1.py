def merge() :#empty list2 decleration

    list1=[]#empty list1 decleration
    list2=[]#empty list2 decleration

    numberOfElementsList1=int(input("Enter number of elements for list1:"))#this variable equals len(list1)
    for i in range(1,numberOfElementsList1+1):
        valuesOfList1=int(input("Enter list1:"))#entering values for list1
        list1.append(valuesOfList1)#append of entered values to the list1 

    numberOfElementsList2=int(input("Enter number of elements for list2:"))#this variable equals len(list2)
    for i in range(1,numberOfElementsList2+1):
        valuesOfList2=int(input("Enter list2:"))#entering values for list2
        list2.append(valuesOfList2)#append of entered values to the list2
   
    mergedList = list1+list2#merging list1 and list2
    return mergedList#return merged list

print("The merged list is" , merge())
