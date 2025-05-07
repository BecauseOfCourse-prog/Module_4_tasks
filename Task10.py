def selection_sort(arr):
    for i in range(len(arr)):
        cloud = arr[i]
        index = i
        for n in range(i,len(arr)):
            if arr[n] < cloud:
                index = n
                cloud = arr[n]
        arr[index] = arr[i]
        arr[i] = cloud

my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)